#include <algorithm>
#include <cctype>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Options {
    std::string left_json;
    std::string right_json;
    std::string consensus_json;
    std::string left_method = "loss_sensitive_4to8";
    std::string right_method = "loss_sensitive_4to8";
    std::string consensus_method = "loss_sensitive_consensus_4to8";
    std::string label = "consensus";
    int high_bits = 8;
    std::string emit = "markdown";
};

struct Group {
    std::string module;
    double cost = 1.0;
};

struct Allocation {
    std::string path;
    std::string method;
    double budget_avg_bits = std::numeric_limits<double>::quiet_NaN();
    std::vector<Group> groups;
    std::vector<int> bits;
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

std::size_t find_matching(const std::string& text, std::size_t open_pos, char open_ch, char close_ch) {
    if (open_pos >= text.size() || text[open_pos] != open_ch) {
        throw std::runtime_error("invalid json opener");
    }
    int depth = 1;
    bool in_string = false;
    bool escaped = false;
    for (std::size_t pos = open_pos + 1; pos < text.size(); ++pos) {
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
        } else if (ch == open_ch) {
            ++depth;
        } else if (ch == close_ch) {
            --depth;
            if (depth == 0) {
                return pos;
            }
        }
    }
    throw std::runtime_error("unterminated json value");
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

std::string extract_object_value(const std::string& text, const std::string& key) {
    std::size_t pos = find_json_key(text, key);
    if (pos == std::string::npos) {
        throw std::runtime_error("json missing object: " + key);
    }
    pos = text.find('{', pos);
    if (pos == std::string::npos) {
        throw std::runtime_error("json field is not an object: " + key);
    }
    const std::size_t end = find_matching(text, pos, '{', '}');
    return text.substr(pos, end - pos + 1);
}

std::vector<int> extract_int_array_from_object(const std::string& object, const std::string& key) {
    std::size_t pos = find_json_key(object, key);
    if (pos == std::string::npos) {
        throw std::runtime_error("json missing allocation method: " + key);
    }
    pos = object.find('[', pos);
    if (pos == std::string::npos) {
        throw std::runtime_error("allocation is not an array: " + key);
    }
    const std::size_t end = find_matching(object, pos, '[', ']');
    const std::string array_text = object.substr(pos + 1, end - pos - 1);
    std::vector<int> values;
    std::size_t cursor = 0;
    while (cursor < array_text.size()) {
        cursor = skip_ws(array_text, cursor);
        if (cursor < array_text.size() && array_text[cursor] == ',') {
            ++cursor;
            continue;
        }
        if (cursor >= array_text.size()) break;
        const std::size_t start = cursor;
        if (array_text[cursor] == '-' || array_text[cursor] == '+') ++cursor;
        while (cursor < array_text.size() && std::isdigit(static_cast<unsigned char>(array_text[cursor]))) {
            ++cursor;
        }
        if (cursor == start) {
            throw std::runtime_error("invalid integer array for allocation method: " + key);
        }
        values.push_back(std::stoi(array_text.substr(start, cursor - start)));
    }
    if (values.empty()) {
        throw std::runtime_error("empty allocation array: " + key);
    }
    return values;
}

std::vector<Group> read_groups(const std::string& text) {
    const std::vector<std::string> objects = extract_array_objects(text, "groups");
    std::vector<Group> groups;
    groups.reserve(objects.size());
    for (std::size_t i = 0; i < objects.size(); ++i) {
        Group group;
        group.module = json_string_value(objects[i], "module");
        group.cost = json_number_value(objects[i], "cost", 1.0);
        if (group.module.empty()) {
            throw std::runtime_error("group missing module at index " + std::to_string(i));
        }
        groups.push_back(group);
    }
    return groups;
}

Allocation read_allocation(const std::string& path, const std::string& method) {
    const std::string text = read_text_file(path);
    Allocation allocation;
    allocation.path = path;
    allocation.method = method;
    allocation.budget_avg_bits = json_number_value(text, "budget_avg_bits", std::numeric_limits<double>::quiet_NaN());
    allocation.groups = read_groups(text);
    allocation.bits = extract_int_array_from_object(extract_object_value(text, "allocations"), method);
    if (allocation.groups.size() != allocation.bits.size()) {
        throw std::runtime_error(path + ": groups and allocation length differ");
    }
    return allocation;
}

void verify_same_modules(const Allocation& left, const Allocation& right, const Allocation& consensus) {
    if (left.groups.size() != right.groups.size() || left.groups.size() != consensus.groups.size()) {
        throw std::runtime_error("allocation group counts differ");
    }
    for (std::size_t i = 0; i < left.groups.size(); ++i) {
        if (left.groups[i].module != right.groups[i].module || left.groups[i].module != consensus.groups[i].module) {
            throw std::runtime_error("module order differs at index " + std::to_string(i));
        }
    }
}

std::set<std::string> high_set(const Allocation& allocation, int high_bits) {
    std::set<std::string> out;
    for (std::size_t i = 0; i < allocation.bits.size(); ++i) {
        if (allocation.bits[i] == high_bits) {
            out.insert(allocation.groups[i].module);
        }
    }
    return out;
}

int intersection_size(const std::set<std::string>& a, const std::set<std::string>& b) {
    int count = 0;
    for (const std::string& value : a) {
        if (b.count(value)) ++count;
    }
    return count;
}

int union_size(const std::set<std::string>& a, const std::set<std::string>& b) {
    std::set<std::string> merged = a;
    merged.insert(b.begin(), b.end());
    return static_cast<int>(merged.size());
}

double jaccard(const std::set<std::string>& a, const std::set<std::string>& b) {
    const int uni = union_size(a, b);
    if (uni == 0) return 1.0;
    return static_cast<double>(intersection_size(a, b)) / static_cast<double>(uni);
}

std::map<int, int> bit_hist(const std::vector<int>& bits) {
    std::map<int, int> hist;
    for (int bit : bits) {
        hist[bit] += 1;
    }
    return hist;
}

double weighted_avg_bits(const Allocation& allocation) {
    double memory = 0.0;
    double cost = 0.0;
    for (std::size_t i = 0; i < allocation.bits.size(); ++i) {
        memory += allocation.groups[i].cost * static_cast<double>(allocation.bits[i]);
        cost += allocation.groups[i].cost;
    }
    return memory / std::max(cost, 1.0e-12);
}

double budget_used(const Allocation& allocation) {
    if (!std::isfinite(allocation.budget_avg_bits)) return std::numeric_limits<double>::quiet_NaN();
    return weighted_avg_bits(allocation) / std::max(allocation.budget_avg_bits, 1.0e-12);
}

std::string format_hist(const std::map<int, int>& hist) {
    std::ostringstream out;
    bool first = true;
    out << "{";
    for (const auto& item : hist) {
        if (!first) out << ", ";
        first = false;
        out << item.first << ": " << item.second;
    }
    out << "}";
    return out.str();
}

void print_markdown(const Options& options, const Allocation& left, const Allocation& right, const Allocation& consensus) {
    const std::set<std::string> left_high = high_set(left, options.high_bits);
    const std::set<std::string> right_high = high_set(right, options.high_bits);
    const std::set<std::string> consensus_high = high_set(consensus, options.high_bits);

    std::cout << "# Quant Consensus Audit\n\n";
    std::cout << "Label: `" << options.label << "`\n\n";
    std::cout << "High bits: `" << options.high_bits << "`\n\n";
    std::cout << "## Inputs\n\n";
    std::cout << "| role | path | method |\n";
    std::cout << "|---|---|---|\n";
    std::cout << "| left | `" << left.path << "` | `" << left.method << "` |\n";
    std::cout << "| right | `" << right.path << "` | `" << right.method << "` |\n";
    std::cout << "| consensus | `" << consensus.path << "` | `" << consensus.method << "` |\n\n";

    std::cout << "## Allocation Summary\n\n";
    std::cout << "| allocation | modules | avg bits | budget used | bit histogram | high-count |\n";
    std::cout << "|---|---:|---:|---:|---|---:|\n";
    const auto print_row = [](const std::string& name, const Allocation& allocation, int high_count) {
        std::cout << "| `" << name << "` | " << allocation.bits.size() << " | " << std::fixed << std::setprecision(4)
                  << weighted_avg_bits(allocation) << " | ";
        const double used = budget_used(allocation);
        if (std::isfinite(used)) {
            std::cout << std::fixed << std::setprecision(4) << used;
        } else {
            std::cout << "NA";
        }
        std::cout << " | `" << format_hist(bit_hist(allocation.bits)) << "` | " << high_count << " |\n";
    };
    print_row("left", left, static_cast<int>(left_high.size()));
    print_row("right", right, static_cast<int>(right_high.size()));
    print_row("consensus", consensus, static_cast<int>(consensus_high.size()));

    std::cout << "\n## Overlap\n\n";
    std::cout << "| pair | intersection | union | Jaccard |\n";
    std::cout << "|---|---:|---:|---:|\n";
    const auto print_overlap = [](const std::string& name, const std::set<std::string>& a,
                                  const std::set<std::string>& b) {
        std::cout << "| `" << name << "` | " << intersection_size(a, b) << " | " << union_size(a, b) << " | "
                  << std::fixed << std::setprecision(4) << jaccard(a, b) << " |\n";
    };
    print_overlap("left/right", left_high, right_high);
    print_overlap("left/consensus", left_high, consensus_high);
    print_overlap("right/consensus", right_high, consensus_high);

    std::cout << "\nPositive Jaccard/overlap only describes allocation stability. It does not prove downstream quality; "
                 "read it with PPL evidence.\n";
}

void print_csv(const Options& options, const Allocation& left, const Allocation& right, const Allocation& consensus) {
    const std::set<std::string> left_high = high_set(left, options.high_bits);
    const std::set<std::string> right_high = high_set(right, options.high_bits);
    const std::set<std::string> consensus_high = high_set(consensus, options.high_bits);
    std::cout << "label,pair,intersection,union,jaccard,left_high,right_high,consensus_high,consensus_avg_bits,"
                 "consensus_budget_used\n";
    std::cout << std::fixed << std::setprecision(6);
    const auto print_pair = [&](const std::string& pair, const std::set<std::string>& a, const std::set<std::string>& b) {
        std::cout << options.label << "," << pair << "," << intersection_size(a, b) << "," << union_size(a, b)
                  << "," << jaccard(a, b) << "," << left_high.size() << "," << right_high.size() << ","
                  << consensus_high.size() << "," << weighted_avg_bits(consensus) << ",";
        const double used = budget_used(consensus);
        if (std::isfinite(used)) {
            std::cout << used;
        }
        std::cout << "\n";
    };
    print_pair("left/right", left_high, right_high);
    print_pair("left/consensus", left_high, consensus_high);
    print_pair("right/consensus", right_high, consensus_high);
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
        if (arg == "--left") {
            options.left_json = require_value("--left");
        } else if (arg == "--right") {
            options.right_json = require_value("--right");
        } else if (arg == "--consensus") {
            options.consensus_json = require_value("--consensus");
        } else if (arg == "--left-method") {
            options.left_method = require_value("--left-method");
        } else if (arg == "--right-method") {
            options.right_method = require_value("--right-method");
        } else if (arg == "--consensus-method") {
            options.consensus_method = require_value("--consensus-method");
        } else if (arg == "--label") {
            options.label = require_value("--label");
        } else if (arg == "--high-bits") {
            options.high_bits = std::stoi(require_value("--high-bits"));
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_consensus_audit --left alloc.json --right alloc.json --consensus alloc.json\n"
                         "                             [--left-method loss_sensitive_4to8]\n"
                         "                             [--right-method loss_sensitive_4to8]\n"
                         "                             [--consensus-method loss_sensitive_consensus_4to8]\n"
                         "                             [--high-bits 8] [--label name] [--emit markdown|csv]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.left_json.empty() || options.right_json.empty() || options.consensus_json.empty()) {
        throw std::runtime_error("--left, --right, and --consensus are required");
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
        const Allocation left = read_allocation(options.left_json, options.left_method);
        const Allocation right = read_allocation(options.right_json, options.right_method);
        const Allocation consensus = read_allocation(options.consensus_json, options.consensus_method);
        verify_same_modules(left, right, consensus);
        if (options.emit == "csv") {
            print_csv(options, left, right, consensus);
        } else {
            print_markdown(options, left, right, consensus);
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << "\n";
        return 1;
    }
}
