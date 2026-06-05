#include <algorithm>
#include <cctype>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace {

struct LogInput {
    std::string label;
    std::string path;
};

struct Options {
    std::vector<LogInput> logs;
    std::string emit = "markdown";
};

struct PackageVersion {
    std::string name;
    std::string version;
};

struct ProbeResult {
    std::string label;
    std::string path;
    bool success = false;
    bool timeout = false;
    bool build_started = false;
    bool metadata_prepared = false;
    bool no_deps = false;
    std::vector<PackageVersion> installed;
    std::string failure_hint;
};

bool contains(const std::string& text, const std::string& needle) {
    return text.find(needle) != std::string::npos;
}

std::string read_text_file(const std::string& path) {
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("failed to open: " + path);
    }
    std::ostringstream buffer;
    buffer << in.rdbuf();
    return buffer.str();
}

std::string trim(std::string value) {
    auto not_space = [](unsigned char ch) { return !std::isspace(ch); };
    value.erase(value.begin(), std::find_if(value.begin(), value.end(), not_space));
    value.erase(std::find_if(value.rbegin(), value.rend(), not_space).base(), value.end());
    return value;
}

std::string json_escape(const std::string& value) {
    std::ostringstream out;
    for (char ch : value) {
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

std::pair<std::string, std::string> split_label_path(const std::string& spec) {
    const std::size_t pos = spec.find('=');
    if (pos == std::string::npos) {
        return {spec, spec};
    }
    const std::string label = trim(spec.substr(0, pos));
    const std::string path = trim(spec.substr(pos + 1));
    if (label.empty() || path.empty()) {
        throw std::runtime_error("--log expects label=path");
    }
    return {label, path};
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
        if (arg == "--log") {
            const auto parsed = split_label_path(require_value("--log"));
            options.logs.push_back({parsed.first, parsed.second});
        } else if (arg == "--emit") {
            options.emit = require_value("--emit");
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: baseline_install_probe --log label=install.log [--log label=other.log]\n"
                         "                              [--emit markdown|json|csv]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.logs.empty()) {
        throw std::runtime_error("at least one --log is required");
    }
    if (options.emit != "markdown" && options.emit != "json" && options.emit != "csv") {
        throw std::runtime_error("--emit must be markdown, json, or csv");
    }
    return options;
}

std::vector<PackageVersion> parse_successfully_installed(const std::string& text) {
    std::vector<PackageVersion> versions;
    const std::string marker = "Successfully installed ";
    std::size_t pos = 0;
    while ((pos = text.find(marker, pos)) != std::string::npos) {
        pos += marker.size();
        const std::size_t end = text.find('\n', pos);
        std::string line = text.substr(pos, end == std::string::npos ? std::string::npos : end - pos);
        line = trim(line);
        std::istringstream parts(line);
        std::string token;
        while (parts >> token) {
            const std::size_t dash = token.rfind('-');
            if (dash == std::string::npos || dash == 0 || dash + 1 >= token.size()) {
                continue;
            }
            std::string version = token.substr(dash + 1);
            const bool version_like = std::any_of(version.begin(), version.end(), [](unsigned char ch) {
                return std::isdigit(ch);
            });
            if (!version_like) {
                continue;
            }
            versions.push_back({token.substr(0, dash), version});
        }
    }
    return versions;
}

std::string infer_failure_hint(const std::string& text) {
    if (contains(text, "ReadTimeoutError") || contains(text, "Read timed out") || contains(text, "TimeoutError")) {
        return "network_read_timeout";
    }
    if (contains(text, "No matching distribution found")) {
        return "no_matching_distribution";
    }
    if (contains(text, "subprocess-exited-with-error")) {
        return "build_subprocess_error";
    }
    if (contains(text, "ERROR:")) {
        return "pip_error";
    }
    return "";
}

ProbeResult probe_log(const LogInput& input) {
    const std::string text = read_text_file(input.path);
    ProbeResult result;
    result.label = input.label;
    result.path = input.path;
    result.success = contains(text, "Successfully installed");
    result.timeout = contains(text, "ReadTimeoutError") || contains(text, "Read timed out") || contains(text, "TimeoutError");
    result.build_started = contains(text, "Building wheel") || contains(text, "Installing build dependencies: started");
    result.metadata_prepared = contains(text, "Preparing metadata") || contains(text, "Getting requirements to build wheel");
    result.no_deps = contains(text, "--no-deps") || contains(input.label, "nodeps") || contains(input.label, "no_deps");
    result.installed = parse_successfully_installed(text);
    result.failure_hint = result.success ? "" : infer_failure_hint(text);
    return result;
}

std::string render_json(const std::vector<ProbeResult>& results) {
    std::ostringstream out;
    out << "{\n  \"baseline_install_probes\": [\n";
    for (std::size_t i = 0; i < results.size(); ++i) {
        const ProbeResult& r = results[i];
        out << "    {\n"
            << "      \"label\": \"" << json_escape(r.label) << "\",\n"
            << "      \"path\": \"" << json_escape(r.path) << "\",\n"
            << "      \"success\": " << (r.success ? "true" : "false") << ",\n"
            << "      \"timeout\": " << (r.timeout ? "true" : "false") << ",\n"
            << "      \"build_started\": " << (r.build_started ? "true" : "false") << ",\n"
            << "      \"metadata_prepared\": " << (r.metadata_prepared ? "true" : "false") << ",\n"
            << "      \"no_deps\": " << (r.no_deps ? "true" : "false") << ",\n"
            << "      \"failure_hint\": \"" << json_escape(r.failure_hint) << "\",\n"
            << "      \"installed\": [";
        for (std::size_t j = 0; j < r.installed.size(); ++j) {
            if (j != 0) {
                out << ", ";
            }
            out << "{\"name\":\"" << json_escape(r.installed[j].name)
                << "\",\"version\":\"" << json_escape(r.installed[j].version) << "\"}";
        }
        out << "]\n    }";
        if (i + 1 != results.size()) {
            out << ",";
        }
        out << "\n";
    }
    out << "  ]\n}\n";
    return out.str();
}

std::string render_csv(const std::vector<ProbeResult>& results) {
    std::ostringstream out;
    out << "label,path,success,timeout,no_deps,failure_hint,installed\n";
    for (const ProbeResult& r : results) {
        std::ostringstream installed;
        for (std::size_t i = 0; i < r.installed.size(); ++i) {
            if (i != 0) {
                installed << ";";
            }
            installed << r.installed[i].name << "==" << r.installed[i].version;
        }
        out << r.label << "," << r.path << "," << (r.success ? "true" : "false") << ","
            << (r.timeout ? "true" : "false") << "," << (r.no_deps ? "true" : "false") << ","
            << r.failure_hint << "," << installed.str() << "\n";
    }
    return out.str();
}

std::string render_markdown(const std::vector<ProbeResult>& results) {
    std::ostringstream out;
    out << "# Baseline Install Probe\n\n"
        << "This report summarizes local attempts to install public quantization baseline packages. "
        << "It is an environment-readiness artifact, not a completed GPTQ/AWQ baseline evaluation.\n\n"
        << "| probe | success | timeout | no-deps | installed packages | failure hint |\n"
        << "|---|---:|---:|---:|---|---|\n";
    for (const ProbeResult& r : results) {
        std::ostringstream installed;
        if (r.installed.empty()) {
            installed << "";
        } else {
            for (std::size_t i = 0; i < r.installed.size(); ++i) {
                if (i != 0) {
                    installed << "<br>";
                }
                installed << "`" << r.installed[i].name << "==" << r.installed[i].version << "`";
            }
        }
        out << "| `" << r.label << "` | " << (r.success ? "true" : "false") << " | "
            << (r.timeout ? "true" : "false") << " | " << (r.no_deps ? "true" : "false")
            << " | " << installed.str() << " | `" << r.failure_hint << "` |\n";
    }
    out << "\n## Interpretation\n\n"
        << "- A full dependency install must complete before claiming a runnable GPTQ/AWQ/Optimum baseline.\n"
        << "- A no-deps install only proves package metadata/build availability; it does not prove the baseline can run.\n"
        << "- Until runnable baselines are installed and evaluated, current claims remain limited to fake-quant diagnostics.\n";
    return out.str();
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        std::vector<ProbeResult> results;
        for (const LogInput& input : options.logs) {
            results.push_back(probe_log(input));
        }

        if (options.emit == "json") {
            std::cout << render_json(results);
        } else if (options.emit == "csv") {
            std::cout << render_csv(results);
        } else {
            std::cout << render_markdown(results);
        }
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << "\n";
        return 1;
    }
    return 0;
}

