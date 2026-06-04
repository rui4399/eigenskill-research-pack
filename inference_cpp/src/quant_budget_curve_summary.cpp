#include <algorithm>
#include <cctype>
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

struct CaseInput {
    std::string dataset;
    std::string path;
};

struct Options {
    std::vector<CaseInput> inputs;
    std::string out_json = "outputs/consensus_budget_curve_summary.json";
    std::string out_csv = "outputs/consensus_budget_curve_summary.csv";
    std::string out_md = "outputs/consensus_budget_curve_report.md";
    std::string out_svg = "outputs/consensus_budget_curve.svg";
    std::string emit = "";
    bool no_write = false;
};

struct ResultItem {
    std::string name;
    double ppl = std::numeric_limits<double>::quiet_NaN();
    double delta_nll_vs_fp16 = 0.0;
    double avg_bits = 0.0;
    std::string bit_hist = "{}";
};

struct Row {
    std::string dataset;
    std::string model;
    int prompt_count = 0;
    std::string config;
    double avg_bits = 0.0;
    double ppl = 0.0;
    double delta_nll_vs_fp16 = 0.0;
    double ppl_improvement_vs_uniform = 0.0;
    double uniform_gap_closed_ratio = 0.0;
    std::string bit_hist = "{}";
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

bool starts_with(const std::string& value, const std::string& prefix) {
    return value.size() >= prefix.size() && std::equal(prefix.begin(), prefix.end(), value.begin());
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

std::string extract_object_value_optional(const std::string& text, const std::string& key) {
    std::size_t pos = find_json_key(text, key);
    if (pos == std::string::npos) return "";
    pos = text.find('{', pos);
    if (pos == std::string::npos) return "";
    const std::size_t end = find_matching(text, pos, '{', '}');
    return text.substr(pos, end - pos + 1);
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
    return out.empty() ? "{}" : out;
}

std::string json_escape(const std::string& value) {
    std::string out;
    for (const char ch : value) {
        switch (ch) {
            case '\\': out += "\\\\"; break;
            case '"': out += "\\\""; break;
            case '\n': out += "\\n"; break;
            case '\r': out += "\\r"; break;
            case '\t': out += "\\t"; break;
            default: out.push_back(ch); break;
        }
    }
    return out;
}

std::string csv_escape(const std::string& value) {
    bool needs_quotes = false;
    for (const char ch : value) {
        if (ch == ',' || ch == '"' || ch == '\n' || ch == '\r') {
            needs_quotes = true;
            break;
        }
    }
    if (!needs_quotes) return value;
    std::string out = "\"";
    for (const char ch : value) {
        if (ch == '"') out += "\"\"";
        else out.push_back(ch);
    }
    out += '"';
    return out;
}

std::string xml_escape(const std::string& value) {
    std::string out;
    for (const char ch : value) {
        switch (ch) {
            case '&': out += "&amp;"; break;
            case '<': out += "&lt;"; break;
            case '>': out += "&gt;"; break;
            case '"': out += "&quot;"; break;
            default: out.push_back(ch); break;
        }
    }
    return out;
}

std::string format_fixed(double value, int precision) {
    if (!std::isfinite(value)) return "NA";
    std::ostringstream ss;
    ss << std::fixed << std::setprecision(precision) << value;
    return ss.str();
}

double parse_budget_from_name(const std::string& name) {
    const std::string prefix = "consensus_budget_";
    if (!starts_with(name, prefix)) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    std::string suffix = name.substr(prefix.size());
    std::replace(suffix.begin(), suffix.end(), 'p', '.');
    try {
        return std::stod(suffix);
    } catch (const std::exception&) {
        return std::numeric_limits<double>::quiet_NaN();
    }
}

double plot_budget_for_config(const Row& row) {
    if (row.config == "uniform_int4") return 4.0;
    const double parsed = parse_budget_from_name(row.config);
    if (std::isfinite(parsed)) return parsed;
    return std::numeric_limits<double>::quiet_NaN();
}

std::vector<ResultItem> read_result_items(const std::string& path) {
    const std::string text = read_text_file(path);
    const std::vector<std::string> objects = extract_array_objects(text, "results");
    std::vector<ResultItem> items;
    items.reserve(objects.size());
    for (const std::string& object : objects) {
        ResultItem item;
        item.name = json_string_value(object, "name");
        const std::string metrics = extract_object_value_optional(object, "metrics");
        item.ppl = json_number_value(metrics.empty() ? object : metrics, "ppl", std::numeric_limits<double>::quiet_NaN());
        item.delta_nll_vs_fp16 = json_number_value(object, "delta_nll_vs_fp16", 0.0);

        if (item.name == "fp16") {
            item.avg_bits = 16.0;
        } else if (item.name == "uniform_int4") {
            item.avg_bits = 4.0;
        } else {
            const std::string summary = extract_object_value_optional(object, "allocation_summary");
            item.avg_bits = json_number_value(summary, "avg_bits", 0.0);
            if (item.avg_bits <= 0.0) {
                const double parsed = parse_budget_from_name(item.name);
                if (std::isfinite(parsed)) item.avg_bits = parsed;
            }
        }

        const std::string quant_meta = extract_object_value_optional(object, "quant_meta");
        const std::string bit_hist = extract_object_value_optional(quant_meta, "bit_hist");
        item.bit_hist = bit_hist.empty() ? "{}" : compact_json(bit_hist);

        if (item.name.empty() || !std::isfinite(item.ppl)) {
            throw std::runtime_error("invalid result object in " + path);
        }
        items.push_back(item);
    }
    return items;
}

double find_required_ppl(const std::vector<ResultItem>& items, const std::string& name, const std::string& path) {
    for (const ResultItem& item : items) {
        if (item.name == name) return item.ppl;
    }
    throw std::runtime_error("missing result '" + name + "' in " + path);
}

std::vector<Row> load_case_rows(const CaseInput& input) {
    const std::string text = read_text_file(input.path);
    const std::vector<ResultItem> items = read_result_items(input.path);
    const double fp16_ppl = find_required_ppl(items, "fp16", input.path);
    const double uniform_ppl = find_required_ppl(items, "uniform_int4", input.path);
    const double uniform_gap = std::max(uniform_ppl - fp16_ppl, 1.0e-12);

    std::vector<Row> rows;
    rows.reserve(items.size());
    for (const ResultItem& item : items) {
        Row row;
        row.dataset = input.dataset;
        row.model = json_string_value(text, "model");
        row.prompt_count = static_cast<int>(json_number_value(text, "prompt_count", 0.0));
        row.config = item.name;
        row.avg_bits = item.avg_bits;
        row.ppl = item.ppl;
        row.delta_nll_vs_fp16 = item.delta_nll_vs_fp16;
        row.ppl_improvement_vs_uniform = uniform_ppl - item.ppl;
        row.uniform_gap_closed_ratio = (uniform_ppl - item.ppl) / uniform_gap;
        row.bit_hist = item.bit_hist;
        rows.push_back(row);
    }
    return rows;
}

std::vector<Row> load_all_rows(const std::vector<CaseInput>& inputs) {
    std::vector<Row> rows;
    for (const CaseInput& input : inputs) {
        const std::vector<Row> case_rows = load_case_rows(input);
        rows.insert(rows.end(), case_rows.begin(), case_rows.end());
    }
    return rows;
}

std::string render_csv(const std::vector<Row>& rows) {
    std::ostringstream out;
    out << "dataset,model,prompt_count,config,avg_bits,ppl,delta_nll_vs_fp16,"
           "ppl_improvement_vs_uniform,uniform_gap_closed_ratio,bit_hist\n";
    out << std::setprecision(12);
    for (const Row& row : rows) {
        out << csv_escape(row.dataset) << ','
            << csv_escape(row.model) << ','
            << row.prompt_count << ','
            << csv_escape(row.config) << ','
            << row.avg_bits << ','
            << row.ppl << ','
            << row.delta_nll_vs_fp16 << ','
            << row.ppl_improvement_vs_uniform << ','
            << row.uniform_gap_closed_ratio << ','
            << csv_escape(row.bit_hist) << '\n';
    }
    return out.str();
}

std::string render_json(const std::vector<Row>& rows) {
    std::ostringstream out;
    out << "{\n  \"rows\": [\n";
    out << std::setprecision(12);
    for (std::size_t i = 0; i < rows.size(); ++i) {
        const Row& row = rows[i];
        out << "    {\n"
            << "      \"dataset\": \"" << json_escape(row.dataset) << "\",\n"
            << "      \"model\": \"" << json_escape(row.model) << "\",\n"
            << "      \"prompt_count\": " << row.prompt_count << ",\n"
            << "      \"config\": \"" << json_escape(row.config) << "\",\n"
            << "      \"avg_bits\": " << row.avg_bits << ",\n"
            << "      \"ppl\": " << row.ppl << ",\n"
            << "      \"delta_nll_vs_fp16\": " << row.delta_nll_vs_fp16 << ",\n"
            << "      \"ppl_improvement_vs_uniform\": " << row.ppl_improvement_vs_uniform << ",\n"
            << "      \"uniform_gap_closed_ratio\": " << row.uniform_gap_closed_ratio << ",\n"
            << "      \"bit_hist\": \"" << json_escape(row.bit_hist) << "\"\n"
            << "    }" << (i + 1 == rows.size() ? "\n" : ",\n");
    }
    out << "  ]\n}\n";
    return out.str();
}

std::string render_markdown(const std::vector<Row>& rows) {
    std::ostringstream out;
    out << "# Consensus Budget Curve\n\n";
    out << "This table evaluates the same cross-dataset consensus allocator at multiple\n";
    out << "average-bit budgets. It is a short-slice PyTorch fake-quant diagnostic,\n";
    out << "not a packed runtime or hardware result.\n\n";
    out << "| dataset | model | config | avg bits | PPL | PPL gain vs uniform INT4 | uniform gap closed | bit hist |\n";
    out << "|---|---|---|---:|---:|---:|---:|---|\n";
    for (const Row& row : rows) {
        out << "| " << row.dataset << " | `" << row.model << "` | `" << row.config << "` | "
            << format_fixed(row.avg_bits, 4) << " | " << format_fixed(row.ppl, 4) << " | "
            << format_fixed(row.ppl_improvement_vs_uniform, 4) << " | "
            << format_fixed(row.uniform_gap_closed_ratio, 4) << " | `"
            << row.bit_hist << "` |\n";
    }
    out << "\n## Interpretation\n\n";
    out << "A useful allocation curve should improve as more high-precision budget is\n";
    out << "released. Non-monotonic points should be treated as calibration noise or\n";
    out << "module-interaction evidence rather than hidden as failed runs.\n";
    return out.str();
}

std::string svg_fmt(double value) {
    std::ostringstream ss;
    ss << std::fixed << std::setprecision(2) << value;
    return ss.str();
}

std::string label_fmt(double value) {
    std::ostringstream ss;
    if (std::fabs(value) >= 10.0) {
        ss << std::fixed << std::setprecision(1) << value;
    } else {
        ss << std::fixed << std::setprecision(2) << value;
    }
    return ss.str();
}

std::vector<std::string> ordered_datasets(const std::vector<Row>& rows) {
    std::vector<std::string> names;
    for (const Row& row : rows) {
        if (std::find(names.begin(), names.end(), row.dataset) == names.end()) {
            names.push_back(row.dataset);
        }
    }
    return names;
}

std::string render_svg(const std::vector<Row>& rows) {
    const std::vector<std::string> datasets = ordered_datasets(rows);
    const int panel_w = 360;
    const int panel_h = 250;
    const int cols = 2;
    const int row_count = static_cast<int>((datasets.size() + cols - 1) / cols);
    const int width = cols * panel_w + 80;
    const int height = row_count * panel_h + 90;
    const int margin_l = 58;
    const int margin_t = 48;
    const int plot_w = 250;
    const int plot_h = 150;

    std::ostringstream out;
    out << "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"" << width << "\" height=\"" << height
        << "\" viewBox=\"0 0 " << width << ' ' << height << "\">\n";
    out << "<style>text{font-family:Arial,Helvetica,sans-serif}.title{font-size:18px;font-weight:700}.label{font-size:11px}.small{font-size:10px}</style>\n";
    out << "<rect width=\"" << width << "\" height=\"" << height << "\" fill=\"#ffffff\"/>\n";
    out << "<text x=\"40\" y=\"30\" class=\"title\" fill=\"#111827\">Consensus budget curve, fake-quant PPL</text>\n";

    for (std::size_t idx = 0; idx < datasets.size(); ++idx) {
        const std::string& dataset = datasets[idx];
        std::vector<Row> data;
        for (const Row& row : rows) {
            if (row.dataset == dataset) data.push_back(row);
        }
        auto fp16_it = std::find_if(data.begin(), data.end(), [](const Row& row) { return row.config == "fp16"; });
        if (fp16_it == data.end()) continue;
        std::vector<Row> curve;
        for (const Row& row : data) {
            if (std::isfinite(plot_budget_for_config(row))) curve.push_back(row);
        }
        if (curve.empty()) continue;
        std::sort(curve.begin(), curve.end(), [](const Row& a, const Row& b) {
            return plot_budget_for_config(a) < plot_budget_for_config(b);
        });

        std::vector<double> ppls;
        std::vector<double> budgets;
        ppls.push_back(fp16_it->ppl);
        for (const Row& row : curve) {
            ppls.push_back(row.ppl);
            budgets.push_back(plot_budget_for_config(row));
        }
        double y_min = *std::min_element(ppls.begin(), ppls.end()) * 0.96;
        double y_max = *std::max_element(ppls.begin(), ppls.end()) * 1.04;
        if (y_max <= y_min) y_max = y_min + 1.0;
        double x_min = *std::min_element(budgets.begin(), budgets.end());
        double x_max = *std::max_element(budgets.begin(), budgets.end());
        if (x_max <= x_min) x_max = x_min + 1.0;

        const int col = static_cast<int>(idx % cols);
        const int row_i = static_cast<int>(idx / cols);
        const int x0 = 40 + col * panel_w;
        const int y0 = 55 + row_i * panel_h;
        const auto sx = [&](double avg_bits) {
            return x0 + margin_l + (avg_bits - x_min) / (x_max - x_min) * plot_w;
        };
        const auto sy = [&](double ppl) {
            return y0 + margin_t + (y_max - ppl) / (y_max - y_min) * plot_h;
        };

        out << "<text x=\"" << (x0 + margin_l) << "\" y=\"" << (y0 + 20)
            << "\" class=\"label\" font-weight=\"700\" fill=\"#1f2933\">" << xml_escape(dataset) << "</text>\n";
        out << "<rect x=\"" << (x0 + margin_l) << "\" y=\"" << (y0 + margin_t)
            << "\" width=\"" << plot_w << "\" height=\"" << plot_h
            << "\" fill=\"#fbfcfd\" stroke=\"#d8dde3\"/>\n";

        const double y_ticks[3] = {y_min, (y_min + y_max) * 0.5, y_max};
        for (const double tick : y_ticks) {
            const double y = sy(tick);
            out << "<line x1=\"" << (x0 + margin_l) << "\" y1=\"" << svg_fmt(y)
                << "\" x2=\"" << (x0 + margin_l + plot_w) << "\" y2=\"" << svg_fmt(y)
                << "\" stroke=\"#d8dde3\" stroke-width=\"1\"/>\n";
            out << "<text x=\"" << (x0 + margin_l - 8) << "\" y=\"" << svg_fmt(y + 3)
                << "\" text-anchor=\"end\" class=\"small\" fill=\"#1f2933\">" << label_fmt(tick) << "</text>\n";
        }

        std::vector<double> ticks = budgets;
        std::sort(ticks.begin(), ticks.end());
        ticks.erase(std::unique(ticks.begin(), ticks.end(), [](double a, double b) { return std::fabs(a - b) < 1.0e-9; }), ticks.end());
        for (const double tick : ticks) {
            const double x = sx(tick);
            out << "<line x1=\"" << svg_fmt(x) << "\" y1=\"" << (y0 + margin_t)
                << "\" x2=\"" << svg_fmt(x) << "\" y2=\"" << (y0 + margin_t + plot_h)
                << "\" stroke=\"#d8dde3\" stroke-width=\"1\"/>\n";
            out << "<text x=\"" << svg_fmt(x) << "\" y=\"" << (y0 + margin_t + plot_h + 18)
                << "\" text-anchor=\"middle\" class=\"small\" fill=\"#1f2933\">" << format_fixed(tick, 2) << "</text>\n";
        }

        const double fp16_y = sy(fp16_it->ppl);
        out << "<line x1=\"" << (x0 + margin_l) << "\" y1=\"" << svg_fmt(fp16_y)
            << "\" x2=\"" << (x0 + margin_l + plot_w) << "\" y2=\"" << svg_fmt(fp16_y)
            << "\" stroke=\"#2ca25f\" stroke-width=\"1.5\" stroke-dasharray=\"4 3\"/>\n";
        out << "<text x=\"" << (x0 + margin_l + plot_w + 6) << "\" y=\"" << svg_fmt(fp16_y + 3)
            << "\" class=\"small\" fill=\"#2ca25f\">FP16</text>\n";

        out << "<path d=\"";
        for (std::size_t point = 0; point < curve.size(); ++point) {
            const double x = sx(plot_budget_for_config(curve[point]));
            const double y = sy(curve[point].ppl);
            out << (point == 0 ? "M " : " L ") << svg_fmt(x) << ' ' << svg_fmt(y);
        }
        out << "\" fill=\"none\" stroke=\"#225ea8\" stroke-width=\"2.2\"/>\n";
        for (const Row& row : curve) {
            const double x = sx(plot_budget_for_config(row));
            const double y = sy(row.ppl);
            out << "<circle cx=\"" << svg_fmt(x) << "\" cy=\"" << svg_fmt(y) << "\" r=\"4\" fill=\"#d94801\"/>\n";
            out << "<text x=\"" << svg_fmt(x) << "\" y=\"" << svg_fmt(y - 8)
                << "\" text-anchor=\"middle\" class=\"small\" fill=\"#1f2933\">" << format_fixed(row.ppl, 2) << "</text>\n";
        }

        out << "<text x=\"" << svg_fmt(x0 + margin_l + plot_w / 2.0) << "\" y=\""
            << (y0 + margin_t + plot_h + 38)
            << "\" text-anchor=\"middle\" class=\"small\" fill=\"#1f2933\">average bits</text>\n";
        out << "<text x=\"" << (x0 + 12) << "\" y=\"" << svg_fmt(y0 + margin_t + plot_h / 2.0)
            << "\" transform=\"rotate(-90 " << (x0 + 12) << ' ' << svg_fmt(y0 + margin_t + plot_h / 2.0)
            << ")\" text-anchor=\"middle\" class=\"small\" fill=\"#1f2933\">PPL</text>\n";
    }

    out << "<text x=\"40\" y=\"" << (height - 24)
        << "\" class=\"small\" fill=\"#1f2933\">Solid line: uniform INT4 and consensus {4,8} budgets. "
           "Dashed green: FP16 reference. Short-slice fake quant; not a hardware result.</text>\n";
    out << "</svg>\n";
    return out.str();
}

CaseInput parse_input_arg(const std::string& text) {
    const std::size_t eq = text.find('=');
    if (eq == std::string::npos) {
        return CaseInput{fs::path(text).stem().string(), text};
    }
    return CaseInput{text.substr(0, eq), text.substr(eq + 1)};
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
            options.inputs.push_back(parse_input_arg(require_value("--input")));
        } else if (arg == "--out-json") {
            options.out_json = require_value("--out-json");
        } else if (arg == "--out-csv") {
            options.out_csv = require_value("--out-csv");
        } else if (arg == "--out-md") {
            options.out_md = require_value("--out-md");
        } else if (arg == "--out-svg") {
            options.out_svg = require_value("--out-svg");
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--no-write") {
            options.no_write = true;
        } else if (arg == "--help" || arg == "-h") {
            std::cout
                << "Usage: quant_budget_curve_summary --input label=summary.json [--input ...]\n"
                << "                                  [--out-json path] [--out-csv path]\n"
                << "                                  [--out-md path] [--out-svg path]\n"
                << "                                  [--emit json|csv|markdown|svg] [--no-write]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.inputs.empty()) {
        throw std::runtime_error("at least one --input is required");
    }
    return options;
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        const std::vector<Row> rows = load_all_rows(options.inputs);
        const std::string json = render_json(rows);
        const std::string csv = render_csv(rows);
        const std::string markdown = render_markdown(rows);
        const std::string svg = render_svg(rows);

        if (!options.no_write) {
            write_text_file(options.out_json, json);
            write_text_file(options.out_csv, csv);
            write_text_file(options.out_md, markdown);
            write_text_file(options.out_svg, svg);
        }

        if (options.emit == "json") {
            std::cout << json;
        } else if (options.emit == "csv") {
            std::cout << csv;
        } else if (options.emit == "markdown" || options.emit == "md") {
            std::cout << markdown;
        } else if (options.emit == "svg") {
            std::cout << svg;
        } else if (!options.emit.empty()) {
            throw std::runtime_error("unknown emit format: " + options.emit);
        } else {
            std::cout << "{\n"
                      << "  \"out_json\": \"" << json_escape(options.out_json) << "\",\n"
                      << "  \"out_csv\": \"" << json_escape(options.out_csv) << "\",\n"
                      << "  \"out_md\": \"" << json_escape(options.out_md) << "\",\n"
                      << "  \"out_svg\": \"" << json_escape(options.out_svg) << "\",\n"
                      << "  \"rows\": " << rows.size() << "\n"
                      << "}\n";
        }
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << "\n";
        return 1;
    }
    return 0;
}
