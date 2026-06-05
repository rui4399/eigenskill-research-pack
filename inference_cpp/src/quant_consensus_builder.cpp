#include <algorithm>
#include <cctype>
#include <cmath>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

namespace fs = std::filesystem;

struct Options {
    std::string left_path;
    std::string right_path;
    std::string left_method = "loss_sensitive_4to8";
    std::string right_method = "loss_sensitive_4to8";
    int base_bits = 4;
    int high_bits = 8;
    double budget_avg_bits = 4.5;
    int selected_limit = 30;
    std::string out_json = "outputs/consensus_alloc_4to8_summary.json";
    std::string out_md = "outputs/consensus_alloc_4to8_report.md";
    std::string emit = "";
    bool no_write = false;
};

struct Group {
    std::string module;
    double cost = 0.0;
    int param_count = 0;
    int weight_params = 0;
    double positive_delta_nll = 0.0;
    int sensitivity_rank = 0;
};

struct ConsensusGroup {
    std::string module;
    double cost = 0.0;
    int param_count = 0;
    int weight_params = 0;
    double positive_delta_nll = 0.0;
    double left_positive_delta_nll = 0.0;
    double right_positive_delta_nll = 0.0;
    double avg_positive_delta_nll = 0.0;
    double consensus_score_delta_per_cost = 0.0;
    int left_sensitivity_rank = 0;
    int right_sensitivity_rank = 0;
};

struct Allocation {
    std::string path;
    std::string method;
    std::string model;
    std::vector<Group> groups;
    std::vector<int> bits;
};

struct Summary {
    std::string name;
    int groups = 0;
    double budget_avg_bits = 0.0;
    double memory = 0.0;
    double budget = 0.0;
    double budget_used = 0.0;
    double avg_bits = 0.0;
    std::map<int, int> bit_hist;
    double positive_delta_nll_total = 0.0;
    double positive_delta_nll_protected = 0.0;
    double positive_delta_nll_protected_ratio = 0.0;
};

struct Meta {
    double target_memory = 0.0;
    double actual_memory = 0.0;
    double budget_used = 0.0;
    int intersection_candidates = 0;
    int intersection_selected = 0;
    std::vector<std::string> skipped_intersection;
    int ranked_additions = 0;
    std::vector<std::string> ranked_addition_modules;
};

std::string read_text_file(const std::string& path) {
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("could not open file: " + path);
    }
    std::ostringstream ss;
    ss << in.rdbuf();
    return ss.str();
}

void write_text_file(const std::string& path, const std::string& text) {
    const fs::path out(path);
    if (!out.parent_path().empty()) {
        fs::create_directories(out.parent_path());
    }
    std::ofstream file(path);
    if (!file) {
        throw std::runtime_error("could not write file: " + path);
    }
    file << text;
}

std::size_t skip_ws(const std::string& text, std::size_t pos) {
    while (pos < text.size() && std::isspace(static_cast<unsigned char>(text[pos]))) {
        ++pos;
    }
    return pos;
}

std::size_t find_json_key(const std::string& text, const std::string& key, std::size_t start = 0) {
    return text.find("\"" + key + "\"", start);
}

std::size_t find_matching(const std::string& text, std::size_t open_pos, char open_ch, char close_ch) {
    if (open_pos >= text.size() || text[open_pos] != open_ch) {
        throw std::runtime_error("invalid json opener");
    }
    int depth = 1;
    bool in_string = false;
    bool escaped = false;
    for (std::size_t pos = open_pos + 1; pos < text.size(); ++pos) {
        const char ch = text[pos];
        if (in_string) {
            if (escaped) {
                escaped = false;
            } else if (ch == '\\') {
                escaped = true;
            } else if (ch == '"') {
                in_string = false;
            }
            continue;
        }
        if (ch == '"') {
            in_string = true;
        } else if (ch == open_ch) {
            ++depth;
        } else if (ch == close_ch) {
            --depth;
            if (depth == 0) {
                return pos;
            }
        }
    }
    throw std::runtime_error("unterminated json value");
}

std::string json_string_value(const std::string& object, const std::string& key) {
    std::size_t pos = find_json_key(object, key);
    if (pos == std::string::npos) return "";
    pos = object.find(':', pos);
    if (pos == std::string::npos) return "";
    pos = skip_ws(object, pos + 1);
    if (pos >= object.size() || object[pos] != '"') return "";
    ++pos;
    std::string out;
    bool escaped = false;
    for (; pos < object.size(); ++pos) {
        const char ch = object[pos];
        if (escaped) {
            out.push_back(ch);
            escaped = false;
        } else if (ch == '\\') {
            escaped = true;
        } else if (ch == '"') {
            return out;
        } else {
            out.push_back(ch);
        }
    }
    return "";
}

double json_number_value(const std::string& object, const std::string& key, double fallback) {
    std::size_t pos = find_json_key(object, key);
    if (pos == std::string::npos) return fallback;
    pos = object.find(':', pos);
    if (pos == std::string::npos) return fallback;
    pos = skip_ws(object, pos + 1);
    const std::size_t start = pos;
    while (pos < object.size()) {
        const char ch = object[pos];
        if ((ch >= '0' && ch <= '9') || ch == '-' || ch == '+' || ch == '.' || ch == 'e' || ch == 'E') {
            ++pos;
        } else {
            break;
        }
    }
    if (pos == start) return fallback;
    return std::stod(object.substr(start, pos - start));
}

std::string extract_object_value(const std::string& text, const std::string& key) {
    std::size_t pos = find_json_key(text, key);
    if (pos == std::string::npos) {
        throw std::runtime_error("json missing object: " + key);
    }
    pos = text.find('{', pos);
    if (pos == std::string::npos) {
        throw std::runtime_error("json field is not an object: " + key);
    }
    const std::size_t end = find_matching(text, pos, '{', '}');
    return text.substr(pos, end - pos + 1);
}

std::vector<std::string> extract_array_objects(const std::string& text, const std::string& array_key) {
    std::size_t pos = find_json_key(text, array_key);
    if (pos == std::string::npos) {
        throw std::runtime_error("json missing array: " + array_key);
    }
    pos = text.find('[', pos);
    if (pos == std::string::npos) {
        throw std::runtime_error("json field is not an array: " + array_key);
    }

    std::vector<std::string> objects;
    int bracket_depth = 1;
    int object_depth = 0;
    bool in_string = false;
    bool escaped = false;
    std::size_t object_start = std::string::npos;
    for (++pos; pos < text.size(); ++pos) {
        const char ch = text[pos];
        if (in_string) {
            if (escaped) {
                escaped = false;
            } else if (ch == '\\') {
                escaped = true;
            } else if (ch == '"') {
                in_string = false;
            }
            continue;
        }
        if (ch == '"') {
            in_string = true;
            continue;
        }
        if (ch == '[') {
            ++bracket_depth;
            continue;
        }
        if (ch == ']') {
            --bracket_depth;
            if (bracket_depth == 0) break;
            continue;
        }
        if (ch == '{') {
            if (object_depth == 0 && bracket_depth == 1) object_start = pos;
            ++object_depth;
            continue;
        }
        if (ch == '}') {
            --object_depth;
            if (object_depth == 0 && object_start != std::string::npos) {
                objects.push_back(text.substr(object_start, pos - object_start + 1));
                object_start = std::string::npos;
            }
        }
    }
    if (objects.empty()) {
        throw std::runtime_error("array contains no objects: " + array_key);
    }
    return objects;
}

std::vector<int> extract_int_array_from_object(const std::string& object, const std::string& key) {
    std::size_t pos = find_json_key(object, key);
    if (pos == std::string::npos) {
        throw std::runtime_error("json missing allocation method: " + key);
    }
    pos = object.find('[', pos);
    if (pos == std::string::npos) {
        throw std::runtime_error("allocation is not an array: " + key);
    }
    const std::size_t end = find_matching(object, pos, '[', ']');
    const std::string array_text = object.substr(pos + 1, end - pos - 1);
    std::vector<int> values;
    std::size_t cursor = 0;
    while (cursor < array_text.size()) {
        cursor = skip_ws(array_text, cursor);
        if (cursor < array_text.size() && array_text[cursor] == ',') {
            ++cursor;
            continue;
        }
        if (cursor >= array_text.size()) break;
        const std::size_t start = cursor;
        if (array_text[cursor] == '-' || array_text[cursor] == '+') ++cursor;
        while (cursor < array_text.size() && std::isdigit(static_cast<unsigned char>(array_text[cursor]))) {
            ++cursor;
        }
        if (cursor == start) {
            throw std::runtime_error("invalid integer array for allocation method: " + key);
        }
        values.push_back(std::stoi(array_text.substr(start, cursor - start)));
    }
    if (values.empty()) {
        throw std::runtime_error("empty allocation array: " + key);
    }
    return values;
}

std::string json_escape(const std::string& value) {
    std::string out;
    for (const char ch : value) {
        switch (ch) {
            case '\\': out += "\\\\"; break;
            case '"': out += "\\\""; break;
            case '\n': out += "\\n"; break;
            case '\r': out += "\\r"; break;
            case '\t': out += "\\t"; break;
            default: out.push_back(ch); break;
        }
    }
    return out;
}

std::vector<Group> read_groups(const std::string& text) {
    const std::vector<std::string> objects = extract_array_objects(text, "groups");
    std::vector<Group> groups;
    groups.reserve(objects.size());
    for (std::size_t i = 0; i < objects.size(); ++i) {
        Group group;
        group.module = json_string_value(objects[i], "module");
        group.cost = json_number_value(objects[i], "cost", 0.0);
        group.param_count = static_cast<int>(json_number_value(objects[i], "param_count", 0.0));
        group.weight_params = static_cast<int>(json_number_value(objects[i], "weight_params", 0.0));
        group.positive_delta_nll = json_number_value(objects[i], "positive_delta_nll", 0.0);
        group.sensitivity_rank = static_cast<int>(json_number_value(objects[i], "sensitivity_rank", 0.0));
        if (group.module.empty()) {
            throw std::runtime_error("group missing module at index " + std::to_string(i));
        }
        if (group.cost <= 0.0 || !std::isfinite(group.cost)) {
            throw std::runtime_error("group has invalid cost at index " + std::to_string(i));
        }
        groups.push_back(group);
    }
    return groups;
}

Allocation read_allocation(const std::string& path, const std::string& method) {
    const std::string text = read_text_file(path);
    Allocation allocation;
    allocation.path = path;
    allocation.method = method;
    allocation.model = json_string_value(text, "model");
    allocation.groups = read_groups(text);
    allocation.bits = extract_int_array_from_object(extract_object_value(text, "allocations"), method);
    if (allocation.groups.size() != allocation.bits.size()) {
        throw std::runtime_error(path + ": groups and allocation length differ");
    }
    return allocation;
}

std::map<int, int> bit_hist(const std::vector<int>& bits) {
    std::map<int, int> hist;
    for (int bit : bits) hist[bit] += 1;
    return hist;
}

std::string bit_hist_json(const std::map<int, int>& hist) {
    std::ostringstream out;
    out << "{";
    bool first = true;
    for (const auto& item : hist) {
        if (!first) out << ", ";
        first = false;
        out << "\"" << item.first << "\": " << item.second;
    }
    out << "}";
    return out.str();
}

std::vector<ConsensusGroup> make_consensus_groups(const Allocation& left, const Allocation& right) {
    if (left.groups.size() != right.groups.size()) {
        throw std::runtime_error("allocation group counts differ");
    }
    std::vector<ConsensusGroup> groups;
    groups.reserve(left.groups.size());
    for (std::size_t i = 0; i < left.groups.size(); ++i) {
        if (left.groups[i].module != right.groups[i].module) {
            throw std::runtime_error("module order differs at index " + std::to_string(i));
        }
        ConsensusGroup group;
        group.module = right.groups[i].module;
        group.cost = right.groups[i].cost > 0.0 ? right.groups[i].cost : left.groups[i].cost;
        group.param_count = right.groups[i].param_count ? right.groups[i].param_count : left.groups[i].param_count;
        group.weight_params = right.groups[i].weight_params ? right.groups[i].weight_params : left.groups[i].weight_params;
        group.positive_delta_nll = right.groups[i].positive_delta_nll;
        group.left_positive_delta_nll = left.groups[i].positive_delta_nll;
        group.right_positive_delta_nll = right.groups[i].positive_delta_nll;
        group.avg_positive_delta_nll = 0.5 * (group.left_positive_delta_nll + group.right_positive_delta_nll);
        group.consensus_score_delta_per_cost = group.avg_positive_delta_nll / std::max(group.cost, 1.0e-12);
        group.left_sensitivity_rank = left.groups[i].sensitivity_rank;
        group.right_sensitivity_rank = right.groups[i].sensitivity_rank;
        groups.push_back(group);
    }
    return groups;
}

std::vector<int> uniform_bits(std::size_t n, int base_bits) {
    return std::vector<int>(n, base_bits);
}

std::pair<std::vector<int>, Meta> build_consensus(
    const std::vector<ConsensusGroup>& groups,
    const std::vector<int>& left_bits,
    const std::vector<int>& right_bits,
    const Options& options
) {
    double total_cost = 0.0;
    for (const ConsensusGroup& group : groups) total_cost += group.cost;
    const double target_memory = options.budget_avg_bits * total_cost;
    std::vector<int> alloc(groups.size(), options.base_bits);
    double memory = options.base_bits * total_cost;
    std::vector<double> upgrade_costs(groups.size(), 0.0);
    for (std::size_t i = 0; i < groups.size(); ++i) {
        upgrade_costs[i] = (options.high_bits - options.base_bits) * groups[i].cost;
    }

    std::vector<int> intersection;
    for (std::size_t i = 0; i < groups.size(); ++i) {
        if (left_bits[i] == options.high_bits && right_bits[i] == options.high_bits) {
            intersection.push_back(static_cast<int>(i));
        }
    }
    auto score_order = [&](int a, int b) {
        const ConsensusGroup& ga = groups[static_cast<std::size_t>(a)];
        const ConsensusGroup& gb = groups[static_cast<std::size_t>(b)];
        if (ga.consensus_score_delta_per_cost != gb.consensus_score_delta_per_cost) {
            return ga.consensus_score_delta_per_cost > gb.consensus_score_delta_per_cost;
        }
        return ga.module < gb.module;
    };
    std::sort(intersection.begin(), intersection.end(), score_order);

    std::set<int> selected;
    Meta meta;
    meta.target_memory = target_memory;
    meta.intersection_candidates = static_cast<int>(intersection.size());
    for (int idx : intersection) {
        const double extra = upgrade_costs[static_cast<std::size_t>(idx)];
        if (memory + extra <= target_memory + 1.0e-6) {
            alloc[static_cast<std::size_t>(idx)] = options.high_bits;
            memory += extra;
            selected.insert(idx);
        } else {
            meta.skipped_intersection.push_back(groups[static_cast<std::size_t>(idx)].module);
        }
    }
    meta.intersection_selected = meta.intersection_candidates - static_cast<int>(meta.skipped_intersection.size());

    std::vector<int> candidates;
    for (std::size_t i = 0; i < groups.size(); ++i) {
        if (!selected.count(static_cast<int>(i))) candidates.push_back(static_cast<int>(i));
    }
    std::sort(candidates.begin(), candidates.end(), [&](int a, int b) {
        const ConsensusGroup& ga = groups[static_cast<std::size_t>(a)];
        const ConsensusGroup& gb = groups[static_cast<std::size_t>(b)];
        if (ga.consensus_score_delta_per_cost != gb.consensus_score_delta_per_cost) {
            return ga.consensus_score_delta_per_cost > gb.consensus_score_delta_per_cost;
        }
        if (ga.avg_positive_delta_nll != gb.avg_positive_delta_nll) {
            return ga.avg_positive_delta_nll > gb.avg_positive_delta_nll;
        }
        if (ga.cost != gb.cost) {
            return ga.cost < gb.cost;
        }
        return ga.module < gb.module;
    });
    for (int idx : candidates) {
        const double extra = upgrade_costs[static_cast<std::size_t>(idx)];
        if (memory + extra <= target_memory + 1.0e-6) {
            alloc[static_cast<std::size_t>(idx)] = options.high_bits;
            memory += extra;
            selected.insert(idx);
            meta.ranked_addition_modules.push_back(groups[static_cast<std::size_t>(idx)].module);
        }
    }
    meta.ranked_additions = static_cast<int>(meta.ranked_addition_modules.size());
    meta.actual_memory = memory;
    meta.budget_used = memory / std::max(target_memory, 1.0e-12);
    return {alloc, meta};
}

Summary summarize(
    const std::string& name,
    const std::vector<ConsensusGroup>& groups,
    const std::vector<int>& bits,
    const Options& options
) {
    Summary summary;
    summary.name = name;
    summary.groups = static_cast<int>(groups.size());
    summary.budget_avg_bits = options.budget_avg_bits;
    double total_cost = 0.0;
    for (std::size_t i = 0; i < groups.size(); ++i) {
        total_cost += groups[i].cost;
        summary.memory += groups[i].cost * bits[i];
        summary.positive_delta_nll_total += groups[i].positive_delta_nll;
        if (bits[i] > options.base_bits) {
            summary.positive_delta_nll_protected += groups[i].positive_delta_nll;
        }
    }
    summary.budget = options.budget_avg_bits * total_cost;
    summary.budget_used = summary.memory / std::max(summary.budget, 1.0e-12);
    summary.avg_bits = summary.memory / std::max(total_cost, 1.0e-12);
    summary.bit_hist = bit_hist(bits);
    summary.positive_delta_nll_protected_ratio =
        summary.positive_delta_nll_protected / std::max(summary.positive_delta_nll_total, 1.0e-12);
    return summary;
}

std::set<std::string> module_set(
    const std::vector<ConsensusGroup>& groups,
    const std::vector<int>& bits,
    int high_bits
) {
    std::set<std::string> out;
    for (std::size_t i = 0; i < groups.size(); ++i) {
        if (bits[i] == high_bits) out.insert(groups[i].module);
    }
    return out;
}

int intersection_size(const std::set<std::string>& a, const std::set<std::string>& b) {
    int count = 0;
    for (const std::string& value : a) {
        if (b.count(value)) ++count;
    }
    return count;
}

double jaccard(const std::set<std::string>& a, const std::set<std::string>& b) {
    std::set<std::string> merged = a;
    merged.insert(b.begin(), b.end());
    return static_cast<double>(intersection_size(a, b)) / std::max(static_cast<double>(merged.size()), 1.0);
}

std::string json_string_array(const std::vector<std::string>& values, int indent) {
    std::ostringstream out;
    out << "[";
    if (!values.empty()) out << "\n";
    const std::string pad(static_cast<std::size_t>(indent), ' ');
    for (std::size_t i = 0; i < values.size(); ++i) {
        out << pad << "\"" << json_escape(values[i]) << "\"" << (i + 1 == values.size() ? "\n" : ",\n");
    }
    if (!values.empty()) out << std::string(static_cast<std::size_t>(indent - 2), ' ');
    out << "]";
    return out.str();
}

std::string render_json(
    const Options& options,
    const Allocation& left,
    const Allocation& right,
    const std::vector<ConsensusGroup>& groups,
    const std::vector<int>& uniform,
    const std::vector<int>& consensus,
    const Summary& uniform_summary,
    const Summary& consensus_summary,
    const Meta& meta
) {
    const std::set<std::string> left_high = module_set(groups, left.bits, options.high_bits);
    const std::set<std::string> right_high = module_set(groups, right.bits, options.high_bits);
    const std::set<std::string> consensus_high = module_set(groups, consensus, options.high_bits);
    std::vector<int> selected_indices;
    for (std::size_t i = 0; i < groups.size(); ++i) {
        if (consensus[i] == options.high_bits) selected_indices.push_back(static_cast<int>(i));
    }
    std::sort(selected_indices.begin(), selected_indices.end(), [&](int a, int b) {
        const ConsensusGroup& ga = groups[static_cast<std::size_t>(a)];
        const ConsensusGroup& gb = groups[static_cast<std::size_t>(b)];
        if (ga.consensus_score_delta_per_cost != gb.consensus_score_delta_per_cost) {
            return ga.consensus_score_delta_per_cost > gb.consensus_score_delta_per_cost;
        }
        if (ga.avg_positive_delta_nll != gb.avg_positive_delta_nll) {
            return ga.avg_positive_delta_nll > gb.avg_positive_delta_nll;
        }
        return ga.module < gb.module;
    });
    if (static_cast<int>(selected_indices.size()) > options.selected_limit) {
        selected_indices.resize(static_cast<std::size_t>(options.selected_limit));
    }

    auto write_summary = [](std::ostringstream& out, const Summary& s, const std::string& suffix) {
        out << "      \"name\": \"" << json_escape(s.name) << "\",\n"
            << "      \"groups\": " << s.groups << ",\n"
            << "      \"budget_avg_bits\": " << s.budget_avg_bits << ",\n"
            << "      \"memory\": " << s.memory << ",\n"
            << "      \"budget\": " << s.budget << ",\n"
            << "      \"budget_used\": " << s.budget_used << ",\n"
            << "      \"avg_bits\": " << s.avg_bits << ",\n"
            << "      \"bit_hist\": " << bit_hist_json(s.bit_hist) << ",\n"
            << "      \"positive_delta_nll_total\": " << s.positive_delta_nll_total << ",\n"
            << "      \"positive_delta_nll_protected\": " << s.positive_delta_nll_protected << ",\n"
            << "      \"positive_delta_nll_protected_ratio\": " << s.positive_delta_nll_protected_ratio << "\n"
            << "    }" << suffix;
    };

    std::ostringstream out;
    out << std::setprecision(12);
    out << "{\n"
        << "  \"left_path\": \"" << json_escape(options.left_path) << "\",\n"
        << "  \"right_path\": \"" << json_escape(options.right_path) << "\",\n"
        << "  \"left_method\": \"" << json_escape(options.left_method) << "\",\n"
        << "  \"right_method\": \"" << json_escape(options.right_method) << "\",\n"
        << "  \"model\": \"" << json_escape(right.model.empty() ? left.model : right.model) << "\",\n"
        << "  \"base_bits\": " << options.base_bits << ",\n"
        << "  \"high_bits\": " << options.high_bits << ",\n"
        << "  \"budget_avg_bits\": " << options.budget_avg_bits << ",\n";

    out << "  \"groups\": [\n";
    for (std::size_t i = 0; i < groups.size(); ++i) {
        const ConsensusGroup& g = groups[i];
        out << "    {\n"
            << "      \"module\": \"" << json_escape(g.module) << "\",\n"
            << "      \"cost\": " << g.cost << ",\n"
            << "      \"param_count\": " << g.param_count << ",\n"
            << "      \"weight_params\": " << g.weight_params << ",\n"
            << "      \"positive_delta_nll\": " << g.positive_delta_nll << ",\n"
            << "      \"left_positive_delta_nll\": " << g.left_positive_delta_nll << ",\n"
            << "      \"right_positive_delta_nll\": " << g.right_positive_delta_nll << ",\n"
            << "      \"avg_positive_delta_nll\": " << g.avg_positive_delta_nll << ",\n"
            << "      \"consensus_score_delta_per_cost\": " << g.consensus_score_delta_per_cost << ",\n"
            << "      \"left_sensitivity_rank\": " << g.left_sensitivity_rank << ",\n"
            << "      \"right_sensitivity_rank\": " << g.right_sensitivity_rank << "\n"
            << "    }" << (i + 1 == groups.size() ? "\n" : ",\n");
    }
    out << "  ],\n";

    out << "  \"allocations\": {\n";
    out << "    \"uniform_int" << options.base_bits << "\": [";
    for (std::size_t i = 0; i < uniform.size(); ++i) {
        if (i) out << ", ";
        out << uniform[i];
    }
    out << "],\n";
    out << "    \"loss_sensitive_consensus_4to8\": [";
    for (std::size_t i = 0; i < consensus.size(); ++i) {
        if (i) out << ", ";
        out << consensus[i];
    }
    out << "]\n  },\n";

    out << "  \"summaries\": [\n    {\n";
    write_summary(out, uniform_summary, ",\n");
    out << "    {\n";
    write_summary(out, consensus_summary, "\n");
    out << "  ],\n";

    out << "  \"consensus_meta\": {\n"
        << "    \"target_memory\": " << meta.target_memory << ",\n"
        << "    \"actual_memory\": " << meta.actual_memory << ",\n"
        << "    \"budget_used\": " << meta.budget_used << ",\n"
        << "    \"intersection_candidates\": " << meta.intersection_candidates << ",\n"
        << "    \"intersection_selected\": " << meta.intersection_selected << ",\n"
        << "    \"skipped_intersection\": " << json_string_array(meta.skipped_intersection, 6) << ",\n"
        << "    \"ranked_additions\": " << meta.ranked_additions << ",\n"
        << "    \"ranked_addition_modules\": " << json_string_array(meta.ranked_addition_modules, 6) << "\n"
        << "  },\n";

    out << "  \"overlap\": {\n"
        << "    \"left_high_count\": " << left_high.size() << ",\n"
        << "    \"right_high_count\": " << right_high.size() << ",\n"
        << "    \"consensus_high_count\": " << consensus_high.size() << ",\n"
        << "    \"left_high_overlap\": " << intersection_size(left_high, consensus_high) << ",\n"
        << "    \"right_high_overlap\": " << intersection_size(right_high, consensus_high) << ",\n"
        << "    \"left_high_jaccard\": " << jaccard(left_high, consensus_high) << ",\n"
        << "    \"right_high_jaccard\": " << jaccard(right_high, consensus_high) << "\n"
        << "  },\n";

    out << "  \"selected_modules\": [\n";
    for (std::size_t k = 0; k < selected_indices.size(); ++k) {
        const ConsensusGroup& g = groups[static_cast<std::size_t>(selected_indices[k])];
        out << "    {\n"
            << "      \"module\": \"" << json_escape(g.module) << "\",\n"
            << "      \"param_count\": " << (g.param_count ? g.param_count : g.weight_params) << ",\n"
            << "      \"avg_positive_delta_nll\": " << g.avg_positive_delta_nll << ",\n"
            << "      \"left_positive_delta_nll\": " << g.left_positive_delta_nll << ",\n"
            << "      \"right_positive_delta_nll\": " << g.right_positive_delta_nll << ",\n"
            << "      \"consensus_score_delta_per_cost\": " << g.consensus_score_delta_per_cost << ",\n"
            << "      \"left_rank\": " << g.left_sensitivity_rank << ",\n"
            << "      \"right_rank\": " << g.right_sensitivity_rank << "\n"
            << "    }" << (k + 1 == selected_indices.size() ? "\n" : ",\n");
    }
    out << "  ]\n}\n";
    return out.str();
}

std::string render_markdown(
    const Options& options,
    const Summary& consensus_summary,
    const Meta& meta,
    const std::vector<ConsensusGroup>& groups,
    const std::vector<int>& consensus
) {
    std::vector<int> selected;
    for (std::size_t i = 0; i < groups.size(); ++i) {
        if (consensus[i] == options.high_bits) selected.push_back(static_cast<int>(i));
    }
    std::sort(selected.begin(), selected.end(), [&](int a, int b) {
        const ConsensusGroup& ga = groups[static_cast<std::size_t>(a)];
        const ConsensusGroup& gb = groups[static_cast<std::size_t>(b)];
        if (ga.consensus_score_delta_per_cost != gb.consensus_score_delta_per_cost) {
            return ga.consensus_score_delta_per_cost > gb.consensus_score_delta_per_cost;
        }
        if (ga.avg_positive_delta_nll != gb.avg_positive_delta_nll) {
            return ga.avg_positive_delta_nll > gb.avg_positive_delta_nll;
        }
        return ga.module < gb.module;
    });
    if (static_cast<int>(selected.size()) > options.selected_limit) {
        selected.resize(static_cast<std::size_t>(options.selected_limit));
    }

    std::ostringstream out;
    out << "# Consensus Loss-Sensitive Allocation\n\n";
    out << "Left allocation: `" << options.left_path << "`\n";
    out << "Right allocation: `" << options.right_path << "`\n\n";
    out << "## Summary\n\n";
    out << "| metric | value |\n|---|---:|\n";
    out << "| modules | " << consensus_summary.groups << " |\n";
    out << "| average bits | " << std::fixed << std::setprecision(4) << consensus_summary.avg_bits << " |\n";
    out << "| budget used | " << consensus_summary.budget_used << " |\n";
    out << "| bit histogram | " << bit_hist_json(consensus_summary.bit_hist) << " |\n";
    out << "| locked intersection modules | " << meta.intersection_selected << " |\n";
    out << "| ranked additions | " << meta.ranked_additions << " |\n\n";
    out << "## Top Consensus 8-bit Modules\n\n";
    out << "| module | params | avg delta NLL | left delta | right delta | score/cost | left rank | right rank |\n";
    out << "|---|---:|---:|---:|---:|---:|---:|---:|\n";
    for (int idx : selected) {
        const ConsensusGroup& g = groups[static_cast<std::size_t>(idx)];
        out << "| `" << g.module << "` | " << (g.param_count ? g.param_count : g.weight_params)
            << " | " << std::fixed << std::setprecision(6) << g.avg_positive_delta_nll
            << " | " << g.left_positive_delta_nll
            << " | " << g.right_positive_delta_nll
            << " | " << std::scientific << std::setprecision(3) << g.consensus_score_delta_per_cost
            << std::fixed << " | " << g.left_sensitivity_rank << " | " << g.right_sensitivity_rank << " |\n";
    }
    out << "\n## Interpretation\n\n";
    out << "This allocation is a stability-oriented policy: it prioritizes modules that\n";
    out << "both calibration probes selected, then fills unused budget by average\n";
    out << "loss-per-cost score. It should be read together with downstream PPL\n";
    out << "evaluation because stable allocation decisions can still trade off quality.\n";
    return out.str();
}

Options parse_args(int argc, char** argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        auto require_value = [&](const char* name) -> std::string {
            if (i + 1 >= argc) throw std::runtime_error(std::string("missing value for ") + name);
            return argv[++i];
        };
        if (arg == "--left") {
            options.left_path = require_value("--left");
        } else if (arg == "--right") {
            options.right_path = require_value("--right");
        } else if (arg == "--left-method") {
            options.left_method = require_value("--left-method");
        } else if (arg == "--right-method") {
            options.right_method = require_value("--right-method");
        } else if (arg == "--base-bits") {
            options.base_bits = std::stoi(require_value("--base-bits"));
        } else if (arg == "--high-bits") {
            options.high_bits = std::stoi(require_value("--high-bits"));
        } else if (arg == "--budget-avg-bits") {
            options.budget_avg_bits = std::stod(require_value("--budget-avg-bits"));
        } else if (arg == "--selected-limit") {
            options.selected_limit = std::stoi(require_value("--selected-limit"));
        } else if (arg == "--out-json") {
            options.out_json = require_value("--out-json");
        } else if (arg == "--out-md") {
            options.out_md = require_value("--out-md");
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--no-write") {
            options.no_write = true;
        } else if (arg == "--help" || arg == "-h") {
            std::cout
                << "Usage: quant_consensus_builder --left left.json --right right.json\n"
                << "                               [--left-method loss_sensitive_4to8]\n"
                << "                               [--right-method loss_sensitive_4to8]\n"
                << "                               [--budget-avg-bits 4.5]\n"
                << "                               [--out-json path] [--out-md path]\n"
                << "                               [--emit json|markdown] [--no-write]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.left_path.empty() || options.right_path.empty()) {
        throw std::runtime_error("--left and --right are required");
    }
    if (options.high_bits <= options.base_bits) {
        throw std::runtime_error("--high-bits must be greater than --base-bits");
    }
    return options;
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        const Allocation left = read_allocation(options.left_path, options.left_method);
        const Allocation right = read_allocation(options.right_path, options.right_method);
        const std::vector<ConsensusGroup> groups = make_consensus_groups(left, right);
        const std::vector<int> uniform = uniform_bits(groups.size(), options.base_bits);
        const auto built = build_consensus(groups, left.bits, right.bits, options);
        const std::vector<int>& consensus = built.first;
        const Meta& meta = built.second;
        const Summary uniform_summary = summarize("uniform_int" + std::to_string(options.base_bits), groups, uniform, options);
        const Summary consensus_summary = summarize("loss_sensitive_consensus_4to8", groups, consensus, options);
        const std::string json = render_json(options, left, right, groups, uniform, consensus, uniform_summary, consensus_summary, meta);
        const std::string markdown = render_markdown(options, consensus_summary, meta, groups, consensus);

        if (!options.no_write) {
            write_text_file(options.out_json, json);
            write_text_file(options.out_md, markdown);
        }

        if (options.emit == "json") {
            std::cout << json;
        } else if (options.emit == "markdown" || options.emit == "md") {
            std::cout << markdown;
        } else if (!options.emit.empty()) {
            throw std::runtime_error("unknown emit format: " + options.emit);
        } else {
            std::cout << "{\n"
                      << "  \"out_json\": \"" << json_escape(options.out_json) << "\",\n"
                      << "  \"out_md\": \"" << json_escape(options.out_md) << "\",\n"
                      << "  \"avg_bits\": " << consensus_summary.avg_bits << ",\n"
                      << "  \"budget_used\": " << consensus_summary.budget_used << "\n"
                      << "}\n";
        }
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << "\n";
        return 1;
    }
    return 0;
}
