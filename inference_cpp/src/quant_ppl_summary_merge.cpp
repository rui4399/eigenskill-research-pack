#include <algorithm>
#include <cmath>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

namespace fs = std::filesystem;

struct Options {
    std::vector<std::string> inputs;
    std::string out = "-";
    double duplicate_ppl_tolerance = 1.0e-6;
};

struct ResultObject {
    std::string name;
    double ppl = std::numeric_limits<double>::quiet_NaN();
    std::string raw;
    std::string source;
};

struct SummaryFile {
    std::string path;
    std::string model;
    int prompt_count = 0;
    int max_length = 0;
    std::string device;
    std::string dtype;
    std::vector<ResultObject> results;
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

void write_text_file(const std::string& path, const std::string& text) {
    if (path == "-") {
        std::cout << text;
        return;
    }
    const fs::path out(path);
    if (!out.parent_path().empty()) {
        fs::create_directories(out.parent_path());
    }
    std::ofstream file(path);
    if (!file) {
        throw std::runtime_error("could not write file: " + path);
    }
    file << text;
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

std::string compact_json(const std::string& text) {
    std::string out;
    out.reserve(text.size());
    bool in_string = false;
    bool escaped = false;
    for (const char ch : text) {
        if (in_string) {
            out.push_back(ch);
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
            out.push_back(ch);
        } else if (!std::isspace(static_cast<unsigned char>(ch))) {
            out.push_back(ch);
        }
    }
    return out;
}

SummaryFile load_summary(const std::string& path) {
    const std::string text = read_text_file(path);
    SummaryFile summary;
    summary.path = path;
    summary.model = json_string_value(text, "model");
    summary.prompt_count = static_cast<int>(json_number_value(text, "prompt_count", -1));
    summary.max_length = static_cast<int>(json_number_value(text, "max_length", -1));
    summary.device = json_string_value(text, "device");
    summary.dtype = json_string_value(text, "dtype");
    if (summary.model.empty() || summary.prompt_count < 0 || summary.max_length < 0 ||
        summary.device.empty() || summary.dtype.empty()) {
        throw std::runtime_error("invalid summary header: " + path);
    }

    const std::vector<std::string> objects = extract_array_objects(text, "results");
    summary.results.reserve(objects.size());
    for (const std::string& object : objects) {
        ResultObject result;
        result.name = json_string_value(object, "name");
        const std::size_t metrics_pos = find_json_key(object, "metrics");
        const std::string metrics_object = metrics_pos == std::string::npos ? object : object.substr(metrics_pos);
        result.ppl = json_number_value(metrics_object, "ppl", std::numeric_limits<double>::quiet_NaN());
        result.raw = compact_json(object);
        result.source = path;
        if (result.name.empty() || !std::isfinite(result.ppl)) {
            throw std::runtime_error("invalid result object in " + path);
        }
        summary.results.push_back(result);
    }
    return summary;
}

void require_same_header(const SummaryFile& base, const SummaryFile& other) {
    if (base.model != other.model) {
        throw std::runtime_error("model mismatch: " + base.path + " vs " + other.path);
    }
    if (base.prompt_count != other.prompt_count) {
        throw std::runtime_error("prompt_count mismatch: " + base.path + " vs " + other.path);
    }
    if (base.max_length != other.max_length) {
        throw std::runtime_error("max_length mismatch: " + base.path + " vs " + other.path);
    }
    if (base.device != other.device) {
        throw std::runtime_error("device mismatch: " + base.path + " vs " + other.path);
    }
    if (base.dtype != other.dtype) {
        throw std::runtime_error("dtype mismatch: " + base.path + " vs " + other.path);
    }
}

std::vector<ResultObject> merge_results(const std::vector<SummaryFile>& summaries, double tolerance) {
    std::vector<ResultObject> merged;
    std::map<std::string, std::size_t> seen;
    for (const SummaryFile& summary : summaries) {
        for (const ResultObject& result : summary.results) {
            const auto it = seen.find(result.name);
            if (it == seen.end()) {
                seen[result.name] = merged.size();
                merged.push_back(result);
                continue;
            }
            const ResultObject& previous = merged[it->second];
            if (std::fabs(previous.ppl - result.ppl) > tolerance) {
                std::ostringstream msg;
                msg << "duplicate result has conflicting PPL: " << result.name << " "
                    << previous.ppl << " from " << previous.source << " vs "
                    << result.ppl << " from " << result.source;
                throw std::runtime_error(msg.str());
            }
        }
    }
    return merged;
}

std::string build_output_json(
    const SummaryFile& base,
    const std::vector<SummaryFile>& summaries,
    const std::vector<ResultObject>& merged) {
    std::ostringstream out;
    out << "{\n";
    out << "  \"model\": \"" << json_escape(base.model) << "\",\n";
    out << "  \"prompt_count\": " << base.prompt_count << ",\n";
    out << "  \"max_length\": " << base.max_length << ",\n";
    out << "  \"device\": \"" << json_escape(base.device) << "\",\n";
    out << "  \"dtype\": \"" << json_escape(base.dtype) << "\",\n";
    out << "  \"results\": [\n";
    for (std::size_t i = 0; i < merged.size(); ++i) {
        out << "    " << merged[i].raw;
        if (i + 1 != merged.size()) out << ",";
        out << "\n";
    }
    out << "  ],\n";
    out << "  \"merge_meta\": {\n";
    out << "    \"source_count\": " << summaries.size() << ",\n";
    out << "    \"result_count\": " << merged.size() << ",\n";
    out << "    \"sources\": [\n";
    for (std::size_t i = 0; i < summaries.size(); ++i) {
        out << "      \"" << json_escape(summaries[i].path) << "\"";
        if (i + 1 != summaries.size()) out << ",";
        out << "\n";
    }
    out << "    ]\n";
    out << "  }\n";
    out << "}\n";
    return out.str();
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
        } else if (arg == "--out") {
            options.out = require_value("--out");
        } else if (arg == "--duplicate-ppl-tolerance") {
            options.duplicate_ppl_tolerance = std::stod(require_value("--duplicate-ppl-tolerance"));
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_ppl_summary_merge --input batch0.json --input batch1.json [--out merged.json]\n"
                      << "                               [--duplicate-ppl-tolerance 1e-6]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.inputs.size() < 2) {
        throw std::runtime_error("at least two --input files are required");
    }
    if (options.duplicate_ppl_tolerance < 0.0) {
        throw std::runtime_error("--duplicate-ppl-tolerance must be non-negative");
    }
    return options;
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        std::vector<SummaryFile> summaries;
        summaries.reserve(options.inputs.size());
        for (const std::string& input : options.inputs) {
            summaries.push_back(load_summary(input));
            if (summaries.size() > 1) {
                require_same_header(summaries.front(), summaries.back());
            }
        }
        const std::vector<ResultObject> merged = merge_results(summaries, options.duplicate_ppl_tolerance);
        write_text_file(options.out, build_output_json(summaries.front(), summaries, merged));
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << "\n";
        return 1;
    }
}
