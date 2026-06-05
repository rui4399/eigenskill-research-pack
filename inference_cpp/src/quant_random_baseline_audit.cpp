#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct CaseInput {
    std::string dataset = "unknown";
    std::string path;
};

struct Options {
    std::vector<CaseInput> cases;
    std::string target = "cpp_loss_sensitive_budget";
    std::string emit = "markdown";
};

struct Result {
    std::string name;
    double ppl = 0.0;
};

struct AuditRow {
    std::string dataset;
    std::string target_name;
    double target_ppl = std::numeric_limits<double>::quiet_NaN();
    std::string best_seed_name;
    double best_seed_ppl = std::numeric_limits<double>::quiet_NaN();
    double seed_mean_ppl = std::numeric_limits<double>::quiet_NaN();
    double worst_seed_ppl = std::numeric_limits<double>::quiet_NaN();
    int seed_count = 0;
    int wins = 0;
    int losses = 0;
    int ties = 0;
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

bool starts_with(const std::string& value, const std::string& prefix) {
    return value.size() >= prefix.size() && std::equal(prefix.begin(), prefix.end(), value.begin());
}

std::vector<Result> read_results_json(const std::string& path) {
    const std::string text = read_text_file(path);
    const std::vector<std::string> objects = extract_array_objects(text, "results");
    std::vector<Result> results;
    results.reserve(objects.size());
    for (const std::string& object : objects) {
        Result result;
        result.name = json_string_value(object, "name");
        const std::size_t metrics_pos = find_json_key(object, "metrics");
        const std::string metrics_object = metrics_pos == std::string::npos ? object : object.substr(metrics_pos);
        result.ppl = json_number_value(metrics_object, "ppl", std::numeric_limits<double>::quiet_NaN());
        if (result.name.empty() || !std::isfinite(result.ppl)) {
            throw std::runtime_error("invalid result object in " + path);
        }
        results.push_back(result);
    }
    return results;
}

bool has_result(const std::vector<Result>& results, const std::string& name) {
    for (const Result& result : results) {
        if (result.name == name) return true;
    }
    return false;
}

double find_ppl(const std::vector<Result>& results, const std::string& name) {
    for (const Result& result : results) {
        if (result.name == name) return result.ppl;
    }
    return std::numeric_limits<double>::quiet_NaN();
}

std::string choose_target_name(const std::vector<Result>& results, const std::string& requested) {
    if (requested != "auto") return requested;
    const std::vector<std::string> candidates = {
        "wikitext_c4_consensus",
        "loss_sensitive_full",
        "cpp_loss_sensitive_budget",
        "blend_sensitivity_85",
        "allocation_loss_sensitive_consensus_4to8",
        "allocation_loss_sensitive_4to8",
    };
    for (const std::string& name : candidates) {
        if (has_result(results, name)) return name;
    }
    throw std::runtime_error("could not infer target result name; pass --target explicitly");
}

AuditRow audit_case(const CaseInput& input, const std::string& target_name) {
    const std::vector<Result> results = read_results_json(input.path);
    const std::string selected_target = choose_target_name(results, target_name);
    AuditRow row;
    row.dataset = input.dataset;
    row.target_name = selected_target;
    row.target_ppl = find_ppl(results, selected_target);
    if (!std::isfinite(row.target_ppl)) {
        throw std::runtime_error("target result not found: " + selected_target);
    }

    double total = 0.0;
    constexpr double tie_eps = 1.0e-9;
    for (const Result& result : results) {
        if (!starts_with(result.name, "random_seed_")) continue;
        ++row.seed_count;
        total += result.ppl;
        if (!std::isfinite(row.best_seed_ppl) || result.ppl < row.best_seed_ppl) {
            row.best_seed_ppl = result.ppl;
            row.best_seed_name = result.name;
        }
        if (!std::isfinite(row.worst_seed_ppl) || result.ppl > row.worst_seed_ppl) {
            row.worst_seed_ppl = result.ppl;
        }
        if (row.target_ppl + tie_eps < result.ppl) {
            ++row.wins;
        } else if (result.ppl + tie_eps < row.target_ppl) {
            ++row.losses;
        } else {
            ++row.ties;
        }
    }
    if (row.seed_count == 0) {
        throw std::runtime_error("no random_seed_* results found in " + input.path);
    }
    row.seed_mean_ppl = total / static_cast<double>(row.seed_count);
    return row;
}

std::string json_escape(const std::string& value) {
    std::ostringstream out;
    for (const char ch : value) {
        switch (ch) {
            case '\\':
                out << "\\\\";
                break;
            case '"':
                out << "\\\"";
                break;
            case '\n':
                out << "\\n";
                break;
            case '\r':
                out << "\\r";
                break;
            case '\t':
                out << "\\t";
                break;
            default:
                out << ch;
                break;
        }
    }
    return out.str();
}

void print_number(double value, int precision = 4) {
    if (std::isfinite(value)) {
        std::cout << std::fixed << std::setprecision(precision) << value;
    } else {
        std::cout << "NA";
    }
}

void print_json_number(double value) {
    if (std::isfinite(value)) {
        std::cout << std::fixed << std::setprecision(6) << value;
    } else {
        std::cout << "null";
    }
}

double win_rate(const AuditRow& row) {
    return static_cast<double>(row.wins) / static_cast<double>(std::max(1, row.seed_count));
}

void print_markdown(const std::vector<AuditRow>& rows, const std::string& target_name) {
    std::cout << "# Random Baseline Audit\n\n";
    std::cout << "Target: `" << target_name << "`\n\n";
    std::cout << "Only `random_seed_*` rows are counted as random seeds; aggregate configs such as "
                 "`cpp_random_budget` are excluded.\n\n";
    std::cout << "| dataset | target PPL | seed count | win/loss/tie | win rate | best seed | seed min/mean/max | "
                 "margin vs best seed | margin vs seed mean |\n";
    std::cout << "|---|---:|---:|---:|---:|---|---|---:|---:|\n";
    for (const AuditRow& row : rows) {
        std::cout << "| " << row.dataset << " | ";
        print_number(row.target_ppl);
        std::cout << " | " << row.seed_count << " | "
                  << row.wins << "/" << row.losses << "/" << row.ties << " | ";
        print_number(win_rate(row) * 100.0, 2);
        std::cout << "% | `" << row.best_seed_name << "` | ";
        print_number(row.best_seed_ppl);
        std::cout << " / ";
        print_number(row.seed_mean_ppl);
        std::cout << " / ";
        print_number(row.worst_seed_ppl);
        std::cout << " | ";
        print_number(row.best_seed_ppl - row.target_ppl);
        std::cout << " | ";
        print_number(row.seed_mean_ppl - row.target_ppl);
        std::cout << " |\n";
    }
    std::cout << "\nPositive margins mean the target has lower PPL than the random comparator. "
                 "Negative margins identify a random seed that beat the target.\n";
}

void print_csv(const std::vector<AuditRow>& rows) {
    std::cout << "dataset,target_name,target_ppl,seed_count,wins,losses,ties,win_rate,best_seed_name,"
                 "best_seed_ppl,seed_mean_ppl,worst_seed_ppl,margin_vs_best_seed,margin_vs_seed_mean\n";
    for (const AuditRow& row : rows) {
        std::cout << row.dataset << "," << row.target_name << ",";
        print_number(row.target_ppl, 6);
        std::cout << "," << row.seed_count << "," << row.wins << "," << row.losses << "," << row.ties << ",";
        print_number(win_rate(row), 6);
        std::cout << "," << row.best_seed_name << ",";
        print_number(row.best_seed_ppl, 6);
        std::cout << ",";
        print_number(row.seed_mean_ppl, 6);
        std::cout << ",";
        print_number(row.worst_seed_ppl, 6);
        std::cout << ",";
        print_number(row.best_seed_ppl - row.target_ppl, 6);
        std::cout << ",";
        print_number(row.seed_mean_ppl - row.target_ppl, 6);
        std::cout << "\n";
    }
}

void print_json(const std::vector<AuditRow>& rows, const std::string& target_name) {
    std::cout << "{\n";
    std::cout << "  \"target\": \"" << json_escape(target_name) << "\",\n";
    std::cout << "  \"random_selector\": \"random_seed_*\",\n";
    std::cout << "  \"rows\": [\n";
    for (std::size_t i = 0; i < rows.size(); ++i) {
        const AuditRow& row = rows[i];
        std::cout << "    {\n";
        std::cout << "      \"dataset\": \"" << json_escape(row.dataset) << "\",\n";
        std::cout << "      \"target_name\": \"" << json_escape(row.target_name) << "\",\n";
        std::cout << "      \"target_ppl\": ";
        print_json_number(row.target_ppl);
        std::cout << ",\n";
        std::cout << "      \"seed_count\": " << row.seed_count << ",\n";
        std::cout << "      \"wins\": " << row.wins << ",\n";
        std::cout << "      \"losses\": " << row.losses << ",\n";
        std::cout << "      \"ties\": " << row.ties << ",\n";
        std::cout << "      \"win_rate\": ";
        print_json_number(win_rate(row));
        std::cout << ",\n";
        std::cout << "      \"best_seed_name\": \"" << json_escape(row.best_seed_name) << "\",\n";
        std::cout << "      \"best_seed_ppl\": ";
        print_json_number(row.best_seed_ppl);
        std::cout << ",\n";
        std::cout << "      \"seed_mean_ppl\": ";
        print_json_number(row.seed_mean_ppl);
        std::cout << ",\n";
        std::cout << "      \"worst_seed_ppl\": ";
        print_json_number(row.worst_seed_ppl);
        std::cout << ",\n";
        std::cout << "      \"margin_vs_best_seed\": ";
        print_json_number(row.best_seed_ppl - row.target_ppl);
        std::cout << ",\n";
        std::cout << "      \"margin_vs_seed_mean\": ";
        print_json_number(row.seed_mean_ppl - row.target_ppl);
        std::cout << "\n";
        std::cout << "    }" << (i + 1 == rows.size() ? "\n" : ",\n");
    }
    std::cout << "  ]\n";
    std::cout << "}\n";
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
        if (arg == "--input") {
            options.cases.push_back(CaseInput{"unknown", require_value("--input")});
        } else if (arg == "--dataset") {
            if (options.cases.empty()) {
                throw std::runtime_error("--dataset must follow --input");
            }
            options.cases.back().dataset = require_value("--dataset");
        } else if (arg == "--target") {
            options.target = require_value("--target");
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_random_baseline_audit --input ppl.json --dataset name [--input ppl2.json --dataset name2]\n"
                         "                                   [--target cpp_loss_sensitive_budget|auto] [--emit markdown|csv|json]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.cases.empty()) {
        throw std::runtime_error("at least one --input is required");
    }
    if (options.emit != "markdown" && options.emit != "csv" && options.emit != "json") {
        throw std::runtime_error("--emit must be markdown, csv, or json");
    }
    return options;
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        std::vector<AuditRow> rows;
        rows.reserve(options.cases.size());
        for (const CaseInput& input : options.cases) {
            rows.push_back(audit_case(input, options.target));
        }
        if (options.emit == "csv") {
            print_csv(rows);
        } else if (options.emit == "json") {
            print_json(rows, options.target);
        } else {
            print_markdown(rows, options.target);
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << "\n";
        return 1;
    }
}
