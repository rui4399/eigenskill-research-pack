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
    double delta_nll = 0.0;
};

struct EvidenceRow {
    std::string dataset;
    std::string target_name;
    double fp16 = std::numeric_limits<double>::quiet_NaN();
    double uniform = std::numeric_limits<double>::quiet_NaN();
    double target = std::numeric_limits<double>::quiet_NaN();
    double category = std::numeric_limits<double>::quiet_NaN();
    double best_random = std::numeric_limits<double>::quiet_NaN();
    std::string best_random_name;
    double random_mean = std::numeric_limits<double>::quiet_NaN();
    double random_max = std::numeric_limits<double>::quiet_NaN();
    int random_count = 0;
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
        result.delta_nll = json_number_value(object, "delta_nll_vs_fp16", 0.0);
        if (result.name.empty() || !std::isfinite(result.ppl)) {
            throw std::runtime_error("invalid result object in " + path);
        }
        results.push_back(result);
    }
    return results;
}

bool starts_with(const std::string& value, const std::string& prefix) {
    return value.size() >= prefix.size() && std::equal(prefix.begin(), prefix.end(), value.begin());
}

bool is_random_name(const std::string& name) {
    return name == "cpp_random_budget" || starts_with(name, "random_seed_") ||
           starts_with(name, "random_budget_seed_");
}

double find_ppl(const std::vector<Result>& results, const std::string& name) {
    for (const Result& result : results) {
        if (result.name == name) return result.ppl;
    }
    return std::numeric_limits<double>::quiet_NaN();
}

bool has_result(const std::vector<Result>& results, const std::string& name) {
    for (const Result& result : results) {
        if (result.name == name) return true;
    }
    return false;
}

std::string choose_target_name(const std::vector<Result>& results, const std::string& requested) {
    if (requested != "auto") {
        return requested;
    }
    const std::vector<std::string> candidates = {
        "wikitext_c4_consensus",
        "cpp_loss_sensitive_budget",
        "blend_sensitivity_85",
        "allocation_loss_sensitive_consensus_4to8",
        "allocation_loss_sensitive_4to8",
    };
    for (const std::string& name : candidates) {
        if (has_result(results, name)) {
            return name;
        }
    }
    throw std::runtime_error("could not infer target result name; pass --target explicitly");
}

EvidenceRow summarize_case(const CaseInput& input, const std::string& target_name) {
    const std::vector<Result> results = read_results_json(input.path);
    const std::string selected_target = choose_target_name(results, target_name);
    EvidenceRow row;
    row.dataset = input.dataset;
    row.target_name = selected_target;
    row.fp16 = find_ppl(results, "fp16");
    row.uniform = find_ppl(results, "uniform_int4");
    row.target = find_ppl(results, selected_target);
    row.category = find_ppl(results, "cpp_category_budget");

    double random_total = 0.0;
    for (const Result& result : results) {
        if (!is_random_name(result.name)) continue;
        ++row.random_count;
        random_total += result.ppl;
        if (!std::isfinite(row.best_random) || result.ppl < row.best_random) {
            row.best_random = result.ppl;
            row.best_random_name = result.name;
        }
        if (!std::isfinite(row.random_max) || result.ppl > row.random_max) {
            row.random_max = result.ppl;
        }
    }
    if (row.random_count > 0) {
        row.random_mean = random_total / row.random_count;
    }
    return row;
}

void print_number(double value) {
    if (std::isfinite(value)) {
        std::cout << std::fixed << std::setprecision(4) << value;
    } else {
        std::cout << "NA";
    }
}

void print_csv_number(double value) {
    if (std::isfinite(value)) {
        std::cout << std::fixed << std::setprecision(6) << value;
    }
}

void print_csv(const std::vector<EvidenceRow>& rows) {
    std::cout << "dataset,target_name,fp16,uniform_int4,target,category,best_random,best_random_name,random_mean,random_max,"
                 "random_count,target_improvement_vs_uniform,target_margin_vs_best_random,target_margin_vs_random_mean\n";
    for (const EvidenceRow& row : rows) {
        std::cout << row.dataset << "," << row.target_name << ",";
        print_csv_number(row.fp16);
        std::cout << ",";
        print_csv_number(row.uniform);
        std::cout << ",";
        print_csv_number(row.target);
        std::cout << ",";
        print_csv_number(row.category);
        std::cout << ",";
        print_csv_number(row.best_random);
        std::cout << "," << row.best_random_name << ",";
        print_csv_number(row.random_mean);
        std::cout << ",";
        print_csv_number(row.random_max);
        std::cout << "," << row.random_count << ",";
        print_csv_number(row.uniform - row.target);
        std::cout << ",";
        print_csv_number(row.best_random - row.target);
        std::cout << ",";
        print_csv_number(row.random_mean - row.target);
        std::cout << "\n";
    }
}

void print_markdown(const std::vector<EvidenceRow>& rows, const std::string& target_name) {
    std::cout << "# Quant Evidence Matrix\n\n";
    std::cout << "Target: `" << target_name << "`\n\n";
    std::cout << "| dataset | target config | FP16 | uniform INT4 | target | category | random min/mean/max | "
                 "target vs uniform | target vs best random | target vs random mean |\n";
    std::cout << "|---|---|---:|---:|---:|---:|---|---:|---:|---:|\n";
    for (const EvidenceRow& row : rows) {
        std::cout << "| " << row.dataset << " | `" << row.target_name << "` | ";
        print_number(row.fp16);
        std::cout << " | ";
        print_number(row.uniform);
        std::cout << " | ";
        print_number(row.target);
        std::cout << " | ";
        print_number(row.category);
        std::cout << " | ";
        print_number(row.best_random);
        std::cout << " / ";
        print_number(row.random_mean);
        std::cout << " / ";
        print_number(row.random_max);
        std::cout << " | ";
        print_number(row.uniform - row.target);
        std::cout << " | ";
        print_number(row.best_random - row.target);
        std::cout << " | ";
        print_number(row.random_mean - row.target);
        std::cout << " |\n";
    }
    std::cout << "\nPositive margins mean the target has lower PPL than the comparator. Negative margins mark a failed comparison.\n";
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
            std::cout << "Usage: quant_evidence_matrix --input ppl.json --dataset name [--input ppl2.json --dataset name2]\n"
                         "                             [--target cpp_loss_sensitive_budget|auto] [--emit markdown|csv]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.cases.empty()) {
        throw std::runtime_error("at least one --input is required");
    }
    if (options.emit != "markdown" && options.emit != "csv") {
        throw std::runtime_error("--emit must be markdown or csv");
    }
    return options;
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        std::vector<EvidenceRow> rows;
        rows.reserve(options.cases.size());
        for (const CaseInput& input : options.cases) {
            rows.push_back(summarize_case(input, options.target));
        }
        if (options.emit == "csv") {
            print_csv(rows);
        } else {
            print_markdown(rows, options.target);
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << "\n";
        return 1;
    }
}
