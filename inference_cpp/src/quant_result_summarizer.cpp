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

struct Options {
    std::string input_json;
    std::string dataset = "unknown";
    std::string target = "cpp_loss_sensitive_budget";
    std::string emit = "markdown";
};

struct Result {
    std::string name;
    double ppl = 0.0;
    double delta_nll = 0.0;
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
        const std::string metrics_object =
            metrics_pos == std::string::npos ? object : object.substr(metrics_pos);
        result.ppl = json_number_value(metrics_object, "ppl", std::numeric_limits<double>::quiet_NaN());
        result.delta_nll = json_number_value(object, "delta_nll_vs_fp16", 0.0);
        if (result.name.empty() || !std::isfinite(result.ppl)) {
            throw std::runtime_error("invalid result object: missing name or ppl");
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

const Result* find_result(const std::vector<Result>& results, const std::string& name) {
    for (const Result& result : results) {
        if (result.name == name) {
            return &result;
        }
    }
    return nullptr;
}

std::vector<const Result*> random_results(const std::vector<Result>& results) {
    std::vector<const Result*> out;
    for (const Result& result : results) {
        if (is_random_name(result.name)) {
            out.push_back(&result);
        }
    }
    return out;
}

double mean_ppl(const std::vector<const Result*>& results) {
    double total = 0.0;
    for (const Result* result : results) {
        total += result->ppl;
    }
    return total / std::max<std::size_t>(results.size(), 1);
}

void print_csv(const Options& options, const std::vector<Result>& results) {
    const Result* target = find_result(results, options.target);
    const std::vector<const Result*> randoms = random_results(results);
    const auto by_ppl = [](const Result* a, const Result* b) { return a->ppl < b->ppl; };
    const Result* best_random = randoms.empty() ? nullptr : *std::min_element(randoms.begin(), randoms.end(), by_ppl);
    const double random_mean = randoms.empty() ? std::numeric_limits<double>::quiet_NaN() : mean_ppl(randoms);

    std::cout << "dataset,name,ppl,delta_nll_vs_fp16,role,target_margin_vs_best_random,random_mean\n";
    std::cout << std::fixed << std::setprecision(6);
    for (const Result& result : results) {
        std::string role = "candidate";
        if (result.name == options.target) role = "target";
        if (is_random_name(result.name)) role = "random";
        const double margin = (target && best_random && result.name == options.target) ? target->ppl - best_random->ppl
                                                                                      : std::numeric_limits<double>::quiet_NaN();
        std::cout << options.dataset << "," << result.name << "," << result.ppl << "," << result.delta_nll << ","
                  << role << ",";
        if (std::isfinite(margin)) {
            std::cout << margin;
        }
        std::cout << ",";
        if (std::isfinite(random_mean)) {
            std::cout << random_mean;
        }
        std::cout << "\n";
    }
}

void print_markdown(const Options& options, const std::vector<Result>& results) {
    const Result* target = find_result(results, options.target);
    const Result* uniform = find_result(results, "uniform_int4");
    std::vector<const Result*> randoms = random_results(results);
    const auto by_ppl = [](const Result* a, const Result* b) { return a->ppl < b->ppl; };
    const Result* best_random = randoms.empty() ? nullptr : *std::min_element(randoms.begin(), randoms.end(), by_ppl);
    const Result* worst_random = randoms.empty() ? nullptr : *std::max_element(randoms.begin(), randoms.end(), by_ppl);
    const double random_mean = randoms.empty() ? std::numeric_limits<double>::quiet_NaN() : mean_ppl(randoms);

    std::vector<Result> ranked = results;
    std::sort(ranked.begin(), ranked.end(), [](const Result& a, const Result& b) {
        if (a.ppl != b.ppl) return a.ppl < b.ppl;
        return a.name < b.name;
    });

    std::cout << "# Quant Result Summary\n\n";
    std::cout << "Dataset: `" << options.dataset << "`\n\n";
    std::cout << "Target: `" << options.target << "`\n\n";
    if (target) {
        std::cout << "- Target PPL: `" << std::fixed << std::setprecision(4) << target->ppl << "`\n";
    }
    if (uniform && target) {
        std::cout << "- Target improvement vs uniform INT4: `" << std::fixed << std::setprecision(4)
                  << (uniform->ppl - target->ppl) << "` PPL\n";
    }
    if (best_random && target) {
        std::cout << "- Best random PPL: `" << std::fixed << std::setprecision(4) << best_random->ppl << "` (`"
                  << best_random->name << "`)\n";
        std::cout << "- Target margin vs best random: `" << std::fixed << std::setprecision(4)
                  << (best_random->ppl - target->ppl) << "` PPL\n";
    }
    if (best_random && worst_random) {
        std::cout << "- Random PPL min/mean/max: `" << std::fixed << std::setprecision(4) << best_random->ppl
                  << " / " << random_mean << " / " << worst_random->ppl << "`\n";
    }
    std::cout << "\n| rank | name | PPL | delta NLL vs FP16 |\n";
    std::cout << "|---:|---|---:|---:|\n";
    for (std::size_t i = 0; i < ranked.size(); ++i) {
        std::cout << "| " << (i + 1) << " | `" << ranked[i].name << "` | " << std::fixed << std::setprecision(4)
                  << ranked[i].ppl << " | " << ranked[i].delta_nll << " |\n";
    }
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
            options.input_json = require_value("--input");
        } else if (arg == "--dataset") {
            options.dataset = require_value("--dataset");
        } else if (arg == "--target") {
            options.target = require_value("--target");
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_result_summarizer --input ppl_summary.json [--dataset name]\n"
                         "                               [--target cpp_loss_sensitive_budget]\n"
                         "                               [--emit markdown|csv]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.input_json.empty()) {
        throw std::runtime_error("--input is required");
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
        const std::vector<Result> results = read_results_json(options.input_json);
        if (options.emit == "csv") {
            print_csv(options, results);
        } else {
            print_markdown(options, results);
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << "\n";
        return 1;
    }
}
