#include <algorithm>
#include <cctype>
#include <chrono>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <regex>
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

bool regex_find(const std::string& text, const std::string& pattern, std::string& out) {
    std::smatch match;
    if (std::regex_search(text, match, std::regex(pattern, std::regex::icase))) {
        out = match[1].str();
        return true;
    }
    return false;
}

double first_double(const std::string& text, const std::vector<std::string>& patterns) {
    std::string out;
    for (const auto& pattern : patterns) {
        if (regex_find(text, pattern, out)) return std::stod(out);
    }
    throw std::runtime_error("numeric field not found");
}

int first_int(const std::string& text, const std::vector<std::string>& patterns) {
    std::string out;
    for (const auto& pattern : patterns) {
        if (regex_find(text, pattern, out)) return std::stoi(out);
    }
    throw std::runtime_error("integer field not found");
}

std::string parse_budget(const std::string& text) {
    std::string out;
    if (regex_find(text, "\\b(tight|medium|relaxed)\\b", out)) return lower(out);
    throw std::runtime_error("budget not found");
}

std::string parse_format(const std::string& text) {
    std::string out;
    if (regex_find(text, "\\b(INT4|INT3|MXFP4|NVFP4)\\b", out)) return upper(out);
    throw std::runtime_error("format not found");
}

std::vector<double> floats_without_layer(std::string text) {
    text = std::regex_replace(text, std::regex("layer_\\d+", std::regex::icase), "layer");
    text = std::regex_replace(text, std::regex("\\b(?:INT4|INT3|MXFP4|NVFP4)\\b", std::regex::icase), "FORMAT");
    std::vector<double> out;
    std::regex number("[-+]?\\d+(?:\\.\\d+)?");
    for (auto it = std::sregex_iterator(text.begin(), text.end(), number); it != std::sregex_iterator(); ++it) {
        out.push_back(std::stod(it->str()));
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
        double mx = first_double(text, {"\\bmax\\s*[=:]?\\s*([-+]?\\d+(?:\\.\\d+)?)", "\\bpeak\\s+([-+]?\\d+(?:\\.\\d+)?)", "\\bchannel_peak\\s*[=:]\\s*([-+]?\\d+(?:\\.\\d+)?)"});
        double p99 = first_double(text, {"\\bp99\\s*[=:]?\\s*([-+]?\\d+(?:\\.\\d+)?)", "\\btail_p99\\s*[=:]\\s*([-+]?\\d+(?:\\.\\d+)?)"});
        double kurt = first_double(text, {"\\bkurtosis\\s*[=:]?\\s*([-+]?\\d+(?:\\.\\d+)?)", "\\bkurt\\s*[=:]\\s*([-+]?\\d+(?:\\.\\d+)?)"});
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
        int ctx = first_int(text, {"\\bctx\\s*[=:]\\s*(\\d+)", "\\bcontext\\s+(\\d+)", "\\blength\\s+(\\d+)", "\\bctx\\s+(\\d+)"});
        double ks = first_double(text, {"\\bK\\s*[=:]\\s*([-+]?\\d+(?:\\.\\d+)?)", "\\bK\\s+sensitivity\\s+([-+]?\\d+(?:\\.\\d+)?)", "\\bkey_sens\\s*[=:]\\s*([-+]?\\d+(?:\\.\\d+)?)", "\\bkey\\s+sens\\s+([-+]?\\d+(?:\\.\\d+)?)"});
        double vs = first_double(text, {"\\bV\\s*[=:]\\s*([-+]?\\d+(?:\\.\\d+)?)", "\\bV\\s+sensitivity\\s+([-+]?\\d+(?:\\.\\d+)?)", "\\bvalue_sens\\s*[=:]\\s*([-+]?\\d+(?:\\.\\d+)?)", "\\bvalue\\s+sens\\s+([-+]?\\d+(?:\\.\\d+)?)"});
        return choose_kv(ctx, ks, vs);
    }
    throw std::runtime_error("unknown skill: " + skill);
}

std::string json_string_value(const std::string& line, const std::string& key) {
    std::regex pattern("\"" + key + "\"\\s*:\\s*\"((?:\\\\.|[^\"\\\\])*)\"");
    std::smatch match;
    if (!std::regex_search(line, match, pattern)) throw std::runtime_error("missing key: " + key);
    std::string raw = match[1].str();
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

bool field_equals(const std::string& response, const std::string& key, const std::string& value) {
    std::string pattern;
    if (value == "true" || value == "false" || (!value.empty() && std::all_of(value.begin(), value.end(), ::isdigit))) {
        pattern = "\"" + key + "\"\\s*:\\s*" + value + "\\b";
    } else {
        pattern = "\"" + key + "\"\\s*:\\s*\"" + value + "\"";
    }
    return std::regex_search(response, std::regex(pattern));
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
    std::cerr << "usage: quant_policy_bypass --data <jsonl> [--out <json>] [--limit N]\n";
}

int main(int argc, char** argv) {
    std::string data_path;
    std::string out_path;
    int limit = 0;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--data" && i + 1 < argc) data_path = argv[++i];
        else if (arg == "--out" && i + 1 < argc) out_path = argv[++i];
        else if (arg == "--limit" && i + 1 < argc) limit = std::stoi(argv[++i]);
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
    json << ",\n    \"_overall\": {\"n\": " << overall.n
         << ", \"policy_fields_exact\": " << (overall.policy_fields_exact / n)
         << ", \"decision_exact\": " << (overall.decision_exact / n)
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
    return 0;
}
