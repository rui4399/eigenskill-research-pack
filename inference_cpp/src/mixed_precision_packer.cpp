#include "eigenskill/esmp_format.hpp"
#include "eigenskill/quant_kernels.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cctype>
#include <cstddef>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Options {
    bool synthetic = false;
    bool verify = false;
    int rows = 0;
    int cols = 0;
    int default_bits = 4;
    int sensitive_bits = 8;
    int sensitive_every = 16;
    std::uint32_t seed = 20260605;
    std::string weights_f32;
    std::string weights_text;
    std::string row_bits_csv;
    std::string row_bits_file;
    std::string out = "weights.esmp";
    std::string manifest_out;
};

[[noreturn]] void usage_error(const std::string& message) {
    throw std::runtime_error(
        message +
        "\nUsage: mixed_precision_packer --rows N --cols K (--synthetic | --weights-f32 path | --weights-text path) "
        "--out path [--manifest-out path] [--row-bits-csv 4,8,... | --row-bits-file path] "
        "[--default-bits 4] [--sensitive-every 16] [--sensitive-bits 8] [--verify]");
}

std::string require_value(int& i, int argc, char** argv, const char* name) {
    if (i + 1 >= argc) {
        usage_error(std::string("missing value for ") + name);
    }
    return argv[++i];
}

int parse_positive_int(const std::string& text, const char* name) {
    const int value = std::stoi(text);
    if (value <= 0) {
        usage_error(std::string(name) + " must be positive");
    }
    return value;
}

void validate_bits(int bits, const char* name) {
    if (bits < 2 || bits > 8) {
        usage_error(std::string(name) + " must be in [2, 8]");
    }
}

Options parse_args(int argc, char** argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        if (arg == "--synthetic") {
            options.synthetic = true;
        } else if (arg == "--verify") {
            options.verify = true;
        } else if (arg == "--rows") {
            options.rows = parse_positive_int(require_value(i, argc, argv, "--rows"), "--rows");
        } else if (arg == "--cols") {
            options.cols = parse_positive_int(require_value(i, argc, argv, "--cols"), "--cols");
        } else if (arg == "--default-bits") {
            options.default_bits = parse_positive_int(require_value(i, argc, argv, "--default-bits"), "--default-bits");
        } else if (arg == "--sensitive-bits") {
            options.sensitive_bits = parse_positive_int(require_value(i, argc, argv, "--sensitive-bits"), "--sensitive-bits");
        } else if (arg == "--sensitive-every") {
            options.sensitive_every =
                parse_positive_int(require_value(i, argc, argv, "--sensitive-every"), "--sensitive-every");
        } else if (arg == "--seed") {
            options.seed = static_cast<std::uint32_t>(std::stoul(require_value(i, argc, argv, "--seed")));
        } else if (arg == "--weights-f32") {
            options.weights_f32 = require_value(i, argc, argv, "--weights-f32");
        } else if (arg == "--weights-text") {
            options.weights_text = require_value(i, argc, argv, "--weights-text");
        } else if (arg == "--row-bits-csv") {
            options.row_bits_csv = require_value(i, argc, argv, "--row-bits-csv");
        } else if (arg == "--row-bits-file") {
            options.row_bits_file = require_value(i, argc, argv, "--row-bits-file");
        } else if (arg == "--out") {
            options.out = require_value(i, argc, argv, "--out");
        } else if (arg == "--manifest-out") {
            options.manifest_out = require_value(i, argc, argv, "--manifest-out");
        } else if (arg == "--help" || arg == "-h") {
            std::cout
                << "Usage: mixed_precision_packer --rows N --cols K "
                   "(--synthetic | --weights-f32 path | --weights-text path) --out path\n"
                << "Options:\n"
                << "  --weights-text path            ASCII float matrix fixture, row-major.\n"
                << "  --row-bits-csv 4,4,8,...       Per-row bit assignment.\n"
                << "  --row-bits-file path           Text file with per-row bit assignment.\n"
                << "  --default-bits N               Default row precision, 2..8.\n"
                << "  --sensitive-every N            Synthetic pattern: every Nth row uses sensitive bits.\n"
                << "  --sensitive-bits N             Synthetic high-precision row bits.\n"
                << "  --manifest-out path            Write JSON sidecar.\n"
                << "  --verify                       Reload the binary package and run a GEMV sanity check.\n";
            std::exit(0);
        } else {
            usage_error("unknown argument: " + arg);
        }
    }
    if (options.rows <= 0 || options.cols <= 0) {
        usage_error("--rows and --cols are required");
    }
    validate_bits(options.default_bits, "--default-bits");
    validate_bits(options.sensitive_bits, "--sensitive-bits");
    const int source_count = (options.synthetic ? 1 : 0) +
                             (!options.weights_f32.empty() ? 1 : 0) +
                             (!options.weights_text.empty() ? 1 : 0);
    if (source_count != 1) {
        usage_error("choose exactly one of --synthetic, --weights-f32, or --weights-text");
    }
    if (!options.row_bits_csv.empty() && !options.row_bits_file.empty()) {
        usage_error("choose at most one of --row-bits-csv or --row-bits-file");
    }
    return options;
}

std::string read_text_file(const std::string& path) {
    std::ifstream in(path, std::ios::binary);
    if (!in) {
        throw std::runtime_error("failed to open text file: " + path);
    }
    std::ostringstream buffer;
    buffer << in.rdbuf();
    return buffer.str();
}

std::vector<int> parse_ints_from_text(const std::string& text) {
    std::vector<int> values;
    std::size_t i = 0;
    while (i < text.size()) {
        while (i < text.size() && !std::isdigit(static_cast<unsigned char>(text[i]))) {
            ++i;
        }
        if (i >= text.size()) {
            break;
        }
        int value = 0;
        while (i < text.size() && std::isdigit(static_cast<unsigned char>(text[i]))) {
            value = value * 10 + static_cast<int>(text[i] - '0');
            ++i;
        }
        values.push_back(value);
    }
    return values;
}

std::vector<float> read_f32_matrix(const std::string& path, int rows, int cols) {
    const std::size_t expected_values = static_cast<std::size_t>(rows) * static_cast<std::size_t>(cols);
    const std::size_t expected_bytes = expected_values * sizeof(float);
    std::ifstream in(path, std::ios::binary);
    if (!in) {
        throw std::runtime_error("failed to open FP32 weights: " + path);
    }
    in.seekg(0, std::ios::end);
    const std::streamoff size = in.tellg();
    in.seekg(0, std::ios::beg);
    if (size != static_cast<std::streamoff>(expected_bytes)) {
        std::ostringstream error;
        error << "FP32 file size mismatch: got " << size << " bytes, expected " << expected_bytes;
        throw std::runtime_error(error.str());
    }
    std::vector<float> values(expected_values);
    in.read(reinterpret_cast<char*>(values.data()), static_cast<std::streamsize>(expected_bytes));
    if (!in) {
        throw std::runtime_error("failed to read FP32 weights: " + path);
    }
    return values;
}

std::vector<float> read_f32_matrix_text(const std::string& path, int rows, int cols) {
    const std::size_t expected_values = static_cast<std::size_t>(rows) * static_cast<std::size_t>(cols);
    std::ifstream in(path);
    if (!in) {
        throw std::runtime_error("failed to open text weights: " + path);
    }
    std::vector<float> values;
    values.reserve(expected_values);
    float value = 0.0f;
    while (in >> value) {
        values.push_back(value);
    }
    if (!in.eof()) {
        throw std::runtime_error("failed to parse text weights as floats: " + path);
    }
    if (values.size() != expected_values) {
        std::ostringstream error;
        error << "text weight value count mismatch: got " << values.size()
              << ", expected " << expected_values;
        throw std::runtime_error(error.str());
    }
    return values;
}

std::vector<float> synthetic_weights(int rows, int cols, std::uint32_t seed) {
    std::mt19937 rng(seed);
    std::normal_distribution<float> base(0.0f, 0.035f);
    std::vector<float> values(static_cast<std::size_t>(rows) * static_cast<std::size_t>(cols));
    for (int row = 0; row < rows; ++row) {
        const float row_gain = 1.0f + 0.015f * static_cast<float>(row % 17);
        for (int col = 0; col < cols; ++col) {
            const float structured = 0.01f * std::sin(0.013f * static_cast<float>(row * 31 + col * 7));
            values[static_cast<std::size_t>(row) * static_cast<std::size_t>(cols) + static_cast<std::size_t>(col)] =
                row_gain * base(rng) + structured;
        }
    }
    return values;
}

std::vector<std::uint8_t> build_row_bits(const Options& options) {
    std::vector<int> parsed;
    if (!options.row_bits_csv.empty()) {
        parsed = parse_ints_from_text(options.row_bits_csv);
    } else if (!options.row_bits_file.empty()) {
        parsed = parse_ints_from_text(read_text_file(options.row_bits_file));
    }

    std::vector<std::uint8_t> row_bits(static_cast<std::size_t>(options.rows),
                                       static_cast<std::uint8_t>(options.default_bits));
    if (!parsed.empty()) {
        if (parsed.size() != static_cast<std::size_t>(options.rows)) {
            usage_error("row bit assignment length must equal --rows");
        }
        for (int row = 0; row < options.rows; ++row) {
            validate_bits(parsed[static_cast<std::size_t>(row)], "row bit assignment");
            row_bits[static_cast<std::size_t>(row)] = static_cast<std::uint8_t>(parsed[static_cast<std::size_t>(row)]);
        }
        return row_bits;
    }

    if (options.synthetic) {
        for (int row = 0; row < options.rows; ++row) {
            if (row % options.sensitive_every == 0) {
                row_bits[static_cast<std::size_t>(row)] = static_cast<std::uint8_t>(options.sensitive_bits);
            }
        }
    }
    return row_bits;
}

std::vector<int> compute_row_sums(const eigenskill::PackedMixedBitMatrix& packed) {
    std::vector<int> sums(static_cast<std::size_t>(packed.rows), 0);
    for (int row = 0; row < packed.rows; ++row) {
        const int bits = static_cast<int>(packed.row_bits[static_cast<std::size_t>(row)]);
        const std::uint64_t row_offset = packed.row_bit_offsets[static_cast<std::size_t>(row)];
        int sum = 0;
        for (int col = 0; col < packed.cols; ++col) {
            const std::uint64_t bit_offset = row_offset + static_cast<std::uint64_t>(col) * static_cast<std::uint64_t>(bits);
            sum += static_cast<int>(eigenskill::unpack_signed_bits(
                packed.bytes.data(),
                static_cast<std::size_t>(bit_offset),
                bits));
        }
        sums[static_cast<std::size_t>(row)] = sum;
    }
    return sums;
}

double average_bits(const std::vector<std::uint8_t>& row_bits) {
    double sum = 0.0;
    for (std::uint8_t bits : row_bits) {
        sum += static_cast<double>(bits);
    }
    return row_bits.empty() ? 0.0 : sum / static_cast<double>(row_bits.size());
}

double verify_gemv_rel_l2(const eigenskill::PackedMixedBitMatrix& packed, const std::vector<float>& weights) {
    std::mt19937 rng(20260605);
    std::normal_distribution<float> dist(0.0f, 1.0f);
    std::vector<float> x(static_cast<std::size_t>(packed.cols));
    for (float& value : x) {
        value = dist(rng);
    }
    std::vector<float> dense(static_cast<std::size_t>(packed.rows), 0.0f);
    std::vector<float> packed_out(static_cast<std::size_t>(packed.rows), 0.0f);
    eigenskill::MatrixView view{weights.data(), packed.rows, packed.cols};
    eigenskill::dense_gemv_avx2(view, x.data(), dense.data());
    eigenskill::mixed_lowbit_dequant_gemv(packed, x.data(), packed_out.data());
    return eigenskill::rel_l2_error(packed_out.data(), dense.data(), packed.rows);
}

std::map<int, int> histogram(const std::vector<std::uint8_t>& row_bits) {
    std::map<int, int> hist;
    for (std::uint8_t bits : row_bits) {
        ++hist[static_cast<int>(bits)];
    }
    return hist;
}

void write_manifest(const std::string& path,
                    const Options& options,
                    const eigenskill::PackedMixedBitMatrix& packed,
                    double rel_l2,
                    bool verify_ok) {
    if (path.empty()) {
        return;
    }
    std::ofstream out(path, std::ios::binary);
    if (!out) {
        throw std::runtime_error("failed to create manifest: " + path);
    }
    const std::size_t f32_bytes =
        static_cast<std::size_t>(packed.rows) * static_cast<std::size_t>(packed.cols) * sizeof(float);
    const std::size_t row_meta_bytes = static_cast<std::size_t>(packed.rows) * eigenskill::kEsmpRowMetaBytes;
    const std::size_t total_package_bytes =
        static_cast<std::size_t>(eigenskill::esmp_total_package_bytes(
            packed.rows,
            static_cast<std::uint64_t>(packed.bytes.size())));
    const std::map<int, int> hist = histogram(packed.row_bits);

    out << std::fixed << std::setprecision(6);
    out << "{\n";
    out << "  \"format\": \"" << eigenskill::kEsmpFormat << "\",\n";
    out << "  \"version\": " << eigenskill::kEsmpVersion << ",\n";
    out << "  \"quantization\": \"signed_symmetric_per_row_mixed_lowbit\",\n";
    out << "  \"rows\": " << packed.rows << ",\n";
    out << "  \"cols\": " << packed.cols << ",\n";
    out << "  \"avg_bits\": " << average_bits(packed.row_bits) << ",\n";
    out << "  \"raw_fp32_bytes\": " << f32_bytes << ",\n";
    out << "  \"packed_payload_bytes\": " << packed.bytes.size() << ",\n";
    out << "  \"row_metadata_bytes\": " << row_meta_bytes << ",\n";
    out << "  \"total_package_bytes\": " << total_package_bytes << ",\n";
    out << "  \"compression_ratio_vs_fp32\": "
        << (static_cast<double>(f32_bytes) / std::max(1.0, static_cast<double>(total_package_bytes))) << ",\n";
    out << "  \"row_bits_histogram\": {";
    bool first = true;
    for (const auto& [bits, count] : hist) {
        out << (first ? "" : ", ") << "\"" << bits << "\": " << count;
        first = false;
    }
    out << "},\n";
    out << "  \"binary_path\": \"" << options.out << "\",\n";
    out << "  \"source\": \""
        << (options.synthetic ? "synthetic" : (!options.weights_text.empty() ? options.weights_text : options.weights_f32))
        << "\",\n";
    out << "  \"verify_requested\": " << (options.verify ? "true" : "false") << ",\n";
    out << "  \"verify_gemv_rel_l2\": " << rel_l2 << ",\n";
    out << "  \"verify_ok\": " << (verify_ok ? "true" : "false") << "\n";
    out << "}\n";
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        std::vector<float> weights;
        if (options.synthetic) {
            weights = synthetic_weights(options.rows, options.cols, options.seed);
        } else if (!options.weights_text.empty()) {
            weights = read_f32_matrix_text(options.weights_text, options.rows, options.cols);
        } else {
            weights = read_f32_matrix(options.weights_f32, options.rows, options.cols);
        }
        const std::vector<std::uint8_t> row_bits = build_row_bits(options);
        eigenskill::PackedMixedBitMatrix packed =
            eigenskill::pack_mixed_lowbit_per_row(weights.data(), options.rows, options.cols, row_bits.data());
        const std::vector<int> row_sums = compute_row_sums(packed);

        eigenskill::write_esmp_matrix(options.out, packed, row_sums);

        double rel_l2 = -1.0;
        bool verify_ok = !options.verify;
        if (options.verify) {
            eigenskill::EsmpMatrix loaded = eigenskill::read_esmp_matrix(options.out);
            if (loaded.matrix.rows != packed.rows || loaded.matrix.cols != packed.cols || loaded.matrix.bytes != packed.bytes ||
                loaded.matrix.row_bits != packed.row_bits || loaded.matrix.row_bit_offsets != packed.row_bit_offsets ||
                loaded.row_sums != row_sums) {
                throw std::runtime_error("reload verification failed: metadata or payload mismatch");
            }
            rel_l2 = verify_gemv_rel_l2(loaded.matrix, weights);
            verify_ok = std::isfinite(rel_l2);
        }

        write_manifest(options.manifest_out, options, packed, rel_l2, verify_ok);

        const std::size_t raw_bytes =
            static_cast<std::size_t>(options.rows) * static_cast<std::size_t>(options.cols) * sizeof(float);
        const std::size_t package_bytes =
            static_cast<std::size_t>(eigenskill::esmp_total_package_bytes(
                options.rows,
                static_cast<std::uint64_t>(packed.bytes.size())));
        std::cout << std::fixed << std::setprecision(6);
        std::cout << "{\n";
        std::cout << "  \"ok\": true,\n";
        std::cout << "  \"format\": \"ESMPQ001\",\n";
        std::cout << "  \"rows\": " << options.rows << ",\n";
        std::cout << "  \"cols\": " << options.cols << ",\n";
        std::cout << "  \"avg_bits\": " << average_bits(row_bits) << ",\n";
        std::cout << "  \"raw_fp32_bytes\": " << raw_bytes << ",\n";
        std::cout << "  \"total_package_bytes\": " << package_bytes << ",\n";
        std::cout << "  \"compression_ratio_vs_fp32\": "
                  << (static_cast<double>(raw_bytes) / std::max(1.0, static_cast<double>(package_bytes))) << ",\n";
        std::cout << "  \"out\": \"" << options.out << "\",\n";
        std::cout << "  \"manifest_out\": \"" << options.manifest_out << "\",\n";
        std::cout << "  \"verify_gemv_rel_l2\": " << rel_l2 << ",\n";
        std::cout << "  \"verify_ok\": " << (verify_ok ? "true" : "false") << "\n";
        std::cout << "}\n";
        return verify_ok ? 0 : 1;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
