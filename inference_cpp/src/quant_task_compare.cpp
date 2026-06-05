#include <algorithm>
#include <cctype>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Options {
    std::vector<std::pair<std::string, std::string>> inputs;
    std::string baseline = "fp16";
    std::string emit = "markdown";
};

struct TaskBucket {
    int total = 0;
    int exact = 0;
};

struct RunSummary {
    std::string label;
    std::string path;
    std::string model;
    int total = 0;
    int exact = 0;
    double accuracy = 0.0;
    std::map<std::string, TaskBucket> by_task;
};

std::string read_text_file(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("could not open file: " + path);
    std::ostringstream ss;
    ss << in.rdbuf();
    return ss.str();
}

std::size_t skip_ws(const std::string& text, std::size_t pos) {
    while (pos < text.size() && std::isspace(static_cast<unsigned char>(text[pos]))) ++pos;
    return pos;
}

std::size_t find_key(const std::string& text, const std::string& key, std::size_t start = 0) {
    return text.find("\"" + key + "\"", start);
}

std::string json_string_value(const std::string& object, const std::string& key) {
    std::size_t pos = find_key(object, key);
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

double json_number_value(const std::string& object, const std::string& key, double fallback = 0.0) {
    std::size_t pos = find_key(object, key);
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

std::string json_escape(const std::string& value) {
    std::string out;
    for (const char ch : value) {
        if (ch == '\\') out += "\\\\";
        else if (ch == '"') out += "\\\"";
        else if (ch == '\n') out += "\\n";
        else out.push_back(ch);
    }
    return out;
}

std::vector<std::string> extract_array_objects(const std::string& text, const std::string& array_key) {
    std::size_t pos = find_key(text, array_key);
    if (pos == std::string::npos) return {};
    pos = text.find('[', pos);
    if (pos == std::string::npos) return {};
    std::vector<std::string> objects;
    int bracket_depth = 1;
    int object_depth = 0;
    bool in_string = false;
    bool escaped = false;
    std::size_t object_start = std::string::npos;
    for (++pos; pos < text.size(); ++pos) {
        const char ch = text[pos];
        if (in_string) {
            if (escaped) escaped = false;
            else if (ch == '\\') escaped = true;
            else if (ch == '"') in_string = false;
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
    return objects;
}

std::string fmt(double value) {
    std::ostringstream out;
    out << std::fixed << std::setprecision(4) << value;
    return out.str();
}

std::pair<std::string, std::string> parse_input_spec(const std::string& spec) {
    const std::size_t eq = spec.find('=');
    if (eq == std::string::npos) {
        throw std::runtime_error("--input must be label=summary.json: " + spec);
    }
    const std::string label = spec.substr(0, eq);
    const std::string path = spec.substr(eq + 1);
    if (label.empty() || path.empty()) {
        throw std::runtime_error("--input must be label=summary.json: " + spec);
    }
    return {label, path};
}

RunSummary load_summary(const std::string& label, const std::string& path) {
    const std::string text = read_text_file(path);
    RunSummary summary;
    summary.label = label;
    summary.path = path;
    summary.model = json_string_value(text, "model");
    summary.total = static_cast<int>(json_number_value(text, "total", 0.0));
    summary.exact = static_cast<int>(json_number_value(text, "exact", 0.0));
    summary.accuracy = json_number_value(
        text,
        "accuracy",
        summary.total > 0 ? static_cast<double>(summary.exact) / summary.total : 0.0
    );

    for (const std::string& row : extract_array_objects(text, "results")) {
        std::string task = json_string_value(row, "task");
        if (task.empty()) task = "unknown";
        const bool exact = row.find("\"exact\": true") != std::string::npos;
        auto& bucket = summary.by_task[task];
        bucket.total += 1;
        bucket.exact += exact ? 1 : 0;
    }
    return summary;
}

Options parse_args(int argc, char** argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        auto require_value = [&](const char* name) -> std::string {
            if (i + 1 >= argc) throw std::runtime_error(std::string("missing value for ") + name);
            return argv[++i];
        };
        if (arg == "--input") {
            options.inputs.push_back(parse_input_spec(require_value("--input")));
        } else if (arg == "--baseline") {
            options.baseline = require_value("--baseline");
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_task_compare --input fp16=summary.json --input consensus=summary.json "
                         "[--baseline fp16] [--emit markdown|csv|json]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.inputs.empty()) throw std::runtime_error("at least one --input is required");
    if (options.emit != "markdown" && options.emit != "csv" && options.emit != "json") {
        throw std::runtime_error("--emit must be markdown, csv, or json");
    }
    return options;
}

const RunSummary* find_label(const std::vector<RunSummary>& runs, const std::string& label) {
    for (const auto& run : runs) {
        if (run.label == label) return &run;
    }
    return nullptr;
}

double accuracy_for(const TaskBucket& bucket) {
    return bucket.total > 0 ? static_cast<double>(bucket.exact) / bucket.total : 0.0;
}

std::set<std::string> collect_tasks(const std::vector<RunSummary>& runs) {
    std::set<std::string> tasks;
    for (const auto& run : runs) {
        for (const auto& item : run.by_task) tasks.insert(item.first);
    }
    return tasks;
}

void emit_csv(const std::vector<RunSummary>& runs, const RunSummary& baseline) {
    std::cout << "label,model,total,exact,accuracy,delta_vs_baseline,retention_vs_baseline\n";
    for (const auto& run : runs) {
        const double delta = run.accuracy - baseline.accuracy;
        const double retention = baseline.accuracy > 0.0 ? run.accuracy / baseline.accuracy : 0.0;
        std::cout << run.label << "," << run.model << "," << run.total << "," << run.exact << ","
                  << fmt(run.accuracy) << "," << fmt(delta) << "," << fmt(retention) << "\n";
    }
}

void emit_json(const std::vector<RunSummary>& runs, const RunSummary& baseline) {
    std::cout << "{\n";
    std::cout << "  \"baseline\": \"" << json_escape(baseline.label) << "\",\n";
    std::cout << "  \"runs\": [\n";
    for (std::size_t i = 0; i < runs.size(); ++i) {
        const auto& run = runs[i];
        const double delta = run.accuracy - baseline.accuracy;
        const double retention = baseline.accuracy > 0.0 ? run.accuracy / baseline.accuracy : 0.0;
        std::cout << "    {\"label\": \"" << json_escape(run.label) << "\", \"model\": \""
                  << json_escape(run.model) << "\", \"total\": " << run.total << ", \"exact\": "
                  << run.exact << ", \"accuracy\": " << fmt(run.accuracy)
                  << ", \"delta_vs_baseline\": " << fmt(delta)
                  << ", \"retention_vs_baseline\": " << fmt(retention) << "}";
        std::cout << (i + 1 == runs.size() ? "\n" : ",\n");
    }
    std::cout << "  ]\n";
    std::cout << "}\n";
}

void emit_markdown(const std::vector<RunSummary>& runs, const RunSummary& baseline) {
    std::cout << "# Task Accuracy Comparison\n\n";
    std::cout << "Baseline: `" << baseline.label << "`\n\n";
    std::cout << "| label | model | total | exact | accuracy | delta vs baseline | retention |\n";
    std::cout << "|---|---|---:|---:|---:|---:|---:|\n";
    for (const auto& run : runs) {
        const double delta = run.accuracy - baseline.accuracy;
        const double retention = baseline.accuracy > 0.0 ? run.accuracy / baseline.accuracy : 0.0;
        std::cout << "| `" << run.label << "` | `" << run.model << "` | " << run.total << " | "
                  << run.exact << " | " << fmt(run.accuracy) << " | " << fmt(delta) << " | "
                  << fmt(retention) << " |\n";
    }

    std::cout << "\n## Per-Task Accuracy\n\n";
    std::cout << "| task | baseline accuracy |";
    for (const auto& run : runs) std::cout << " " << run.label << " |";
    std::cout << "\n|---|---:|";
    for (std::size_t i = 0; i < runs.size(); ++i) std::cout << "---:|";
    std::cout << "\n";

    for (const auto& task : collect_tasks(runs)) {
        const auto base_it = baseline.by_task.find(task);
        const double base_acc = base_it == baseline.by_task.end() ? 0.0 : accuracy_for(base_it->second);
        std::cout << "| " << task << " | " << fmt(base_acc) << " |";
        for (const auto& run : runs) {
            const auto it = run.by_task.find(task);
            const double acc = it == run.by_task.end() ? 0.0 : accuracy_for(it->second);
            std::cout << " " << fmt(acc) << " |";
        }
        std::cout << "\n";
    }

    std::cout << "\n## Interpretation\n\n";
    std::cout << "Use this C++ report as the task-level gate for future quantized runs. "
              << "A paper-facing result should preserve task accuracy against FP16 while also "
              << "beating uniform INT4 and any budget-matched random or structural allocation baselines.\n";
}

void run(const Options& options) {
    std::vector<RunSummary> runs;
    for (const auto& input : options.inputs) runs.push_back(load_summary(input.first, input.second));
    const RunSummary* baseline = find_label(runs, options.baseline);
    if (baseline == nullptr) {
        throw std::runtime_error("baseline label not found: " + options.baseline);
    }
    if (options.emit == "csv") {
        emit_csv(runs, *baseline);
    } else if (options.emit == "json") {
        emit_json(runs, *baseline);
    } else {
        emit_markdown(runs, *baseline);
    }
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
