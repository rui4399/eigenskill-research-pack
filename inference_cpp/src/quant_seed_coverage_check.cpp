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
    std::vector<std::string> inputs;
    std::string prefix = "random_budget_seed_";
    int start_seed = 0;
    int end_seed = -1;
    std::vector<std::string> required_names;
    std::string emit = "markdown";
};

struct SeenName {
    std::string name;
    std::string source;
};

struct Report {
    std::vector<SeenName> all_names;
    std::map<std::string, std::vector<std::string>> name_sources;
    std::vector<std::string> missing_seed_names;
    std::vector<std::string> duplicate_seed_names;
    std::vector<std::string> out_of_range_seed_names;
    std::vector<std::string> missing_required_names;
    int expected_seed_count = 0;
    int matched_seed_count = 0;
    bool pass = false;
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

std::vector<std::string> extract_array_objects_at(std::string const& text, std::size_t array_pos) {
    if (array_pos == std::string::npos || array_pos >= text.size() || text[array_pos] != '[') {
        throw std::runtime_error("json field is not an array");
    }
    std::vector<std::string> objects;
    int bracket_depth = 1;
    int object_depth = 0;
    bool in_string = false;
    bool escaped = false;
    std::size_t object_start = std::string::npos;
    for (std::size_t pos = array_pos + 1; pos < text.size(); ++pos) {
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
        throw std::runtime_error("array contains no objects");
    }
    return objects;
}

std::vector<std::string> extract_named_objects(const std::string& text) {
    std::size_t pos = find_json_key(text, "results");
    if (pos != std::string::npos) {
        pos = text.find('[', pos);
        return extract_array_objects_at(text, pos);
    }
    pos = skip_ws(text, 0);
    if (pos < text.size() && text[pos] == '[') {
        return extract_array_objects_at(text, pos);
    }
    throw std::runtime_error("expected a top-level array or an object with a results array");
}

bool starts_with(const std::string& value, const std::string& prefix) {
    return value.size() >= prefix.size() && std::equal(prefix.begin(), prefix.end(), value.begin());
}

int parse_seed(const std::string& name, const std::string& prefix) {
    if (!starts_with(name, prefix)) return -1;
    const std::string suffix = name.substr(prefix.size());
    if (suffix.empty()) return -1;
    for (const char ch : suffix) {
        if (!std::isdigit(static_cast<unsigned char>(ch))) return -1;
    }
    return std::stoi(suffix);
}

std::string seed_name(const std::string& prefix, int seed) {
    return prefix + std::to_string(seed);
}

std::vector<SeenName> load_names(const std::vector<std::string>& inputs) {
    std::vector<SeenName> names;
    for (const std::string& input : inputs) {
        const std::string text = read_text_file(input);
        const std::vector<std::string> objects = extract_named_objects(text);
        for (const std::string& object : objects) {
            const std::string name = json_string_value(object, "name");
            if (!name.empty()) {
                names.push_back(SeenName{name, input});
            }
        }
    }
    return names;
}

Report build_report(const Options& options) {
    Report report;
    report.expected_seed_count = options.end_seed - options.start_seed + 1;
    if (report.expected_seed_count <= 0) {
        throw std::runtime_error("--end must be greater than or equal to --start");
    }

    report.all_names = load_names(options.inputs);
    for (const SeenName& seen : report.all_names) {
        report.name_sources[seen.name].push_back(seen.source);
    }

    for (int seed = options.start_seed; seed <= options.end_seed; ++seed) {
        const std::string expected = seed_name(options.prefix, seed);
        const auto it = report.name_sources.find(expected);
        if (it == report.name_sources.end()) {
            report.missing_seed_names.push_back(expected);
        } else {
            ++report.matched_seed_count;
            if (it->second.size() > 1) {
                report.duplicate_seed_names.push_back(expected);
            }
        }
    }

    for (const auto& [name, sources] : report.name_sources) {
        const int seed = parse_seed(name, options.prefix);
        if (seed < 0) continue;
        if (seed < options.start_seed || seed > options.end_seed) {
            report.out_of_range_seed_names.push_back(name);
        }
    }

    for (const std::string& required : options.required_names) {
        if (report.name_sources.find(required) == report.name_sources.end()) {
            report.missing_required_names.push_back(required);
        }
    }

    report.pass = report.missing_seed_names.empty() && report.duplicate_seed_names.empty() &&
                  report.out_of_range_seed_names.empty() && report.missing_required_names.empty();
    return report;
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

void print_json_string_array(const std::vector<std::string>& values) {
    std::cout << "[";
    for (std::size_t i = 0; i < values.size(); ++i) {
        if (i > 0) std::cout << ", ";
        std::cout << "\"" << json_escape(values[i]) << "\"";
    }
    std::cout << "]";
}

void emit_json(const Report& report) {
    std::cout << "{\n";
    std::cout << "  \"pass\": " << (report.pass ? "true" : "false") << ",\n";
    std::cout << "  \"expected_seed_count\": " << report.expected_seed_count << ",\n";
    std::cout << "  \"matched_seed_count\": " << report.matched_seed_count << ",\n";
    std::cout << "  \"missing_seed_names\": ";
    print_json_string_array(report.missing_seed_names);
    std::cout << ",\n";
    std::cout << "  \"duplicate_seed_names\": ";
    print_json_string_array(report.duplicate_seed_names);
    std::cout << ",\n";
    std::cout << "  \"out_of_range_seed_names\": ";
    print_json_string_array(report.out_of_range_seed_names);
    std::cout << ",\n";
    std::cout << "  \"missing_required_names\": ";
    print_json_string_array(report.missing_required_names);
    std::cout << "\n";
    std::cout << "}\n";
}

void emit_csv(const Report& report) {
    std::cout << "pass,expected_seed_count,matched_seed_count,missing_count,duplicate_count,out_of_range_count,missing_required_count\n";
    std::cout << (report.pass ? "true" : "false") << ','
              << report.expected_seed_count << ','
              << report.matched_seed_count << ','
              << report.missing_seed_names.size() << ','
              << report.duplicate_seed_names.size() << ','
              << report.out_of_range_seed_names.size() << ','
              << report.missing_required_names.size() << '\n';
}

void print_list(const std::string& label, const std::vector<std::string>& values) {
    std::cout << "- " << label << ": ";
    if (values.empty()) {
        std::cout << "none\n";
        return;
    }
    for (std::size_t i = 0; i < values.size(); ++i) {
        if (i > 0) std::cout << ", ";
        std::cout << "`" << values[i] << "`";
    }
    std::cout << "\n";
}

void emit_markdown(const Report& report) {
    std::cout << "# Quant Seed Coverage Check\n\n";
    std::cout << "| status | expected seeds | matched seeds | missing | duplicates | out-of-range | missing required |\n";
    std::cout << "|---|---:|---:|---:|---:|---:|---:|\n";
    std::cout << "| " << (report.pass ? "pass" : "fail")
              << " | " << report.expected_seed_count
              << " | " << report.matched_seed_count
              << " | " << report.missing_seed_names.size()
              << " | " << report.duplicate_seed_names.size()
              << " | " << report.out_of_range_seed_names.size()
              << " | " << report.missing_required_names.size()
              << " |\n\n";
    print_list("missing seeds", report.missing_seed_names);
    print_list("duplicate seeds", report.duplicate_seed_names);
    print_list("out-of-range seeds", report.out_of_range_seed_names);
    print_list("missing required names", report.missing_required_names);
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
            options.inputs.push_back(require_value("--input"));
        } else if (arg == "--prefix") {
            options.prefix = require_value("--prefix");
        } else if (arg == "--start") {
            options.start_seed = std::stoi(require_value("--start"));
        } else if (arg == "--end") {
            options.end_seed = std::stoi(require_value("--end"));
        } else if (arg == "--require-name") {
            options.required_names.push_back(require_value("--require-name"));
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_seed_coverage_check --input config_or_summary.json [--input ...]\n"
                      << "                                 --prefix random_budget_seed_ --start 20260604 --end 20260619\n"
                      << "                                 [--require-name fp16] [--emit markdown|csv|json]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.inputs.empty()) {
        throw std::runtime_error("at least one --input is required");
    }
    if (options.prefix.empty()) {
        throw std::runtime_error("--prefix must be non-empty");
    }
    if (options.end_seed < options.start_seed) {
        throw std::runtime_error("--end must be greater than or equal to --start");
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
        const Report report = build_report(options);
        if (options.emit == "json") {
            emit_json(report);
        } else if (options.emit == "csv") {
            emit_csv(report);
        } else {
            emit_markdown(report);
        }
        return report.pass ? 0 : 2;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << "\n";
        return 1;
    }
}
