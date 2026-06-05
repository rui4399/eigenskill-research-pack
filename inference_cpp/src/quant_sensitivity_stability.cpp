#include <algorithm>
#include <cctype>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Options {
    std::string left_json;
    std::string right_json;
    std::string left_name = "left";
    std::string right_name = "right";
    std::vector<int> top_ks = {10, 20, 40};
    double epsilon = 1.0e-12;
    std::string emit = "markdown";
};

struct Group {
    std::string module;
    double positive_delta_nll = 0.0;
    double signed_delta_nll = 0.0;
    double cost = 1.0;
};

struct TopOverlap {
    int k = 0;
    int left_count = 0;
    int right_count = 0;
    int overlap = 0;
    int uni = 0;
    double jaccard = 0.0;
    double instability = 0.0;
};

struct InstabilitySummary {
    double positive_set_instability = 0.0;
    double sign_instability = 0.0;
    double score_rank_instability = 0.0;
    double mean_topk_jaccard = 0.0;
    double topk_instability = 0.0;
    double csi = 0.0;
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

std::size_t skip_ws(const std::string& text, std::size_t pos) {
    while (pos < text.size() && std::isspace(static_cast<unsigned char>(text[pos]))) {
        ++pos;
    }
    return pos;
}

std::size_t find_json_key(const std::string& text, const std::string& key, std::size_t start = 0) {
    return text.find("\"" + key + "\"", start);
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
        } else if (ch == '[') {
            ++bracket_depth;
        } else if (ch == ']') {
            --bracket_depth;
            if (bracket_depth == 0) break;
        } else if (ch == '{') {
            if (object_depth == 0 && bracket_depth == 1) object_start = pos;
            ++object_depth;
        } else if (ch == '}') {
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

std::vector<Group> read_groups(const std::string& path) {
    const std::string text = read_text_file(path);
    const std::vector<std::string> objects = extract_array_objects(text, "groups");
    std::vector<Group> groups;
    groups.reserve(objects.size());
    for (std::size_t i = 0; i < objects.size(); ++i) {
        Group group;
        group.module = json_string_value(objects[i], "module");
        if (group.module.empty()) {
            throw std::runtime_error(path + ": group missing module at index " + std::to_string(i));
        }
        group.positive_delta_nll = std::max(json_number_value(objects[i], "positive_delta_nll", 0.0), 0.0);
        group.signed_delta_nll = json_number_value(objects[i], "delta_nll", group.positive_delta_nll);
        group.cost = std::max(json_number_value(objects[i], "cost", json_number_value(objects[i], "param_count", 1.0)), 1.0e-12);
        groups.push_back(group);
    }
    std::sort(groups.begin(), groups.end(), [](const Group& a, const Group& b) { return a.module < b.module; });
    return groups;
}

void align_groups(const std::vector<Group>& left, const std::vector<Group>& right, std::vector<Group>& left_out,
                  std::vector<Group>& right_out) {
    std::size_t i = 0;
    std::size_t j = 0;
    while (i < left.size() && j < right.size()) {
        if (left[i].module == right[j].module) {
            left_out.push_back(left[i]);
            right_out.push_back(right[j]);
            ++i;
            ++j;
        } else if (left[i].module < right[j].module) {
            ++i;
        } else {
            ++j;
        }
    }
    if (left_out.empty()) {
        throw std::runtime_error("no shared modules");
    }
}

double pearson(const std::vector<double>& xs, const std::vector<double>& ys) {
    if (xs.size() != ys.size() || xs.empty()) return std::numeric_limits<double>::quiet_NaN();
    double mean_x = 0.0;
    double mean_y = 0.0;
    for (std::size_t i = 0; i < xs.size(); ++i) {
        mean_x += xs[i];
        mean_y += ys[i];
    }
    mean_x /= static_cast<double>(xs.size());
    mean_y /= static_cast<double>(ys.size());
    double num = 0.0;
    double den_x = 0.0;
    double den_y = 0.0;
    for (std::size_t i = 0; i < xs.size(); ++i) {
        const double dx = xs[i] - mean_x;
        const double dy = ys[i] - mean_y;
        num += dx * dy;
        den_x += dx * dx;
        den_y += dy * dy;
    }
    if (den_x <= 0.0 || den_y <= 0.0) return std::numeric_limits<double>::quiet_NaN();
    return num / std::sqrt(den_x * den_y);
}

std::vector<double> average_ranks(const std::vector<double>& values, bool descending) {
    std::vector<std::pair<int, double>> indexed;
    indexed.reserve(values.size());
    for (std::size_t i = 0; i < values.size(); ++i) {
        indexed.push_back({static_cast<int>(i), values[i]});
    }
    std::sort(indexed.begin(), indexed.end(), [descending](const auto& a, const auto& b) {
        if (a.second == b.second) return a.first < b.first;
        return descending ? a.second > b.second : a.second < b.second;
    });
    std::vector<double> ranks(values.size(), 0.0);
    std::size_t pos = 0;
    while (pos < indexed.size()) {
        std::size_t end = pos + 1;
        while (end < indexed.size() && indexed[end].second == indexed[pos].second) {
            ++end;
        }
        const double avg_rank = 0.5 * (static_cast<double>(pos + 1) + static_cast<double>(end));
        for (std::size_t idx = pos; idx < end; ++idx) {
            ranks[static_cast<std::size_t>(indexed[idx].first)] = avg_rank;
        }
        pos = end;
    }
    return ranks;
}

double spearman(const std::vector<double>& xs, const std::vector<double>& ys) {
    return pearson(average_ranks(xs, true), average_ranks(ys, true));
}

double kendall_tau_a(const std::vector<double>& xs, const std::vector<double>& ys) {
    int concordant = 0;
    int discordant = 0;
    for (std::size_t i = 0; i < xs.size(); ++i) {
        for (std::size_t j = i + 1; j < xs.size(); ++j) {
            const double prod = (xs[i] - xs[j]) * (ys[i] - ys[j]);
            if (prod > 0.0) {
                ++concordant;
            } else if (prod < 0.0) {
                ++discordant;
            }
        }
    }
    const int total = concordant + discordant;
    if (total == 0) return std::numeric_limits<double>::quiet_NaN();
    return static_cast<double>(concordant - discordant) / static_cast<double>(total);
}

std::string sign_bucket(double value, double epsilon) {
    if (value > epsilon) return "positive";
    if (value < -epsilon) return "negative";
    return "near_zero";
}

std::set<std::string> top_modules(const std::vector<Group>& groups, const std::vector<double>& scores, int k) {
    std::vector<std::pair<std::string, double>> pairs;
    pairs.reserve(groups.size());
    for (std::size_t i = 0; i < groups.size(); ++i) {
        pairs.push_back({groups[i].module, scores[i]});
    }
    std::sort(pairs.begin(), pairs.end(), [](const auto& a, const auto& b) {
        if (a.second == b.second) return a.first > b.first;
        return a.second > b.second;
    });
    std::set<std::string> out;
    const int limit = std::min(k, static_cast<int>(pairs.size()));
    for (int i = 0; i < limit; ++i) {
        out.insert(pairs[static_cast<std::size_t>(i)].first);
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

int union_size(const std::set<std::string>& a, const std::set<std::string>& b) {
    std::set<std::string> merged = a;
    merged.insert(b.begin(), b.end());
    return static_cast<int>(merged.size());
}

std::vector<TopOverlap> top_overlap_rows(const std::vector<Group>& groups, const std::vector<double>& left_scores,
                                         const std::vector<double>& right_scores, const std::vector<int>& top_ks) {
    std::vector<TopOverlap> rows;
    for (int k : top_ks) {
        const std::set<std::string> left_top = top_modules(groups, left_scores, k);
        const std::set<std::string> right_top = top_modules(groups, right_scores, k);
        TopOverlap row;
        row.k = k;
        row.left_count = static_cast<int>(left_top.size());
        row.right_count = static_cast<int>(right_top.size());
        row.overlap = intersection_size(left_top, right_top);
        row.uni = union_size(left_top, right_top);
        row.jaccard = static_cast<double>(row.overlap) / static_cast<double>(std::max(row.uni, 1));
        row.instability = 1.0 - row.jaccard;
        rows.push_back(row);
    }
    return rows;
}

double clamp_unit(double value) {
    if (!std::isfinite(value)) return std::numeric_limits<double>::quiet_NaN();
    return std::max(0.0, std::min(1.0, value));
}

double corr_instability(double corr) {
    if (!std::isfinite(corr)) return std::numeric_limits<double>::quiet_NaN();
    return clamp_unit(1.0 - ((corr + 1.0) * 0.5));
}

InstabilitySummary summarize_instability(double positive_jaccard, double sign_agreement_ratio,
                                         double score_spearman, const std::vector<TopOverlap>& top_rows) {
    InstabilitySummary out;
    out.positive_set_instability = clamp_unit(1.0 - positive_jaccard);
    out.sign_instability = clamp_unit(1.0 - sign_agreement_ratio);
    out.score_rank_instability = corr_instability(score_spearman);
    double topk_sum = 0.0;
    int topk_count = 0;
    for (const TopOverlap& row : top_rows) {
        if (std::isfinite(row.jaccard)) {
            topk_sum += row.jaccard;
            ++topk_count;
        }
    }
    out.mean_topk_jaccard = topk_count > 0 ? topk_sum / static_cast<double>(topk_count)
                                           : std::numeric_limits<double>::quiet_NaN();
    out.topk_instability = clamp_unit(1.0 - out.mean_topk_jaccard);

    double sum = 0.0;
    int count = 0;
    for (double value : {out.positive_set_instability, out.sign_instability, out.score_rank_instability,
                         out.topk_instability}) {
        if (std::isfinite(value)) {
            sum += value;
            ++count;
        }
    }
    out.csi = count > 0 ? sum / static_cast<double>(count) : std::numeric_limits<double>::quiet_NaN();
    return out;
}

std::string format_double(double value) {
    if (!std::isfinite(value)) return "NA";
    std::ostringstream out;
    out << std::fixed << std::setprecision(4) << value;
    return out.str();
}

std::string csv_double(double value) {
    if (!std::isfinite(value)) return "";
    std::ostringstream out;
    out << std::fixed << std::setprecision(6) << value;
    return out.str();
}

std::string json_double(double value) {
    if (!std::isfinite(value)) return "null";
    std::ostringstream out;
    out << std::fixed << std::setprecision(6) << value;
    return out.str();
}

std::string json_escape(const std::string& value) {
    std::string out;
    out.reserve(value.size() + 8);
    for (const char ch : value) {
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

std::vector<int> parse_top_ks(const std::string& text) {
    std::vector<int> out;
    std::size_t cursor = 0;
    while (cursor < text.size()) {
        while (cursor < text.size() && (text[cursor] == ',' || std::isspace(static_cast<unsigned char>(text[cursor])))) {
            ++cursor;
        }
        if (cursor >= text.size()) break;
        std::size_t end = cursor;
        while (end < text.size() && text[end] != ',') {
            ++end;
        }
        const int value = std::stoi(text.substr(cursor, end - cursor));
        if (value <= 0) {
            throw std::runtime_error("--top-k values must be positive");
        }
        out.push_back(value);
        cursor = end;
    }
    if (out.empty()) {
        throw std::runtime_error("--top-k produced no values");
    }
    return out;
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
        if (arg == "--left") {
            options.left_json = require_value("--left");
        } else if (arg == "--right") {
            options.right_json = require_value("--right");
        } else if (arg == "--left-name") {
            options.left_name = require_value("--left-name");
        } else if (arg == "--right-name") {
            options.right_name = require_value("--right-name");
        } else if (arg == "--top-k") {
            options.top_ks = parse_top_ks(require_value("--top-k"));
        } else if (arg == "--epsilon") {
            options.epsilon = std::stod(require_value("--epsilon"));
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_sensitivity_stability --left left.json --right right.json\n"
                         "                                  [--left-name WikiText2] [--right-name C4]\n"
                         "                                  [--top-k 10,20,40] [--epsilon 1e-12]\n"
                         "                                  [--emit markdown|csv|json]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.left_json.empty() || options.right_json.empty()) {
        throw std::runtime_error("--left and --right are required");
    }
    if (options.emit != "markdown" && options.emit != "csv" && options.emit != "json") {
        throw std::runtime_error("--emit must be markdown, csv, or json");
    }
    if (options.epsilon < 0.0) {
        throw std::runtime_error("--epsilon must be non-negative");
    }
    return options;
}

void run(const Options& options) {
    const std::vector<Group> left_raw = read_groups(options.left_json);
    const std::vector<Group> right_raw = read_groups(options.right_json);
    std::vector<Group> left;
    std::vector<Group> right;
    align_groups(left_raw, right_raw, left, right);

    std::vector<double> left_pos;
    std::vector<double> right_pos;
    std::vector<double> left_score;
    std::vector<double> right_score;
    left_pos.reserve(left.size());
    right_pos.reserve(right.size());
    left_score.reserve(left.size());
    right_score.reserve(right.size());

    std::set<std::string> left_positive_set;
    std::set<std::string> right_positive_set;
    int both_positive = 0;
    int either_positive = 0;
    int sign_agree = 0;
    for (std::size_t i = 0; i < left.size(); ++i) {
        const bool left_positive = left[i].positive_delta_nll > options.epsilon;
        const bool right_positive = right[i].positive_delta_nll > options.epsilon;
        if (left_positive) left_positive_set.insert(left[i].module);
        if (right_positive) right_positive_set.insert(right[i].module);
        if (left_positive && right_positive) ++both_positive;
        if (left_positive || right_positive) ++either_positive;
        if (sign_bucket(left[i].signed_delta_nll, options.epsilon) ==
            sign_bucket(right[i].signed_delta_nll, options.epsilon)) {
            ++sign_agree;
        }
        left_pos.push_back(left[i].positive_delta_nll);
        right_pos.push_back(right[i].positive_delta_nll);
        left_score.push_back(left[i].positive_delta_nll / left[i].cost);
        right_score.push_back(right[i].positive_delta_nll / right[i].cost);
    }
    const int positive_union = union_size(left_positive_set, right_positive_set);
    const int positive_overlap = intersection_size(left_positive_set, right_positive_set);
    const double positive_jaccard =
        static_cast<double>(positive_overlap) / static_cast<double>(std::max(positive_union, 1));
    const double sign_agreement_ratio = static_cast<double>(sign_agree) / static_cast<double>(left.size());
    const double positive_pearson = pearson(left_pos, right_pos);
    const double positive_spearman = spearman(left_pos, right_pos);
    const double score_pearson = pearson(left_score, right_score);
    const double score_spearman = spearman(left_score, right_score);
    const double score_kendall = kendall_tau_a(left_score, right_score);
    const std::vector<TopOverlap> top_rows = top_overlap_rows(left, left_score, right_score, options.top_ks);
    const InstabilitySummary instability =
        summarize_instability(positive_jaccard, sign_agreement_ratio, score_spearman, top_rows);

    if (options.emit == "csv") {
        std::cout << "left_name,right_name,shared_modules,left_positive,right_positive,both_positive,"
                     "either_positive,positive_jaccard,sign_agreement,positive_pearson,positive_spearman,"
                     "score_pearson,score_spearman,score_kendall_tau_a,positive_set_instability,"
                     "sign_instability,score_rank_instability,mean_topk_jaccard,topk_instability,csi\n";
        std::cout << options.left_name << "," << options.right_name << "," << left.size() << ","
                  << left_positive_set.size() << "," << right_positive_set.size() << "," << both_positive << ","
                  << either_positive << "," << csv_double(positive_jaccard) << "," << csv_double(sign_agreement_ratio)
                  << "," << csv_double(positive_pearson) << "," << csv_double(positive_spearman) << ","
                  << csv_double(score_pearson) << "," << csv_double(score_spearman) << "," << csv_double(score_kendall)
                  << "," << csv_double(instability.positive_set_instability)
                  << "," << csv_double(instability.sign_instability)
                  << "," << csv_double(instability.score_rank_instability)
                  << "," << csv_double(instability.mean_topk_jaccard)
                  << "," << csv_double(instability.topk_instability)
                  << "," << csv_double(instability.csi)
                  << "\n";
        return;
    }

    if (options.emit == "json") {
        std::cout << "{\n";
        std::cout << "  \"left_name\": \"" << json_escape(options.left_name) << "\",\n";
        std::cout << "  \"right_name\": \"" << json_escape(options.right_name) << "\",\n";
        std::cout << "  \"left_json\": \"" << json_escape(options.left_json) << "\",\n";
        std::cout << "  \"right_json\": \"" << json_escape(options.right_json) << "\",\n";
        std::cout << "  \"shared_modules\": " << left.size() << ",\n";
        std::cout << "  \"left_positive_modules\": " << left_positive_set.size() << ",\n";
        std::cout << "  \"right_positive_modules\": " << right_positive_set.size() << ",\n";
        std::cout << "  \"both_positive_modules\": " << both_positive << ",\n";
        std::cout << "  \"either_positive_modules\": " << either_positive << ",\n";
        std::cout << "  \"positive_jaccard\": " << json_double(positive_jaccard) << ",\n";
        std::cout << "  \"sign_agreement\": " << json_double(sign_agreement_ratio) << ",\n";
        std::cout << "  \"positive_pearson\": " << json_double(positive_pearson) << ",\n";
        std::cout << "  \"positive_spearman\": " << json_double(positive_spearman) << ",\n";
        std::cout << "  \"score_pearson\": " << json_double(score_pearson) << ",\n";
        std::cout << "  \"score_spearman\": " << json_double(score_spearman) << ",\n";
        std::cout << "  \"score_kendall_tau_a\": " << json_double(score_kendall) << ",\n";
        std::cout << "  \"calibration_split_instability\": {\n";
        std::cout << "    \"positive_set_instability\": " << json_double(instability.positive_set_instability) << ",\n";
        std::cout << "    \"sign_instability\": " << json_double(instability.sign_instability) << ",\n";
        std::cout << "    \"score_rank_instability\": " << json_double(instability.score_rank_instability) << ",\n";
        std::cout << "    \"mean_topk_jaccard\": " << json_double(instability.mean_topk_jaccard) << ",\n";
        std::cout << "    \"topk_instability\": " << json_double(instability.topk_instability) << ",\n";
        std::cout << "    \"csi\": " << json_double(instability.csi) << "\n";
        std::cout << "  },\n";
        std::cout << "  \"topk_overlap\": [\n";
        for (std::size_t i = 0; i < top_rows.size(); ++i) {
            const TopOverlap& row = top_rows[i];
            std::cout << "    {\"k\": " << row.k << ", \"left_count\": " << row.left_count
                      << ", \"right_count\": " << row.right_count << ", \"overlap\": " << row.overlap
                      << ", \"union\": " << row.uni << ", \"jaccard\": " << json_double(row.jaccard)
                      << ", \"instability\": " << json_double(row.instability) << "}";
            std::cout << (i + 1 == top_rows.size() ? "\n" : ",\n");
        }
        std::cout << "  ]\n";
        std::cout << "}\n";
        return;
    }

    std::cout << "# Calibration Split Instability Report\n\n";
    std::cout << "Left: `" << options.left_json << "` (`" << options.left_name << "`)\n";
    std::cout << "Right: `" << options.right_json << "` (`" << options.right_name << "`)\n\n";
    std::cout << "CSI is the mean of positive-set instability, sign instability, score-rank instability, "
                 "and top-k instability. Higher means the calibration split is less reliable for bit allocation.\n\n";
    std::cout << "## Summary\n\n";
    std::cout << "| metric | value |\n";
    std::cout << "|---|---:|\n";
    std::cout << "| shared modules | " << left.size() << " |\n";
    std::cout << "| left positive modules | " << left_positive_set.size() << " |\n";
    std::cout << "| right positive modules | " << right_positive_set.size() << " |\n";
    std::cout << "| both positive modules | " << both_positive << " |\n";
    std::cout << "| either positive modules | " << either_positive << " |\n";
    std::cout << "| positive-set Jaccard | " << format_double(positive_jaccard) << " |\n";
    std::cout << "| signed-delta sign agreement | " << format_double(sign_agreement_ratio) << " |\n";
    std::cout << "| positive-delta Pearson | " << format_double(positive_pearson) << " |\n";
    std::cout << "| positive-delta Spearman | " << format_double(positive_spearman) << " |\n";
    std::cout << "| score/cost Pearson | " << format_double(score_pearson) << " |\n";
    std::cout << "| score/cost Spearman | " << format_double(score_spearman) << " |\n";
    std::cout << "| score/cost Kendall tau-a | " << format_double(score_kendall) << " |\n\n";
    std::cout << "## Calibration Split Instability\n\n";
    std::cout << "| metric | value |\n";
    std::cout << "|---|---:|\n";
    std::cout << "| positive-set instability | " << format_double(instability.positive_set_instability) << " |\n";
    std::cout << "| signed-delta sign instability | " << format_double(instability.sign_instability) << " |\n";
    std::cout << "| score-rank instability | " << format_double(instability.score_rank_instability) << " |\n";
    std::cout << "| mean top-k Jaccard | " << format_double(instability.mean_topk_jaccard) << " |\n";
    std::cout << "| top-k instability | " << format_double(instability.topk_instability) << " |\n";
    std::cout << "| CSI | " << format_double(instability.csi) << " |\n\n";
    std::cout << "## Top-K Score Overlap\n\n";
    std::cout << "| k | left top-k | right top-k | overlap | union | Jaccard | instability |\n";
    std::cout << "|---:|---:|---:|---:|---:|---:|---:|\n";
    for (const TopOverlap& row : top_rows) {
        std::cout << "| " << row.k << " | " << row.left_count << " | " << row.right_count << " | "
                  << row.overlap << " | " << row.uni << " | " << format_double(row.jaccard) << " | "
                  << format_double(row.instability) << " |\n";
    }
    std::cout << "\nThis C++ audit treats calibration split instability as the primary diagnostic target, not as "
                 "a side note. Random baselines remain sanity checks; the paper claim should be about robustness "
                 "under calibration-source shift.\n";
}

}  // namespace

int main(int argc, char** argv) {
    try {
        run(parse_args(argc, argv));
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << "\n";
        return 1;
    }
}
