#include <cctype>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Options {
    std::string input;
    std::string label = "task_eval";
    std::string emit = "markdown";
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

Options parse_args(int argc, char** argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        auto require_value = [&](const char* name) -> std::string {
            if (i + 1 >= argc) throw std::runtime_error(std::string("missing value for ") + name);
            return argv[++i];
        };
        if (arg == "--input") {
            options.input = require_value("--input");
        } else if (arg == "--label") {
            options.label = require_value("--label");
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_task_eval_summary --input summary.json [--emit markdown|csv|json]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.input.empty()) throw std::runtime_error("--input is required");
    if (options.emit != "markdown" && options.emit != "csv" && options.emit != "json") {
        throw std::runtime_error("--emit must be markdown, csv, or json");
    }
    return options;
}

void run(const Options& options) {
    const std::string text = read_text_file(options.input);
    const std::string model = json_string_value(text, "model");
    const int total = static_cast<int>(json_number_value(text, "total", 0.0));
    const int exact = static_cast<int>(json_number_value(text, "exact", 0.0));
    const double accuracy = json_number_value(text, "accuracy", total > 0 ? static_cast<double>(exact) / total : 0.0);
    const std::vector<std::string> rows = extract_array_objects(text, "results");
    std::map<std::string, std::pair<int, int>> by_task;
    for (const std::string& row : rows) {
        const std::string task = json_string_value(row, "task");
        const bool ok = row.find("\"exact\": true") != std::string::npos;
        auto& bucket = by_task[task.empty() ? "unknown" : task];
        bucket.first += 1;
        bucket.second += ok ? 1 : 0;
    }

    if (options.emit == "csv") {
        std::cout << "label,model,total,exact,accuracy\n";
        std::cout << options.label << "," << model << "," << total << "," << exact << "," << fmt(accuracy) << "\n";
        return;
    }
    if (options.emit == "json") {
        std::cout << "{\n"
                  << "  \"label\": \"" << json_escape(options.label) << "\",\n"
                  << "  \"model\": \"" << json_escape(model) << "\",\n"
                  << "  \"total\": " << total << ",\n"
                  << "  \"exact\": " << exact << ",\n"
                  << "  \"accuracy\": " << fmt(accuracy) << "\n"
                  << "}\n";
        return;
    }

    std::cout << "# Task Eval Summary\n\n";
    std::cout << "- label: `" << options.label << "`\n";
    std::cout << "- model: `" << model << "`\n";
    std::cout << "- total: `" << total << "`\n";
    std::cout << "- exact: `" << exact << "`\n";
    std::cout << "- accuracy: `" << fmt(accuracy) << "`\n\n";
    std::cout << "## By Task\n\n";
    std::cout << "| task | total | exact | accuracy |\n";
    std::cout << "|---|---:|---:|---:|\n";
    for (const auto& item : by_task) {
        const int task_total = item.second.first;
        const int task_exact = item.second.second;
        std::cout << "| " << item.first << " | " << task_total << " | " << task_exact << " | "
                  << fmt(static_cast<double>(task_exact) / std::max(task_total, 1)) << " |\n";
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
