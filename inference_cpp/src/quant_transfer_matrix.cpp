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

struct CaseInput {
    std::string dataset;
    std::string summary_path;
    std::string guard_path;
};

struct Options {
    std::vector<CaseInput> cases;
    std::string base = "loss_sensitive_full";
    std::string target = "swap_search_wikitext2_64";
    std::string emit = "markdown";
    double max_memory_ratio = 0.85;
};

struct GuardInfo {
    bool present = false;
    int returncode = 0;
    bool killed = false;
    int max_memory_mib = 0;
    int memory_total_mib = 0;
    double max_memory_ratio = 0.0;
};

struct Row {
    std::string dataset;
    double fp16 = std::numeric_limits<double>::quiet_NaN();
    double uniform_int4 = std::numeric_limits<double>::quiet_NaN();
    double base_ppl = std::numeric_limits<double>::quiet_NaN();
    double target_ppl = std::numeric_limits<double>::quiet_NaN();
    GuardInfo guard;
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

std::string json_string_value(const std::string& text, const std::string& key) {
    std::size_t pos = find_json_key(text, key);
    if (pos == std::string::npos) return "";
    pos = text.find(':', pos);
    if (pos == std::string::npos) return "";
    pos = skip_ws(text, pos + 1);
    if (pos >= text.size() || text[pos] != '"') return "";
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
    return "";
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

CaseInput parse_case_arg(const std::string& value) {
    const std::size_t eq = value.find('=');
    if (eq == std::string::npos) {
        throw std::runtime_error("--case expects dataset=summary.json");
    }
    return CaseInput{value.substr(0, eq), value.substr(eq + 1), ""};
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
        if (arg == "--case") {
            options.cases.push_back(parse_case_arg(require_value("--case")));
        } else if (arg == "--guard") {
            if (options.cases.empty()) {
                throw std::runtime_error("--guard must follow a --case");
            }
            options.cases.back().guard_path = require_value("--guard");
        } else if (arg == "--base") {
            options.base = require_value("--base");
        } else if (arg == "--target") {
            options.target = require_value("--target");
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--max-memory-ratio") {
            options.max_memory_ratio = std::stod(require_value("--max-memory-ratio"));
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_transfer_matrix --case dataset=summary.json [--guard guard.json] ...\n"
                      << "                             [--base loss_sensitive_full] [--target swap_search_wikitext2_64]\n"
                      << "                             [--emit markdown|csv|json]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.cases.empty()) {
        throw std::runtime_error("at least one --case is required");
    }
    if (options.emit != "markdown" && options.emit != "csv" && options.emit != "json") {
        throw std::runtime_error("--emit must be markdown, csv, or json");
    }
    return options;
}

double result_ppl(const std::string& text, const std::string& name) {
    for (const std::string& object : extract_array_objects(text, "results")) {
        if (json_string_value(object, "name") != name) continue;
        const std::string metrics = extract_object_after_key(object, "metrics");
        const double ppl = json_number_value(metrics, "ppl", std::numeric_limits<double>::quiet_NaN());
        if (!std::isfinite(ppl)) {
            throw std::runtime_error("invalid ppl for result: " + name);
        }
        return ppl;
    }
    return std::numeric_limits<double>::quiet_NaN();
}

GuardInfo load_guard(const std::string& path) {
    const std::string text = read_text_file(path);
    GuardInfo guard;
    guard.present = true;
    guard.returncode = static_cast<int>(json_number_value(text, "returncode", -999));
    guard.killed = json_bool_value(text, "killed_by_guard", true);
    guard.max_memory_mib = static_cast<int>(json_number_value(text, "max_memory_used_mib", 0));
    guard.memory_total_mib = static_cast<int>(json_number_value(text, "memory_total_mib", 0));
    guard.max_memory_ratio = json_number_value(text, "max_memory_used_ratio", 0.0);
    if (guard.returncode == -999 || guard.memory_total_mib <= 0 || !std::isfinite(guard.max_memory_ratio)) {
        throw std::runtime_error("invalid guard json: " + path);
    }
    return guard;
}

Row load_row(const CaseInput& input, const Options& options) {
    const std::string text = read_text_file(input.summary_path);
    Row row;
    row.dataset = input.dataset;
    row.fp16 = result_ppl(text, "fp16");
    row.uniform_int4 = result_ppl(text, "uniform_int4");
    row.base_ppl = result_ppl(text, options.base);
    row.target_ppl = result_ppl(text, options.target);
    if (!input.guard_path.empty()) {
        row.guard = load_guard(input.guard_path);
    }
    if (!std::isfinite(row.base_ppl) || !std::isfinite(row.target_ppl)) {
        throw std::runtime_error("missing base or target result in " + input.summary_path);
    }
    return row;
}

bool guard_pass(const GuardInfo& guard, double max_memory_ratio) {
    if (!guard.present) return true;
    return guard.returncode == 0 && !guard.killed && guard.max_memory_ratio <= max_memory_ratio;
}

double improvement(const Row& row) {
    return row.base_ppl - row.target_ppl;
}

std::vector<Row> load_rows(const Options& options) {
    std::vector<Row> rows;
    rows.reserve(options.cases.size());
    for (const CaseInput& input : options.cases) {
        rows.push_back(load_row(input, options));
    }
    return rows;
}

void emit_markdown(const std::vector<Row>& rows, const Options& options) {
    std::cout << "# Quant Transfer Matrix\n\n";
    std::cout << "Base: `" << options.base << "`  Target: `" << options.target << "`\n\n";
    std::cout << "| dataset | FP16 | uniform INT4 | base PPL | target PPL | improvement | guard |\n";
    std::cout << "|---|---:|---:|---:|---:|---:|---|\n";
    std::cout << std::fixed << std::setprecision(4);
    for (const Row& row : rows) {
        std::cout << "| " << row.dataset
                  << " | " << row.fp16
                  << " | " << row.uniform_int4
                  << " | " << row.base_ppl
                  << " | " << row.target_ppl
                  << " | " << improvement(row)
                  << " | " << (guard_pass(row.guard, options.max_memory_ratio) ? "pass" : "fail");
        if (row.guard.present) {
            std::cout << " (" << std::setprecision(2) << row.guard.max_memory_ratio * 100.0 << "%)"
                      << std::setprecision(4);
        }
        std::cout << " |\n";
    }
    std::cout << "\nPositive improvement means the target allocation lowers PPL relative to the base allocation on that dataset.\n";
}

void emit_csv(const std::vector<Row>& rows, const Options& options) {
    std::cout << "dataset,fp16,uniform_int4,base,target,improvement,guard_status,max_memory_ratio\n";
    std::cout << std::fixed << std::setprecision(6);
    for (const Row& row : rows) {
        std::cout << row.dataset << ','
                  << row.fp16 << ','
                  << row.uniform_int4 << ','
                  << row.base_ppl << ','
                  << row.target_ppl << ','
                  << improvement(row) << ','
                  << (guard_pass(row.guard, options.max_memory_ratio) ? "pass" : "fail") << ','
                  << row.guard.max_memory_ratio << '\n';
    }
}

void emit_json(const std::vector<Row>& rows, const Options& options) {
    std::cout << "{\n";
    std::cout << "  \"base\": \"" << options.base << "\",\n";
    std::cout << "  \"target\": \"" << options.target << "\",\n";
    std::cout << "  \"rows\": [\n";
    std::cout << std::fixed << std::setprecision(6);
    for (std::size_t i = 0; i < rows.size(); ++i) {
        const Row& row = rows[i];
        std::cout << "    {"
                  << "\"dataset\":\"" << row.dataset << "\","
                  << "\"fp16\":" << row.fp16 << ","
                  << "\"uniform_int4\":" << row.uniform_int4 << ","
                  << "\"base\":" << row.base_ppl << ","
                  << "\"target\":" << row.target_ppl << ","
                  << "\"improvement\":" << improvement(row) << ","
                  << "\"guard_status\":\"" << (guard_pass(row.guard, options.max_memory_ratio) ? "pass" : "fail") << "\""
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
        const std::vector<Row> rows = load_rows(options);
        if (options.emit == "markdown") {
            emit_markdown(rows, options);
        } else if (options.emit == "csv") {
            emit_csv(rows, options);
        } else {
            emit_json(rows, options);
        }
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << '\n';
        return 1;
    }
}
