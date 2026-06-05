#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct GuardInput {
    std::string label;
    std::string path;
};

struct Options {
    std::vector<GuardInput> inputs;
    std::string emit = "markdown";
    double max_memory_ratio = 0.85;
};

struct GuardRow {
    std::string label;
    std::string path;
    int returncode = 0;
    bool killed = false;
    int max_memory_mib = 0;
    int memory_total_mib = 0;
    double max_memory_ratio = 0.0;
    int max_utilization_pct = 0;
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

GuardInput parse_input_arg(const std::string& text) {
    const std::size_t eq = text.find('=');
    if (eq == std::string::npos) {
        return GuardInput{text, text};
    }
    return GuardInput{text.substr(0, eq), text.substr(eq + 1)};
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
        if (arg == "--input") {
            options.inputs.push_back(parse_input_arg(require_value("--input")));
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--max-memory-ratio") {
            options.max_memory_ratio = std::stod(require_value("--max-memory-ratio"));
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: gpu_guard_summary --input label=guard.json [--input ...]\n"
                      << "                         [--emit markdown|csv|json] [--max-memory-ratio 0.85]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.inputs.empty()) {
        throw std::runtime_error("at least one --input is required");
    }
    if (options.emit != "markdown" && options.emit != "csv" && options.emit != "json") {
        throw std::runtime_error("--emit must be markdown, csv, or json");
    }
    return options;
}

GuardRow load_guard(const GuardInput& input) {
    const std::string text = read_text_file(input.path);
    GuardRow row;
    row.label = input.label;
    row.path = input.path;
    row.returncode = static_cast<int>(json_number_value(text, "returncode", -999));
    row.killed = json_bool_value(text, "killed_by_guard", true);
    row.max_memory_mib = static_cast<int>(json_number_value(text, "max_memory_used_mib", 0));
    row.memory_total_mib = static_cast<int>(json_number_value(text, "memory_total_mib", 0));
    row.max_memory_ratio = json_number_value(text, "max_memory_used_ratio", 0.0);
    row.max_utilization_pct = static_cast<int>(json_number_value(text, "max_utilization_gpu_pct", 0));
    if (row.returncode == -999 || row.memory_total_mib <= 0 || !std::isfinite(row.max_memory_ratio)) {
        throw std::runtime_error("invalid guard json: " + input.path);
    }
    return row;
}

std::vector<GuardRow> load_rows(const std::vector<GuardInput>& inputs) {
    std::vector<GuardRow> rows;
    rows.reserve(inputs.size());
    for (const GuardInput& input : inputs) {
        rows.push_back(load_guard(input));
    }
    return rows;
}

bool pass_guard(const GuardRow& row, double max_memory_ratio) {
    return row.returncode == 0 && !row.killed && row.max_memory_ratio <= max_memory_ratio;
}

void emit_markdown(const std::vector<GuardRow>& rows, double max_memory_ratio) {
    std::cout << "# GPU Guard Summary\n\n";
    std::cout << "Max allowed memory ratio: `" << std::fixed << std::setprecision(2)
              << (max_memory_ratio * 100.0) << "%`\n\n";
    std::cout << "| label | returncode | killed | max memory | max ratio | max util | status |\n";
    std::cout << "|---|---:|---:|---:|---:|---:|---|\n";
    std::cout << std::fixed << std::setprecision(2);
    for (const GuardRow& row : rows) {
        std::cout << "| " << row.label
                  << " | " << row.returncode
                  << " | " << (row.killed ? "true" : "false")
                  << " | " << row.max_memory_mib << " / " << row.memory_total_mib << " MiB"
                  << " | " << (row.max_memory_ratio * 100.0) << "%"
                  << " | " << row.max_utilization_pct << "%"
                  << " | " << (pass_guard(row, max_memory_ratio) ? "pass" : "fail")
                  << " |\n";
    }
}

void emit_csv(const std::vector<GuardRow>& rows, double max_memory_ratio) {
    std::cout << "label,returncode,killed,max_memory_mib,memory_total_mib,max_memory_ratio,max_utilization_pct,status\n";
    std::cout << std::fixed << std::setprecision(6);
    for (const GuardRow& row : rows) {
        std::cout << row.label << ','
                  << row.returncode << ','
                  << (row.killed ? "true" : "false") << ','
                  << row.max_memory_mib << ','
                  << row.memory_total_mib << ','
                  << row.max_memory_ratio << ','
                  << row.max_utilization_pct << ','
                  << (pass_guard(row, max_memory_ratio) ? "pass" : "fail")
                  << '\n';
    }
}

void emit_json(const std::vector<GuardRow>& rows, double max_memory_ratio) {
    std::cout << "{\n";
    std::cout << "  \"max_memory_ratio\": " << std::fixed << std::setprecision(6) << max_memory_ratio << ",\n";
    std::cout << "  \"rows\": [\n";
    for (std::size_t i = 0; i < rows.size(); ++i) {
        const GuardRow& row = rows[i];
        std::cout << "    {"
                  << "\"label\":\"" << row.label << "\","
                  << "\"returncode\":" << row.returncode << ","
                  << "\"killed\":" << (row.killed ? "true" : "false") << ","
                  << "\"max_memory_mib\":" << row.max_memory_mib << ","
                  << "\"memory_total_mib\":" << row.memory_total_mib << ","
                  << "\"max_memory_ratio\":" << row.max_memory_ratio << ","
                  << "\"max_utilization_pct\":" << row.max_utilization_pct << ","
                  << "\"status\":\"" << (pass_guard(row, max_memory_ratio) ? "pass" : "fail") << "\""
                  << "}";
        if (i + 1 != rows.size()) std::cout << ',';
        std::cout << '\n';
    }
    std::cout << "  ]\n";
    std::cout << "}\n";
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        const std::vector<GuardRow> rows = load_rows(options.inputs);
        if (options.emit == "markdown") {
            emit_markdown(rows, options.max_memory_ratio);
        } else if (options.emit == "csv") {
            emit_csv(rows, options.max_memory_ratio);
        } else {
            emit_json(rows, options.max_memory_ratio);
        }
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << '\n';
        return 1;
    }
}

