#include <algorithm>
#include <cctype>
#include <chrono>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

struct Policy {
    std::map<std::string, std::string> fields;
};

struct Stats {
    int n = 0;
    int policy_fields_exact = 0;
    int decision_exact = 0;
    int parse_error = 0;
};

std::string read_file(const std::string& path) {
    std::ifstream in(path, std::ios::binary);
    if (!in) throw std::runtime_error("cannot open file: " + path);
    std::ostringstream ss;
    ss << in.rdbuf();
    return ss.str();
}

std::string trim(const std::string& s) {
    std::size_t first = 0;
    while (first < s.size() && std::isspace(static_cast<unsigned char>(s[first]))) ++first;
    std::size_t last = s.size();
    while (last > first && std::isspace(static_cast<unsigned char>(s[last - 1]))) --last;
    return s.substr(first, last - first);
}

std::string lower(std::string s) {
    for (char& c : s) c = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
    return s;
}

std::string upper(std::string s) {
    for (char& c : s) c = static_cast<char>(std::toupper(static_cast<unsigned char>(c)));
    return s;
}

bool starts_with_ci(const std::string& text, std::size_t pos, const std::string& needle) {
    if (pos + needle.size() > text.size()) return false;
    for (std::size_t i = 0; i < needle.size(); ++i) {
        char a = static_cast<char>(std::tolower(static_cast<unsigned char>(text[pos + i])));
        char b = static_cast<char>(std::tolower(static_cast<unsigned char>(needle[i])));
        if (a != b) return false;
    }
    return true;
}

bool is_word_char(char c) {
    return std::isalnum(static_cast<unsigned char>(c)) || c == '_';
}

bool contains_word_ci(const std::string& text, const std::string& word) {
    for (std::size_t pos = 0; pos + word.size() <= text.size(); ++pos) {
        if (!starts_with_ci(text, pos, word)) continue;
        bool left = pos > 0 && is_word_char(text[pos - 1]);
        bool right = pos + word.size() < text.size() && is_word_char(text[pos + word.size()]);
        if (!left && !right) return true;
    }
    return false;
}

bool parse_number_at(const std::string& text, std::size_t pos, double& value, std::size_t& end_pos) {
    if (pos >= text.size()) return false;
    const char* begin = text.c_str() + pos;
    char* end = nullptr;
    value = std::strtod(begin, &end);
    if (end == begin) return false;
    end_pos = static_cast<std::size_t>(end - text.c_str());
    return true;
}

bool scan_next_number(const std::string& text, std::size_t pos, double& value, std::size_t& end_pos) {
    for (std::size_t i = pos; i < text.size(); ++i) {
        char c = text[i];
        bool number_start = std::isdigit(static_cast<unsigned char>(c)) || c == '+' || c == '-' ||
                            (c == '.' && i + 1 < text.size() && std::isdigit(static_cast<unsigned char>(text[i + 1])));
        if (!number_start) continue;
        if (parse_number_at(text, i, value, end_pos)) return true;
    }
    return false;
}

std::size_t find_ci(const std::string& text, const std::string& needle, std::size_t start = 0) {
    for (std::size_t pos = start; pos + needle.size() <= text.size(); ++pos) {
        if (starts_with_ci(text, pos, needle)) return pos;
    }
    return std::string::npos;
}

double first_labeled_double(const std::string& text, const std::vector<std::string>& labels) {
    for (const auto& label : labels) {
        std::size_t pos = find_ci(text, label);
        if (pos == std::string::npos) continue;
        double value = 0.0;
        std::size_t end_pos = 0;
        if (scan_next_number(text, pos + label.size(), value, end_pos)) return value;
    }
    throw std::runtime_error("numeric field not found");
}

int first_labeled_int(const std::string& text, const std::vector<std::string>& labels) {
    return static_cast<int>(std::llround(first_labeled_double(text, labels)));
}

std::string parse_budget(const std::string& text) {
    if (contains_word_ci(text, "tight")) return "tight";
    if (contains_word_ci(text, "medium")) return "medium";
    if (contains_word_ci(text, "relaxed")) return "relaxed";
    throw std::runtime_error("budget not found");
}

std::string parse_format(const std::string& text) {
    if (contains_word_ci(text, "INT4")) return "INT4";
    if (contains_word_ci(text, "INT3")) return "INT3";
    if (contains_word_ci(text, "MXFP4")) return "MXFP4";
    if (contains_word_ci(text, "NVFP4")) return "NVFP4";
    throw std::runtime_error("format not found");
}

std::vector<double> floats_without_layer(const std::string& text) {
    std::vector<double> out;
    for (std::size_t i = 0; i < text.size();) {
        if (starts_with_ci(text, i, "layer_")) {
            i += 6;
            while (i < text.size() && std::isdigit(static_cast<unsigned char>(text[i]))) ++i;
            continue;
        }
        if (starts_with_ci(text, i, "INT")) {
            i += 3;
            while (i < text.size() && std::isdigit(static_cast<unsigned char>(text[i]))) ++i;
            continue;
        }
        if (starts_with_ci(text, i, "MXFP") || starts_with_ci(text, i, "NVFP")) {
            i += 4;
            while (i < text.size() && std::isdigit(static_cast<unsigned char>(text[i]))) ++i;
            continue;
        }
        char c = text[i];
        bool number_start = std::isdigit(static_cast<unsigned char>(c)) || c == '+' || c == '-' ||
                            (c == '.' && i + 1 < text.size() && std::isdigit(static_cast<unsigned char>(text[i + 1])));
        if (number_start) {
            double value = 0.0;
            std::size_t end_pos = 0;
            if (!parse_number_at(text, i, value, end_pos)) {
                ++i;
                continue;
            }
            out.push_back(value);
            i = end_pos;
        } else {
            ++i;
        }
    }
    return out;
}

Policy choose_outlier(double mx, double p99, double kurt) {
    double risk = (mx / std::max(p99, 1.0e-6)) + 0.25 * kurt;
    bool protect = risk > 5.2 || kurt > 9.0 || mx > 8.0;
    Policy p;
    p.fields["policy"] = protect ? "protect_top_channels" : "standard_group_quant";
    p.fields["protect"] = protect ? "true" : "false";
    p.fields["skill"] = "outlier_detect";
    return p;
}

Policy choose_bits(double sens, double var, const std::string& budget) {
    double score = sens * std::sqrt(var);
    int bits = 4;
    if (budget == "tight") {
        bits = score > 1.45 ? 4 : (score > 0.8 ? 3 : 2);
    } else if (budget == "medium") {
        bits = score > 2.2 ? 8 : (score > 0.75 ? 4 : 3);
    } else {
        bits = score > 1.25 ? 8 : 4;
    }
    Policy p;
    p.fields["bits"] = std::to_string(bits);
    p.fields["format"] = bits == 8 ? "INT8" : "INT" + std::to_string(bits);
    p.fields["skill"] = "bit_allocate";
    return p;
}

Policy choose_rotation(double block, double kurt, const std::string& fmt) {
    std::string rot;
    if ((fmt == "MXFP4" || fmt == "NVFP4") && block > 1.35) {
        rot = "two_level_block_orthogonal";
    } else if (kurt > 7.5) {
        rot = "block_hadamard";
    } else if (block > 1.1) {
        rot = "butterfly";
    } else {
        rot = "none";
    }
    Policy p;
    p.fields["format"] = fmt;
    p.fields["rotation"] = rot;
    p.fields["skill"] = "rotation_select";
    return p;
}

Policy choose_residual(double e1, double e4, double e8) {
    int rank = 0;
    if (e8 > 0.78) rank = 8;
    else if (e4 > 0.62) rank = 4;
    else if (e1 > 0.45) rank = 2;
    Policy p;
    p.fields["apply"] = rank > 0 ? "true" : "false";
    p.fields["rank"] = std::to_string(rank);
    p.fields["skill"] = "residual_patch";
    return p;
}

Policy choose_kv(int ctx, double ks, double vs) {
    double sens = std::max(ks, vs);
    std::string policy;
    if (ctx >= 8192 && sens < 0.55) {
        policy = "int2_history_bf16_recent";
    } else if (ctx >= 4096 && sens < 0.8) {
        policy = "int4_tokenwise_with_recent_window";
    } else if (sens >= 1.1) {
        policy = "int8_or_bf16_sensitive_heads";
    } else {
        policy = "int4_groupwise";
    }
    Policy p;
    p.fields["context"] = std::to_string(ctx);
    p.fields["policy"] = policy;
    p.fields["skill"] = "kv_policy";
    return p;
}

Policy predict(const std::string& skill, const std::string& text) {
    auto nums = floats_without_layer(text);
    if (skill == "outlier_detect") {
        double mx = first_labeled_double(text, {"channel_peak", "max", "peak"});
        double p99 = first_labeled_double(text, {"tail_p99", "p99"});
        double kurt = first_labeled_double(text, {"kurtosis", "kurt"});
        return choose_outlier(mx, p99, kurt);
    }
    if (skill == "bit_allocate") {
        if (nums.size() < 2) throw std::runtime_error("bit allocation numbers not found");
        return choose_bits(nums[0], nums[1], parse_budget(text));
    }
    if (skill == "rotation_select") {
        if (nums.size() < 2) throw std::runtime_error("rotation numbers not found");
        return choose_rotation(nums[0], nums[1], parse_format(text));
    }
    if (skill == "residual_patch") {
        if (nums.size() < 3) throw std::runtime_error("residual spectrum not found");
        return choose_residual(nums[0], nums[1], nums[2]);
    }
    if (skill == "kv_policy") {
        int ctx = first_labeled_int(text, {"ctx", "context", "length"});
        double ks = first_labeled_double(text, {"key_sens", "key sens", "K sensitivity", "K="});
        double vs = first_labeled_double(text, {"value_sens", "value sens", "V sensitivity", "V="});
        return choose_kv(ctx, ks, vs);
    }
    throw std::runtime_error("unknown skill: " + skill);
}

std::string json_string_value(const std::string& line, const std::string& key) {
    std::string needle = "\"" + key + "\"";
    std::size_t pos = line.find(needle);
    if (pos == std::string::npos) throw std::runtime_error("missing key: " + key);
    pos = line.find(':', pos + needle.size());
    if (pos == std::string::npos) throw std::runtime_error("missing key separator: " + key);
    ++pos;
    while (pos < line.size() && std::isspace(static_cast<unsigned char>(line[pos]))) ++pos;
    if (pos >= line.size() || line[pos] != '"') throw std::runtime_error("key is not a string: " + key);
    ++pos;
    std::string raw;
    bool escaped = false;
    for (; pos < line.size(); ++pos) {
        char c = line[pos];
        if (escaped) {
            raw.push_back('\\');
            raw.push_back(c);
            escaped = false;
        } else if (c == '\\') {
            escaped = true;
        } else if (c == '"') {
            break;
        } else {
            raw.push_back(c);
        }
    }
    std::string out;
    for (std::size_t i = 0; i < raw.size(); ++i) {
        if (raw[i] == '\\' && i + 1 < raw.size()) {
            char n = raw[++i];
            if (n == 'n') out.push_back('\n');
            else if (n == 't') out.push_back('\t');
            else out.push_back(n);
        } else {
            out.push_back(raw[i]);
        }
    }
    return out;
}

std::string json_scalar_value(const std::string& line, const std::string& key) {
    std::string needle = "\"" + key + "\"";
    std::size_t pos = line.find(needle);
    if (pos == std::string::npos) return "";
    pos = line.find(':', pos + needle.size());
    if (pos == std::string::npos) return "";
    ++pos;
    while (pos < line.size() && std::isspace(static_cast<unsigned char>(line[pos]))) ++pos;
    if (pos >= line.size()) return "";
    if (line[pos] == '"') {
        ++pos;
        std::string out;
        bool escaped = false;
        for (; pos < line.size(); ++pos) {
            char c = line[pos];
            if (escaped) {
                out.push_back(c);
                escaped = false;
            } else if (c == '\\') {
                escaped = true;
            } else if (c == '"') {
                break;
            } else {
                out.push_back(c);
            }
        }
        return out;
    }
    std::size_t start = pos;
    while (pos < line.size() && line[pos] != ',' && line[pos] != '}') ++pos;
    return trim(line.substr(start, pos - start));
}

bool field_equals(const std::string& response, const std::string& key, const std::string& value) {
    return json_scalar_value(response, key) == value;
}

bool decision_exact(const std::string& skill, const Policy& pred, const std::string& response) {
    static const std::map<std::string, std::vector<std::string>> keys = {
        {"outlier_detect", {"protect", "policy"}},
        {"bit_allocate", {"bits", "format"}},
        {"rotation_select", {"rotation", "format"}},
        {"residual_patch", {"rank", "apply"}},
        {"kv_policy", {"policy", "context"}},
    };
    auto it = keys.find(skill);
    if (it == keys.end()) return false;
    for (const auto& key : it->second) {
        auto pred_it = pred.fields.find(key);
        if (pred_it == pred.fields.end() || !field_equals(response, key, pred_it->second)) return false;
    }
    return true;
}

std::string policy_json(const Policy& p) {
    std::ostringstream ss;
    ss << "{";
    bool first = true;
    for (const auto& [key, value] : p.fields) {
        if (!first) ss << ",";
        first = false;
        ss << "\"" << key << "\":";
        if (value == "true" || value == "false" || (!value.empty() && std::all_of(value.begin(), value.end(), ::isdigit))) {
            ss << value;
        } else {
            ss << "\"" << value << "\"";
        }
    }
    ss << "}";
    return ss.str();
}

void usage() {
    std::cerr << "usage: quant_policy_bypass --data <jsonl> [--out <json>] [--limit N] [--min-decision-exact X]\n";
}

int main(int argc, char** argv) {
    std::string data_path;
    std::string out_path;
    int limit = 0;
    double min_decision_exact = -1.0;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--data" && i + 1 < argc) data_path = argv[++i];
        else if (arg == "--out" && i + 1 < argc) out_path = argv[++i];
        else if (arg == "--limit" && i + 1 < argc) limit = std::stoi(argv[++i]);
        else if (arg == "--min-decision-exact" && i + 1 < argc) min_decision_exact = std::stod(argv[++i]);
        else if (arg == "--help" || arg == "-h") { usage(); return 0; }
        else { usage(); return 2; }
    }
    if (data_path.empty()) { usage(); return 2; }

    std::ifstream in(data_path);
    if (!in) {
        std::cerr << "cannot open data: " << data_path << "\n";
        return 1;
    }

    std::map<std::string, Stats> by_skill;
    Stats overall;
    std::string line;
    int row_index = 0;
    auto t0 = std::chrono::high_resolution_clock::now();
    while (std::getline(in, line)) {
        if (trim(line).empty()) continue;
        if (limit > 0 && row_index >= limit) break;
        ++row_index;
        std::string skill = json_string_value(line, "skill");
        std::string input = json_string_value(line, "input");
        std::string response = json_string_value(line, "response");
        Stats& stats = by_skill[skill];
        stats.n += 1;
        overall.n += 1;
        try {
            Policy pred = predict(skill, input);
            bool ok = decision_exact(skill, pred, response);
            stats.decision_exact += ok ? 1 : 0;
            stats.policy_fields_exact += ok ? 1 : 0;
            overall.decision_exact += ok ? 1 : 0;
            overall.policy_fields_exact += ok ? 1 : 0;
        } catch (const std::exception&) {
            stats.parse_error += 1;
            overall.parse_error += 1;
        }
    }
    auto t1 = std::chrono::high_resolution_clock::now();
    double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();

    std::ostringstream json;
    json << std::fixed << std::setprecision(6);
    json << "{\n";
    json << "  \"data\": \"" << data_path << "\",\n";
    json << "  \"limit\": " << limit << ",\n";
    json << "  \"elapsed_ms\": " << ms << ",\n";
    json << "  \"rows_per_second\": " << (overall.n ? (1000.0 * overall.n / std::max(ms, 1.0e-9)) : 0.0) << ",\n";
    json << "  \"summary\": {\n";
    bool first = true;
    for (const auto& [skill, s] : by_skill) {
        if (!first) json << ",\n";
        first = false;
        double n = std::max(s.n, 1);
        json << "    \"" << skill << "\": {\"n\": " << s.n
             << ", \"policy_fields_exact\": " << (s.policy_fields_exact / n)
             << ", \"decision_exact\": " << (s.decision_exact / n)
             << ", \"parse_error\": " << (s.parse_error / n) << "}";
    }
    double n = std::max(overall.n, 1);
    double overall_decision_exact = overall.decision_exact / n;
    json << ",\n    \"_overall\": {\"n\": " << overall.n
         << ", \"policy_fields_exact\": " << (overall.policy_fields_exact / n)
         << ", \"decision_exact\": " << overall_decision_exact
         << ", \"parse_error\": " << (overall.parse_error / n) << "}\n";
    json << "  }\n";
    json << "}\n";

    std::cout << json.str();
    if (!out_path.empty()) {
        std::ofstream out(out_path);
        if (!out) {
            std::cerr << "cannot write output: " << out_path << "\n";
            return 1;
        }
        out << json.str();
    }
    if (min_decision_exact >= 0.0 && overall_decision_exact + 1.0e-12 < min_decision_exact) {
        std::cerr << "decision_exact " << overall_decision_exact
                  << " below required " << min_decision_exact << "\n";
        return 1;
    }
    return 0;
}
