#include "eigenskill/esmp_format.hpp"
#include "eigenskill/quant_kernels.hpp"

#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Options {
    std::string input;
    int expect_rows = 0;
    int expect_cols = 0;
    double max_avg_bits = 0.0;
    double min_compression_vs_fp32 = 0.0;
    bool verify_row_sums = false;
    std::vector<int> require_bits;
};

[[noreturn]] void usage_error(const std::string& message) {
    throw std::runtime_error(
        message +
        "\nUsage: esmp_inspect --input weights.esmp [--expect-rows N] [--expect-cols K] "
        "[--max-avg-bits B] [--min-compression-vs-fp32 R] [--require-bits 4,8] [--verify-row-sums]");
}

std::string require_value(int& i, int argc, char** argv, const char* name) {
    if (i + 1 >= argc) {
        usage_error(std::string("missing value for ") + name);
    }
    return argv[++i];
}

std::vector<int> parse_int_csv(const std::string& text) {
    std::vector<int> values;
    std::stringstream in(text);
    std::string token;
    while (std::getline(in, token, ',')) {
        if (token.empty()) {
            continue;
        }
        values.push_back(std::stoi(token));
    }
    return values;
}

Options parse_args(int argc, char** argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        if (arg == "--input") {
            options.input = require_value(i, argc, argv, "--input");
        } else if (arg == "--expect-rows") {
            options.expect_rows = std::stoi(require_value(i, argc, argv, "--expect-rows"));
        } else if (arg == "--expect-cols") {
            options.expect_cols = std::stoi(require_value(i, argc, argv, "--expect-cols"));
        } else if (arg == "--max-avg-bits") {
            options.max_avg_bits = std::stod(require_value(i, argc, argv, "--max-avg-bits"));
        } else if (arg == "--min-compression-vs-fp32") {
            options.min_compression_vs_fp32 = std::stod(require_value(i, argc, argv, "--min-compression-vs-fp32"));
        } else if (arg == "--require-bits") {
            options.require_bits = parse_int_csv(require_value(i, argc, argv, "--require-bits"));
        } else if (arg == "--verify-row-sums") {
            options.verify_row_sums = true;
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: esmp_inspect --input weights.esmp [checks]\n";
            std::exit(0);
        } else {
            usage_error("unknown argument: " + arg);
        }
    }
    if (options.input.empty()) {
        usage_error("--input is required");
    }
    if (options.expect_rows < 0 || options.expect_cols < 0 ||
        options.max_avg_bits < 0.0 || options.min_compression_vs_fp32 < 0.0) {
        usage_error("numeric checks must be non-negative");
    }
    for (int bits : options.require_bits) {
        if (bits < 2 || bits > 8) {
            usage_error("--require-bits entries must be in [2, 8]");
        }
    }
    return options;
}

std::map<int, int> histogram(const std::vector<std::uint8_t>& row_bits) {
    std::map<int, int> hist;
    for (std::uint8_t bits : row_bits) {
        ++hist[static_cast<int>(bits)];
    }
    return hist;
}

double average_bits(const std::vector<std::uint8_t>& row_bits) {
    if (row_bits.empty()) {
        return 0.0;
    }
    const double sum = std::accumulate(row_bits.begin(), row_bits.end(), 0.0);
    return sum / static_cast<double>(row_bits.size());
}

bool contains_bit(const std::map<int, int>& hist, int bits) {
    const auto it = hist.find(bits);
    return it != hist.end() && it->second > 0;
}

std::vector<int> recompute_row_sums(const eigenskill::PackedMixedBitMatrix& matrix) {
    std::vector<int> sums(static_cast<std::size_t>(matrix.rows), 0);
    for (int row = 0; row < matrix.rows; ++row) {
        const std::size_t index = static_cast<std::size_t>(row);
        const int bits = static_cast<int>(matrix.row_bits[index]);
        const std::uint64_t row_offset = matrix.row_bit_offsets[index];
        int sum = 0;
        for (int col = 0; col < matrix.cols; ++col) {
            const std::uint64_t bit_offset =
                row_offset + static_cast<std::uint64_t>(col) * static_cast<std::uint64_t>(bits);
            sum += static_cast<int>(
                eigenskill::unpack_signed_bits(matrix.bytes.data(), static_cast<std::size_t>(bit_offset), bits));
        }
        sums[index] = sum;
    }
    return sums;
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

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        const eigenskill::EsmpMatrix loaded = eigenskill::read_esmp_matrix(options.input);
        const auto hist = histogram(loaded.matrix.row_bits);
        const double avg_bits_value = average_bits(loaded.matrix.row_bits);
        const std::uint64_t fp32_bytes =
            static_cast<std::uint64_t>(loaded.matrix.rows) * static_cast<std::uint64_t>(loaded.matrix.cols) * 4u;
        const double compression =
            static_cast<double>(fp32_bytes) / std::max(1.0, static_cast<double>(loaded.file_bytes));

        std::vector<std::string> failures;
        if (options.expect_rows > 0 && loaded.matrix.rows != options.expect_rows) {
            failures.push_back("rows_mismatch");
        }
        if (options.expect_cols > 0 && loaded.matrix.cols != options.expect_cols) {
            failures.push_back("cols_mismatch");
        }
        if (options.max_avg_bits > 0.0 && avg_bits_value > options.max_avg_bits) {
            failures.push_back("avg_bits_too_high");
        }
        if (options.min_compression_vs_fp32 > 0.0 && compression < options.min_compression_vs_fp32) {
            failures.push_back("compression_too_low");
        }
        for (int bits : options.require_bits) {
            if (!contains_bit(hist, bits)) {
                failures.push_back("required_bit_width_missing");
                break;
            }
        }

        bool row_sums_ok = true;
        if (options.verify_row_sums) {
            const std::vector<int> recomputed = recompute_row_sums(loaded.matrix);
            row_sums_ok = recomputed == loaded.row_sums;
            if (!row_sums_ok) {
                failures.push_back("row_sums_mismatch");
            }
        }

        std::cout << std::fixed << std::setprecision(6);
        std::cout << "{\n";
        std::cout << "  \"ok\": " << (failures.empty() ? "true" : "false") << ",\n";
        std::cout << "  \"input\": \"" << json_escape(options.input) << "\",\n";
        std::cout << "  \"format\": \"" << eigenskill::kEsmpFormat << "\",\n";
        std::cout << "  \"version\": " << eigenskill::kEsmpVersion << ",\n";
        std::cout << "  \"rows\": " << loaded.matrix.rows << ",\n";
        std::cout << "  \"cols\": " << loaded.matrix.cols << ",\n";
        std::cout << "  \"avg_bits\": " << avg_bits_value << ",\n";
        std::cout << "  \"bit_histogram\": {";
        bool first = true;
        for (const auto& [bits, count] : hist) {
            std::cout << (first ? "" : ", ") << "\"" << bits << "\": " << count;
            first = false;
        }
        std::cout << "},\n";
        std::cout << "  \"payload_bytes\": " << loaded.data_bytes << ",\n";
        std::cout << "  \"file_bytes\": " << loaded.file_bytes << ",\n";
        std::cout << "  \"fp32_equivalent_bytes\": " << fp32_bytes << ",\n";
        std::cout << "  \"compression_ratio_vs_fp32\": " << compression << ",\n";
        std::cout << "  \"row_sums_checked\": " << (options.verify_row_sums ? "true" : "false") << ",\n";
        std::cout << "  \"row_sums_ok\": " << (row_sums_ok ? "true" : "false") << ",\n";
        std::cout << "  \"failures\": [";
        for (std::size_t i = 0; i < failures.size(); ++i) {
            std::cout << (i == 0 ? "" : ", ") << "\"" << failures[i] << "\"";
        }
        std::cout << "]\n";
        std::cout << "}\n";
        return failures.empty() ? 0 : 1;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
