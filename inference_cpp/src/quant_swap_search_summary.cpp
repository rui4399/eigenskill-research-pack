#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Options {
    std::string summary_path;
    std::string guard_path;
    std::string label = "swap_search";
    std::string emit = "markdown";
    double max_memory_ratio = 0.85;
};

struct TrialRow {
    std::string out_module;
    std::string in_module;
    double ppl = std::numeric_limits<double>::quiet_NaN();
    double mean_nll = std::numeric_limits<double>::quiet_NaN();
};

struct GuardRow {
    bool present = false;
    int returncode = 0;
    bool killed = false;
    int max_memory_mib = 0;
    int memory_total_mib = 0;
    double max_memory_ratio = 0.0;
    int max_utilization_pct = 0;
};

struct Summary {
    std::string label;
    std::string model;
    int prompt_count = 0;
    int max_length = 0;
    int group_size = 0;
    bool reuse_model = false;
    double base_ppl = std::numeric_limits<double>::quiet_NaN();
    double base_mean_nll = std::numeric_limits<double>::quiet_NaN();
    double best_ppl = std::numeric_limits<double>::quiet_NaN();
    double best_mean_nll = std::numeric_limits<double>::quiet_NaN();
    std::string best_out_module;
    std::string best_in_module;
    std::vector<TrialRow> trials;
    GuardRow guard;
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

std::string json_string_value(const std::string& text, const std::string& key, const std::string& fallback = "") {
    std::size_t pos = find_json_key(text, key);
    if (pos == std::string::npos) return fallback;
    pos = text.find(':', pos);
    if (pos == std::string::npos) return fallback;
    pos = skip_ws(text, pos + 1);
    if (pos >= text.size() || text[pos] != '"') return fallback;
    ++pos;
    std::string out;
    bool escaped = false;
    for (; pos < text.size(); ++pos) {
        const char ch = text[pos];
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
    return fallback;
}

double json_number_value(const std::string& text, const std::string& key, double fallback) {
    std::size_t pos = find_json_key(text, key);
    if (pos == std::string::npos) return fallback;
    pos = text.find(':', pos);
    if (pos == std::string::npos) return fallback;
    pos = skip_ws(text, pos + 1);
    const std::size_t start = pos;
    while (pos < text.size()) {
        const char ch = text[pos];
        if ((ch >= '0' && ch <= '9') || ch == '-' || ch == '+' || ch == '.' || ch == 'e' || ch == 'E') {
            ++pos;
        } else {
            break;
        }
    }
    if (pos == start) return fallback;
    return std::stod(text.substr(start, pos - start));
}

bool json_bool_value(const std::string& text, const std::string& key, bool fallback) {
    std::size_t pos = find_json_key(text, key);
    if (pos == std::string::npos) return fallback;
    pos = text.find(':', pos);
    if (pos == std::string::npos) return fallback;
    pos = skip_ws(text, pos + 1);
    if (text.compare(pos, 4, "true") == 0) return true;
    if (text.compare(pos, 5, "false") == 0) return false;
    return fallback;
}

std::string extract_object_after_key(const std::string& text, const std::string& key) {
    std::size_t pos = find_json_key(text, key);
    if (pos == std::string::npos) {
        throw std::runtime_error("json missing object: " + key);
    }
    pos = text.find('{', pos);
    if (pos == std::string::npos) {
        throw std::runtime_error("json field is not an object: " + key);
    }
    const std::size_t start = pos;
    int depth = 0;
    bool in_string = false;
    bool escaped = false;
    for (; pos < text.size(); ++pos) {
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
        } else if (ch == '{') {
            ++depth;
        } else if (ch == '}') {
            --depth;
            if (depth == 0) {
                return text.substr(start, pos - start + 1);
            }
        }
    }
    throw std::runtime_error("unterminated object: " + key);
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
    return objects;
}

Options parse_args(int argc, char** argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        auto require_value = [&](const std::string& flag) -> std::string {
            if (i + 1 >= argc) {
                throw std::runtime_error("missing value for " + flag);
            }
            return argv[++i];
        };
        if (arg == "--summary") {
            options.summary_path = require_value("--summary");
        } else if (arg == "--guard") {
            options.guard_path = require_value("--guard");
        } else if (arg == "--label") {
            options.label = require_value("--label");
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--max-memory-ratio") {
            options.max_memory_ratio = std::stod(require_value("--max-memory-ratio"));
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_swap_search_summary --summary summary.json [--guard guard.json]\n"
                      << "                                 [--label name] [--emit markdown|csv|json]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.summary_path.empty()) {
        throw std::runtime_error("--summary is required");
    }
    if (options.emit != "markdown" && options.emit != "csv" && options.emit != "json") {
        throw std::runtime_error("--emit must be markdown, csv, or json");
    }
    return options;
}

TrialRow parse_trial(const std::string& object) {
    const std::string swap = extract_object_after_key(object, "swap");
    const std::string metrics = extract_object_after_key(object, "metrics");
    TrialRow row;
    row.out_module = json_string_value(swap, "out_module", "-");
    row.in_module = json_string_value(swap, "in_module", "-");
    row.ppl = json_number_value(metrics, "ppl", std::numeric_limits<double>::quiet_NaN());
    row.mean_nll = json_number_value(metrics, "mean_nll", std::numeric_limits<double>::quiet_NaN());
    if (!std::isfinite(row.ppl) || !std::isfinite(row.mean_nll)) {
        throw std::runtime_error("invalid trial metrics");
    }
    return row;
}

GuardRow load_guard(const std::string& path) {
    const std::string text = read_text_file(path);
    GuardRow row;
    row.present = true;
    row.returncode = static_cast<int>(json_number_value(text, "returncode", -999));
    row.killed = json_bool_value(text, "killed_by_guard", true);
    row.max_memory_mib = static_cast<int>(json_number_value(text, "max_memory_used_mib", 0));
    row.memory_total_mib = static_cast<int>(json_number_value(text, "memory_total_mib", 0));
    row.max_memory_ratio = json_number_value(text, "max_memory_used_ratio", 0.0);
    row.max_utilization_pct = static_cast<int>(json_number_value(text, "max_utilization_gpu_pct", 0));
    if (row.returncode == -999 || row.memory_total_mib <= 0 || !std::isfinite(row.max_memory_ratio)) {
        throw std::runtime_error("invalid guard json: " + path);
    }
    return row;
}

Summary load_summary(const Options& options) {
    const std::string text = read_text_file(options.summary_path);
    Summary summary;
    summary.label = options.label;
    summary.model = json_string_value(text, "model", "");
    summary.prompt_count = static_cast<int>(json_number_value(text, "prompt_count", 0));
    summary.max_length = static_cast<int>(json_number_value(text, "max_length", 0));
    summary.group_size = static_cast<int>(json_number_value(text, "group_size", 0));
    summary.reuse_model = json_bool_value(text, "reuse_model", false);

    const std::string base_metrics = extract_object_after_key(text, "base_metrics");
    summary.base_ppl = json_number_value(base_metrics, "ppl", std::numeric_limits<double>::quiet_NaN());
    summary.base_mean_nll = json_number_value(base_metrics, "mean_nll", std::numeric_limits<double>::quiet_NaN());

    const std::string best = extract_object_after_key(text, "best");
    const std::string best_metrics = extract_object_after_key(best, "metrics");
    const std::string best_swap = extract_object_after_key(best, "swap");
    summary.best_ppl = json_number_value(best_metrics, "ppl", std::numeric_limits<double>::quiet_NaN());
    summary.best_mean_nll = json_number_value(best_metrics, "mean_nll", std::numeric_limits<double>::quiet_NaN());
    summary.best_out_module = json_string_value(best_swap, "out_module", "-");
    summary.best_in_module = json_string_value(best_swap, "in_module", "-");

    for (const std::string& object : extract_array_objects(text, "trials")) {
        summary.trials.push_back(parse_trial(object));
    }
    if (!options.guard_path.empty()) {
        summary.guard = load_guard(options.guard_path);
    }
    if (!std::isfinite(summary.base_ppl) || !std::isfinite(summary.best_ppl)) {
        throw std::runtime_error("invalid summary metrics");
    }
    return summary;
}

bool guard_pass(const Summary& summary, double max_memory_ratio) {
    if (!summary.guard.present) return true;
    return summary.guard.returncode == 0 && !summary.guard.killed && summary.guard.max_memory_ratio <= max_memory_ratio;
}

double improvement_ppl(const Summary& summary) {
    return summary.base_ppl - summary.best_ppl;
}

std::string best_swap_text(const Summary& summary) {
    if (summary.best_out_module == "-" && summary.best_in_module == "-") {
        return "none";
    }
    return summary.best_out_module + " -> " + summary.best_in_module;
}

void emit_markdown(const Summary& summary, double max_memory_ratio) {
    std::cout << "# Swap Search Summary\n\n";
    std::cout << "Label: `" << summary.label << "`\n\n";
    std::cout << "| model | prompts | max length | group size | reuse model |\n";
    std::cout << "|---|---:|---:|---:|---:|\n";
    std::cout << "| " << summary.model << " | " << summary.prompt_count << " | " << summary.max_length
              << " | " << summary.group_size << " | " << (summary.reuse_model ? "true" : "false") << " |\n\n";

    std::cout << "| base PPL | best PPL | improvement | trials | best swap |\n";
    std::cout << "|---:|---:|---:|---:|---|\n";
    std::cout << std::fixed << std::setprecision(4)
              << "| " << summary.base_ppl
              << " | " << summary.best_ppl
              << " | " << improvement_ppl(summary)
              << " | " << summary.trials.size()
              << " | " << best_swap_text(summary) << " |\n\n";

    if (summary.guard.present) {
        std::cout << "| guard status | max memory | max ratio | max util | limit |\n";
        std::cout << "|---|---:|---:|---:|---:|\n";
        std::cout << "| " << (guard_pass(summary, max_memory_ratio) ? "pass" : "fail")
                  << " | " << summary.guard.max_memory_mib << " / " << summary.guard.memory_total_mib << " MiB"
                  << " | " << std::setprecision(2) << (summary.guard.max_memory_ratio * 100.0) << "%"
                  << " | " << summary.guard.max_utilization_pct << "%"
                  << " | " << (max_memory_ratio * 100.0) << "% |\n\n";
    }

    std::cout << "Interpretation: positive improvement means the one-step global-PPL swap search beat the base allocation. "
              << "Zero or negative improvement is a local-stability or negative-result signal, not a runtime claim.\n";
}

void emit_csv(const Summary& summary, double max_memory_ratio) {
    std::cout << "label,model,prompt_count,max_length,group_size,reuse_model,base_ppl,best_ppl,improvement_ppl,trials,best_swap,guard_status,max_memory_mib,memory_total_mib,max_memory_ratio,max_utilization_pct\n";
    std::cout << std::fixed << std::setprecision(6)
              << summary.label << ','
              << summary.model << ','
              << summary.prompt_count << ','
              << summary.max_length << ','
              << summary.group_size << ','
              << (summary.reuse_model ? "true" : "false") << ','
              << summary.base_ppl << ','
              << summary.best_ppl << ','
              << improvement_ppl(summary) << ','
              << summary.trials.size() << ','
              << '"' << best_swap_text(summary) << '"' << ','
              << (guard_pass(summary, max_memory_ratio) ? "pass" : "fail") << ','
              << summary.guard.max_memory_mib << ','
              << summary.guard.memory_total_mib << ','
              << summary.guard.max_memory_ratio << ','
              << summary.guard.max_utilization_pct << '\n';
}

void emit_json(const Summary& summary, double max_memory_ratio) {
    std::cout << "{\n";
    std::cout << "  \"label\": \"" << summary.label << "\",\n";
    std::cout << "  \"model\": \"" << summary.model << "\",\n";
    std::cout << "  \"prompt_count\": " << summary.prompt_count << ",\n";
    std::cout << "  \"max_length\": " << summary.max_length << ",\n";
    std::cout << "  \"group_size\": " << summary.group_size << ",\n";
    std::cout << "  \"reuse_model\": " << (summary.reuse_model ? "true" : "false") << ",\n";
    std::cout << "  \"base_ppl\": " << std::fixed << std::setprecision(6) << summary.base_ppl << ",\n";
    std::cout << "  \"best_ppl\": " << summary.best_ppl << ",\n";
    std::cout << "  \"improvement_ppl\": " << improvement_ppl(summary) << ",\n";
    std::cout << "  \"trials\": " << summary.trials.size() << ",\n";
    std::cout << "  \"best_swap\": \"" << best_swap_text(summary) << "\",\n";
    std::cout << "  \"guard_status\": \"" << (guard_pass(summary, max_memory_ratio) ? "pass" : "fail") << "\"\n";
    std::cout << "}\n";
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        const Summary summary = load_summary(options);
        if (options.emit == "markdown") {
            emit_markdown(summary, options.max_memory_ratio);
        } else if (options.emit == "csv") {
            emit_csv(summary, options.max_memory_ratio);
        } else {
            emit_json(summary, options.max_memory_ratio);
        }
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << '\n';
        return 1;
    }
}
