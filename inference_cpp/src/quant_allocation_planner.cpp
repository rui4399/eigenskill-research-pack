#include <algorithm>
#include <cctype>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {

struct Group {
    std::string module;
    double cost = 0.0;
    double positive_delta_nll = 0.0;
    std::string category;
};

struct Options {
    std::string input_csv;
    std::string sensitivity_json;
    int low_bits = 4;
    int high_bits = 8;
    double budget_avg_bits = 4.5;
    std::uint32_t seed = 20260604;
    std::string emit = "json";
};

struct Summary {
    std::string name;
    std::vector<int> bits;
    double memory = 0.0;
    double budget = 0.0;
    double budget_used = 0.0;
    double avg_bits = 0.0;
    double positive_total = 0.0;
    double positive_protected = 0.0;
    double protected_ratio = 0.0;
    double expected_unprotected_delta = 0.0;
};

std::string trim(std::string value) {
    auto not_space = [](unsigned char ch) { return !std::isspace(ch); };
    value.erase(value.begin(), std::find_if(value.begin(), value.end(), not_space));
    value.erase(std::find_if(value.rbegin(), value.rend(), not_space).base(), value.end());
    return value;
}

std::vector<std::string> split_csv_line(const std::string& line) {
    std::vector<std::string> fields;
    std::string field;
    bool quoted = false;
    for (char ch : line) {
        if (ch == '"') {
            quoted = !quoted;
        } else if (ch == ',' && !quoted) {
            fields.push_back(trim(field));
            field.clear();
        } else {
            field.push_back(ch);
        }
    }
    fields.push_back(trim(field));
    return fields;
}

std::string read_text_file(const std::string& path) {
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("could not open file: " + path);
    }
    std::ostringstream ss;
    ss << in.rdbuf();
    return ss.str();
}

int index_of(const std::vector<std::string>& header, const std::string& name) {
    for (std::size_t i = 0; i < header.size(); ++i) {
        if (header[i] == name) {
            return static_cast<int>(i);
        }
    }
    return -1;
}

std::vector<Group> read_groups_csv(const std::string& path) {
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("could not open input csv: " + path);
    }

    std::string line;
    if (!std::getline(in, line)) {
        throw std::runtime_error("empty input csv: " + path);
    }
    const std::vector<std::string> header = split_csv_line(line);
    const int module_idx = index_of(header, "module");
    const int cost_idx = index_of(header, "cost");
    const int delta_idx = index_of(header, "positive_delta_nll");
    const int category_idx = index_of(header, "category");
    if (module_idx < 0 || cost_idx < 0 || delta_idx < 0) {
        throw std::runtime_error("csv must contain module,cost,positive_delta_nll columns");
    }

    std::vector<Group> groups;
    int line_no = 1;
    while (std::getline(in, line)) {
        ++line_no;
        if (trim(line).empty()) {
            continue;
        }
        const std::vector<std::string> fields = split_csv_line(line);
        const int required = std::max({module_idx, cost_idx, delta_idx, category_idx});
        if (static_cast<int>(fields.size()) <= required) {
            throw std::runtime_error("csv row has too few fields at line " + std::to_string(line_no));
        }
        Group group;
        group.module = fields[static_cast<std::size_t>(module_idx)];
        group.cost = std::stod(fields[static_cast<std::size_t>(cost_idx)]);
        group.positive_delta_nll = std::max(0.0, std::stod(fields[static_cast<std::size_t>(delta_idx)]));
        if (category_idx >= 0) {
            group.category = fields[static_cast<std::size_t>(category_idx)];
        }
        if (group.module.empty() || group.cost <= 0.0 || !std::isfinite(group.cost) ||
            !std::isfinite(group.positive_delta_nll)) {
            throw std::runtime_error("invalid row at line " + std::to_string(line_no));
        }
        groups.push_back(group);
    }
    if (groups.empty()) {
        throw std::runtime_error("input csv contains no groups");
    }
    return groups;
}

std::string infer_category(const std::string& module) {
    if (module == "lm_head") return "lm_head";
    if (module.find(".self_attn.q_proj") != std::string::npos) return "attn.q_proj";
    if (module.find(".self_attn.k_proj") != std::string::npos) return "attn.k_proj";
    if (module.find(".self_attn.v_proj") != std::string::npos) return "attn.v_proj";
    if (module.find(".self_attn.o_proj") != std::string::npos) return "attn.o_proj";
    if (module.find(".mlp.gate_proj") != std::string::npos) return "mlp.gate_proj";
    if (module.find(".mlp.up_proj") != std::string::npos) return "mlp.up_proj";
    if (module.find(".mlp.down_proj") != std::string::npos) return "mlp.down_proj";
    return "other";
}

std::size_t find_json_key(const std::string& text, const std::string& key, std::size_t start = 0) {
    return text.find("\"" + key + "\"", start);
}

std::size_t skip_ws(const std::string& text, std::size_t pos) {
    while (pos < text.size() && std::isspace(static_cast<unsigned char>(text[pos]))) {
        ++pos;
    }
    return pos;
}

std::string json_string_value(const std::string& object, const std::string& key) {
    std::size_t pos = find_json_key(object, key);
    if (pos == std::string::npos) {
        return "";
    }
    pos = object.find(':', pos);
    if (pos == std::string::npos) {
        return "";
    }
    pos = skip_ws(object, pos + 1);
    if (pos >= object.size() || object[pos] != '"') {
        return "";
    }
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
    if (pos == std::string::npos) {
        return fallback;
    }
    pos = object.find(':', pos);
    if (pos == std::string::npos) {
        return fallback;
    }
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
    if (pos == start) {
        return fallback;
    }
    return std::stod(object.substr(start, pos - start));
}

std::vector<std::string> extract_groups_objects(const std::string& text) {
    std::size_t pos = find_json_key(text, "groups");
    if (pos == std::string::npos) {
        throw std::runtime_error("json missing groups array");
    }
    pos = text.find('[', pos);
    if (pos == std::string::npos) {
        throw std::runtime_error("json groups field is not an array");
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
            if (bracket_depth == 0) {
                break;
            }
            continue;
        }
        if (ch == '{') {
            if (object_depth == 0 && bracket_depth == 1) {
                object_start = pos;
            }
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
        throw std::runtime_error("json groups array contains no objects");
    }
    return objects;
}

std::vector<Group> read_groups_sensitivity_json(const std::string& path) {
    const std::string text = read_text_file(path);
    const std::vector<std::string> objects = extract_groups_objects(text);
    std::vector<Group> groups;
    groups.reserve(objects.size());
    for (const std::string& object : objects) {
        Group group;
        group.module = json_string_value(object, "module");
        group.cost = json_number_value(object, "cost", json_number_value(object, "param_count", 0.0));
        group.positive_delta_nll = std::max(0.0, json_number_value(object, "positive_delta_nll", 0.0));
        group.category = json_string_value(object, "category");
        if (group.category.empty()) {
            group.category = infer_category(group.module);
        }
        if (group.module.empty() || group.cost <= 0.0 || !std::isfinite(group.cost) ||
            !std::isfinite(group.positive_delta_nll)) {
            throw std::runtime_error("invalid group object in json: missing module/cost/delta");
        }
        groups.push_back(group);
    }
    return groups;
}

Options parse_args(int argc, char** argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        auto require_value = [&](const char* name) -> std::string {
            if (i + 1 >= argc) {
                throw std::runtime_error(std::string("missing value for ") + name);
            }
            return argv[++i];
        };
        if (arg == "--csv") {
            options.input_csv = require_value("--csv");
        } else if (arg == "--sensitivity-json") {
            options.sensitivity_json = require_value("--sensitivity-json");
        } else if (arg == "--low-bits") {
            options.low_bits = std::stoi(require_value("--low-bits"));
        } else if (arg == "--high-bits") {
            options.high_bits = std::stoi(require_value("--high-bits"));
        } else if (arg == "--budget-avg-bits") {
            options.budget_avg_bits = std::stod(require_value("--budget-avg-bits"));
        } else if (arg == "--seed") {
            options.seed = static_cast<std::uint32_t>(std::stoul(require_value("--seed")));
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_allocation_planner (--csv groups.csv | --sensitivity-json summary.json)\n"
                         "                                [--low-bits 4] [--high-bits 8]\n"
                         "                                [--budget-avg-bits 4.5] [--seed 20260604]\n"
                         "                                [--emit json|csv]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.input_csv.empty() == options.sensitivity_json.empty()) {
        throw std::runtime_error("provide exactly one of --csv or --sensitivity-json");
    }
    if (options.low_bits < 1 || options.high_bits <= options.low_bits || options.high_bits > 16) {
        throw std::runtime_error("invalid bit range");
    }
    if (options.budget_avg_bits < options.low_bits || options.budget_avg_bits > options.high_bits) {
        throw std::runtime_error("--budget-avg-bits must be within [low_bits, high_bits]");
    }
    if (options.emit != "json" && options.emit != "csv") {
        throw std::runtime_error("--emit must be json or csv");
    }
    return options;
}

double total_cost(const std::vector<Group>& groups) {
    double total = 0.0;
    for (const Group& group : groups) {
        total += group.cost;
    }
    return total;
}

double total_positive_delta(const std::vector<Group>& groups) {
    double total = 0.0;
    for (const Group& group : groups) {
        total += group.positive_delta_nll;
    }
    return total;
}

double category_score(const Group& group) {
    double score = 0.0;
    if (group.category == "attn.k_proj" || group.category == "attn.v_proj") {
        score += 100.0;
    } else if (group.category == "attn.q_proj" || group.category == "attn.o_proj") {
        score += 50.0;
    } else if (group.category == "mlp.down_proj") {
        score += 20.0;
    } else if (group.category == "lm_head") {
        score -= 100.0;
    }
    const std::string marker = "model.layers.";
    const std::size_t pos = group.module.find(marker);
    if (pos != std::string::npos) {
        const std::size_t start = pos + marker.size();
        const std::size_t end = group.module.find('.', start);
        if (end != std::string::npos) {
            try {
                const int layer = std::stoi(group.module.substr(start, end - start));
                score += std::max(0, 128 - layer) / 128.0;
            } catch (const std::exception&) {
            }
        }
    }
    return score;
}

std::vector<int> allocate_budgeted(const std::vector<Group>& groups,
                                   const Options& options,
                                   const std::vector<int>& ordered_indices) {
    const double budget = options.budget_avg_bits * total_cost(groups);
    const double low_memory = options.low_bits * total_cost(groups);
    double remaining = std::max(0.0, budget - low_memory);
    std::vector<int> bits(groups.size(), options.low_bits);
    std::vector<char> selected(groups.size(), 0);

    for (int idx : ordered_indices) {
        if (idx < 0 || idx >= static_cast<int>(groups.size())) {
            throw std::runtime_error("internal invalid group index");
        }
        const double extra = groups[static_cast<std::size_t>(idx)].cost * (options.high_bits - options.low_bits);
        if (extra <= remaining + 1.0e-9 &&
            groups[static_cast<std::size_t>(idx)].positive_delta_nll > 0.0) {
            bits[static_cast<std::size_t>(idx)] = options.high_bits;
            selected[static_cast<std::size_t>(idx)] = 1;
            remaining -= extra;
        }
    }

    std::vector<std::pair<double, int>> small_first;
    for (std::size_t idx = 0; idx < groups.size(); ++idx) {
        small_first.push_back({groups[idx].cost, static_cast<int>(idx)});
    }
    std::sort(small_first.begin(), small_first.end());
    for (const auto& [cost, idx] : small_first) {
        (void)cost;
        if (selected[static_cast<std::size_t>(idx)] ||
            groups[static_cast<std::size_t>(idx)].positive_delta_nll <= 0.0) {
            continue;
        }
        const double extra = groups[static_cast<std::size_t>(idx)].cost * (options.high_bits - options.low_bits);
        if (extra <= remaining + 1.0e-9) {
            bits[static_cast<std::size_t>(idx)] = options.high_bits;
            selected[static_cast<std::size_t>(idx)] = 1;
            remaining -= extra;
        }
    }
    return bits;
}

std::vector<int> sensitivity_order(const std::vector<Group>& groups, const Options& options) {
    std::vector<int> order(groups.size());
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int lhs, int rhs) {
        const Group& a = groups[static_cast<std::size_t>(lhs)];
        const Group& b = groups[static_cast<std::size_t>(rhs)];
        const double a_extra = a.cost * (options.high_bits - options.low_bits);
        const double b_extra = b.cost * (options.high_bits - options.low_bits);
        const double a_score = a.positive_delta_nll / std::max(a_extra, 1.0e-12);
        const double b_score = b.positive_delta_nll / std::max(b_extra, 1.0e-12);
        if (a_score != b_score) return a_score > b_score;
        if (a.positive_delta_nll != b.positive_delta_nll) return a.positive_delta_nll > b.positive_delta_nll;
        return a.module < b.module;
    });
    return order;
}

std::vector<int> category_order(const std::vector<Group>& groups) {
    std::vector<int> order(groups.size());
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int lhs, int rhs) {
        const Group& a = groups[static_cast<std::size_t>(lhs)];
        const Group& b = groups[static_cast<std::size_t>(rhs)];
        const double a_score = category_score(a);
        const double b_score = category_score(b);
        if (a_score != b_score) return a_score > b_score;
        if (a.positive_delta_nll != b.positive_delta_nll) return a.positive_delta_nll > b.positive_delta_nll;
        return a.module < b.module;
    });
    return order;
}

std::vector<int> random_order(std::size_t n, std::uint32_t seed) {
    std::vector<int> order(n);
    std::iota(order.begin(), order.end(), 0);
    std::mt19937 rng(seed);
    std::shuffle(order.begin(), order.end(), rng);
    return order;
}

Summary summarize(const std::string& name,
                  const std::vector<Group>& groups,
                  const Options& options,
                  std::vector<int> bits) {
    Summary summary;
    summary.name = name;
    summary.bits = std::move(bits);
    summary.budget = options.budget_avg_bits * total_cost(groups);
    summary.positive_total = total_positive_delta(groups);
    for (std::size_t idx = 0; idx < groups.size(); ++idx) {
        summary.memory += groups[idx].cost * summary.bits[idx];
        if (summary.bits[idx] > options.low_bits) {
            summary.positive_protected += groups[idx].positive_delta_nll;
        } else {
            summary.expected_unprotected_delta += groups[idx].positive_delta_nll;
        }
    }
    summary.budget_used = summary.memory / std::max(summary.budget, 1.0e-12);
    summary.avg_bits = summary.memory / std::max(total_cost(groups), 1.0e-12);
    summary.protected_ratio = summary.positive_protected / std::max(summary.positive_total, 1.0e-12);
    return summary;
}

void print_bit_hist(std::ostream& out, const std::vector<int>& bits) {
    std::vector<int> values = bits;
    std::sort(values.begin(), values.end());
    out << "{";
    bool first = true;
    for (std::size_t i = 0; i < values.size();) {
        const int bit = values[i];
        std::size_t j = i;
        while (j < values.size() && values[j] == bit) {
            ++j;
        }
        if (!first) out << ",";
        first = false;
        out << "\"" << bit << "\":" << (j - i);
        i = j;
    }
    out << "}";
}

void print_bits_json(std::ostream& out, const std::vector<int>& bits) {
    out << "[";
    for (std::size_t i = 0; i < bits.size(); ++i) {
        if (i > 0) out << ",";
        out << bits[i];
    }
    out << "]";
}

std::string json_escape(const std::string& text) {
    std::string out;
    for (char ch : text) {
        switch (ch) {
            case '\\':
                out += "\\\\";
                break;
            case '"':
                out += "\\\"";
                break;
            case '\n':
                out += "\\n";
                break;
            case '\r':
                out += "\\r";
                break;
            case '\t':
                out += "\\t";
                break;
            default:
                out.push_back(ch);
                break;
        }
    }
    return out;
}

void print_groups_json(std::ostream& out, const std::vector<Group>& groups) {
    out << "[\n";
    for (std::size_t i = 0; i < groups.size(); ++i) {
        const Group& g = groups[i];
        out << "    {\"module\":\"" << json_escape(g.module) << "\","
            << "\"cost\":" << g.cost << ","
            << "\"positive_delta_nll\":" << g.positive_delta_nll << ","
            << "\"category\":\"" << json_escape(g.category) << "\"}";
        out << (i + 1 == groups.size() ? "\n" : ",\n");
    }
    out << "  ]";
}

void print_allocations_json(std::ostream& out, const std::vector<Summary>& summaries) {
    out << "{\n";
    for (std::size_t i = 0; i < summaries.size(); ++i) {
        const Summary& s = summaries[i];
        out << "    \"" << json_escape(s.name) << "\": ";
        print_bits_json(out, s.bits);
        out << (i + 1 == summaries.size() ? "\n" : ",\n");
    }
    out << "  }";
}

void print_json(const std::vector<Group>& groups, const Options& options, const std::vector<Summary>& summaries) {
    std::cout << std::fixed << std::setprecision(6);
    std::cout << "{\n";
    std::cout << "  \"group_count\": " << groups.size() << ",\n";
    std::cout << "  \"low_bits\": " << options.low_bits << ",\n";
    std::cout << "  \"high_bits\": " << options.high_bits << ",\n";
    std::cout << "  \"budget_avg_bits\": " << options.budget_avg_bits << ",\n";
    std::cout << "  \"budget_memory\": " << options.budget_avg_bits * total_cost(groups) << ",\n";
    std::cout << "  \"total_cost\": " << total_cost(groups) << ",\n";
    std::cout << "  \"groups\": ";
    print_groups_json(std::cout, groups);
    std::cout << ",\n";
    std::cout << "  \"allocations\": ";
    print_allocations_json(std::cout, summaries);
    std::cout << ",\n";
    std::cout << "  \"summaries\": [\n";
    for (std::size_t i = 0; i < summaries.size(); ++i) {
        const Summary& s = summaries[i];
        std::cout << "    {\n";
        std::cout << "      \"name\": \"" << s.name << "\",\n";
        std::cout << "      \"memory\": " << s.memory << ",\n";
        std::cout << "      \"budget_used\": " << s.budget_used << ",\n";
        std::cout << "      \"avg_bits\": " << s.avg_bits << ",\n";
        std::cout << "      \"positive_delta_nll_total\": " << s.positive_total << ",\n";
        std::cout << "      \"positive_delta_nll_protected\": " << s.positive_protected << ",\n";
        std::cout << "      \"positive_delta_nll_protected_ratio\": " << s.protected_ratio << ",\n";
        std::cout << "      \"expected_unprotected_delta_nll\": " << s.expected_unprotected_delta << ",\n";
        std::cout << "      \"bit_hist\": ";
        print_bit_hist(std::cout, s.bits);
        std::cout << ",\n";
        std::cout << "      \"bits\": ";
        print_bits_json(std::cout, s.bits);
        std::cout << "\n";
        std::cout << "    }" << (i + 1 == summaries.size() ? "\n" : ",\n");
    }
    std::cout << "  ]\n";
    std::cout << "}\n";
}

void print_csv(const std::vector<Summary>& summaries) {
    std::cout << "name,memory,budget_used,avg_bits,protected_ratio,expected_unprotected_delta_nll,bit_hist\n";
    std::cout << std::fixed << std::setprecision(6);
    for (const Summary& s : summaries) {
        std::cout << s.name << "," << s.memory << "," << s.budget_used << "," << s.avg_bits << ","
                  << s.protected_ratio << "," << s.expected_unprotected_delta << ",";
        print_bit_hist(std::cout, s.bits);
        std::cout << "\n";
    }
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        const std::vector<Group> groups = options.input_csv.empty()
                                              ? read_groups_sensitivity_json(options.sensitivity_json)
                                              : read_groups_csv(options.input_csv);
        std::vector<Summary> summaries;
        summaries.push_back(summarize(
            "loss_sensitive_budget",
            groups,
            options,
            allocate_budgeted(groups, options, sensitivity_order(groups, options))));
        summaries.push_back(summarize(
            "random_budget",
            groups,
            options,
            allocate_budgeted(groups, options, random_order(groups.size(), options.seed))));
        summaries.push_back(summarize(
            "category_budget",
            groups,
            options,
            allocate_budgeted(groups, options, category_order(groups))));

        if (options.emit == "json") {
            print_json(groups, options, summaries);
        } else {
            print_csv(summaries);
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
