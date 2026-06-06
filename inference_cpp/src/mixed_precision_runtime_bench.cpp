#include "eigenskill/quant_kernels.hpp"

#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

constexpr std::array<char, 8> kMagic{{'E', 'S', 'M', 'P', 'Q', '0', '0', '1'}};
constexpr std::uint32_t kVersion = 1;
constexpr std::uint32_t kHeaderBytes = 64;
constexpr std::uint32_t kRowMetaBytes = 24;
constexpr std::uint32_t kQuantSchemeSignedSymmetricPerRow = 1;

struct Options {
    std::string input;
    int iters = 200;
    int warmup = 20;
    int active_rows = 0;
    std::uint32_t seed = 20260606;
};

struct EsmpMatrix {
    eigenskill::PackedMixedBitMatrix matrix;
    std::vector<int> row_sums;
    std::uint64_t data_bytes = 0;
    std::uint64_t file_bytes = 0;
};

[[noreturn]] void usage_error(const std::string& message) {
    throw std::runtime_error(
        message +
        "\nUsage: mixed_precision_runtime_bench --input weights.esmp [--iters 200] [--warmup 20] [--active-rows N]");
}

std::string require_value(int& i, int argc, char** argv, const char* name) {
    if (i + 1 >= argc) {
        usage_error(std::string("missing value for ") + name);
    }
    return argv[++i];
}

Options parse_args(int argc, char** argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        if (arg == "--input") {
            options.input = require_value(i, argc, argv, "--input");
        } else if (arg == "--iters") {
            options.iters = std::stoi(require_value(i, argc, argv, "--iters"));
        } else if (arg == "--warmup") {
            options.warmup = std::stoi(require_value(i, argc, argv, "--warmup"));
        } else if (arg == "--active-rows") {
            options.active_rows = std::stoi(require_value(i, argc, argv, "--active-rows"));
        } else if (arg == "--seed") {
            options.seed = static_cast<std::uint32_t>(std::stoul(require_value(i, argc, argv, "--seed")));
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: mixed_precision_runtime_bench --input weights.esmp [--iters 200] [--warmup 20] [--active-rows N]\n";
            std::exit(0);
        } else {
            usage_error("unknown argument: " + arg);
        }
    }
    if (options.input.empty()) {
        usage_error("--input is required");
    }
    if (options.iters <= 0 || options.warmup < 0 || options.active_rows < 0) {
        usage_error("--iters must be positive; --warmup and --active-rows must be non-negative");
    }
    return options;
}

std::uint32_t read_u32_le(const std::vector<std::uint8_t>& bytes, std::size_t offset) {
    if (offset + 4 > bytes.size()) {
        throw std::runtime_error("truncated u32 field");
    }
    std::uint32_t value = 0;
    for (int i = 0; i < 4; ++i) {
        value |= static_cast<std::uint32_t>(bytes[offset + static_cast<std::size_t>(i)]) << (8 * i);
    }
    return value;
}

std::int32_t read_i32_le(const std::vector<std::uint8_t>& bytes, std::size_t offset) {
    return static_cast<std::int32_t>(read_u32_le(bytes, offset));
}

std::uint64_t read_u64_le(const std::vector<std::uint8_t>& bytes, std::size_t offset) {
    if (offset + 8 > bytes.size()) {
        throw std::runtime_error("truncated u64 field");
    }
    std::uint64_t value = 0;
    for (int i = 0; i < 8; ++i) {
        value |= static_cast<std::uint64_t>(bytes[offset + static_cast<std::size_t>(i)]) << (8 * i);
    }
    return value;
}

float read_f32_le(const std::vector<std::uint8_t>& bytes, std::size_t offset) {
    const std::uint32_t raw = read_u32_le(bytes, offset);
    float value = 0.0f;
    std::memcpy(&value, &raw, sizeof(value));
    return value;
}

EsmpMatrix read_esmp(const std::string& path) {
    std::ifstream in(path, std::ios::binary);
    if (!in) {
        throw std::runtime_error("failed to open ESMP file: " + path);
    }
    in.seekg(0, std::ios::end);
    const std::streamoff size = in.tellg();
    in.seekg(0, std::ios::beg);
    if (size < static_cast<std::streamoff>(kHeaderBytes)) {
        throw std::runtime_error("ESMP file is smaller than header");
    }
    std::vector<std::uint8_t> bytes(static_cast<std::size_t>(size));
    in.read(reinterpret_cast<char*>(bytes.data()), size);
    if (!in) {
        throw std::runtime_error("failed to read ESMP file: " + path);
    }
    if (!std::equal(kMagic.begin(), kMagic.end(), reinterpret_cast<const char*>(bytes.data()))) {
        throw std::runtime_error("bad ESMP magic");
    }
    const std::uint32_t version = read_u32_le(bytes, 8);
    const std::uint32_t header_bytes = read_u32_le(bytes, 12);
    const std::uint64_t rows_u64 = read_u64_le(bytes, 16);
    const std::uint64_t cols_u64 = read_u64_le(bytes, 24);
    const std::uint64_t row_meta_offset = read_u64_le(bytes, 32);
    const std::uint64_t data_offset = read_u64_le(bytes, 40);
    const std::uint64_t data_bytes = read_u64_le(bytes, 48);
    const std::uint32_t quant_scheme = read_u32_le(bytes, 56);
    if (version != kVersion || header_bytes != kHeaderBytes || quant_scheme != kQuantSchemeSignedSymmetricPerRow) {
        throw std::runtime_error("unsupported ESMP version/header/quant scheme");
    }
    if (rows_u64 == 0 || cols_u64 == 0 || rows_u64 > static_cast<std::uint64_t>(std::numeric_limits<int>::max()) ||
        cols_u64 > static_cast<std::uint64_t>(std::numeric_limits<int>::max())) {
        throw std::runtime_error("invalid ESMP dimensions");
    }
    const std::uint64_t expected_meta_end = row_meta_offset + rows_u64 * static_cast<std::uint64_t>(kRowMetaBytes);
    if (row_meta_offset != kHeaderBytes || data_offset != expected_meta_end || data_offset + data_bytes != bytes.size()) {
        throw std::runtime_error("inconsistent ESMP offsets or payload length");
    }

    EsmpMatrix loaded;
    loaded.matrix.rows = static_cast<int>(rows_u64);
    loaded.matrix.cols = static_cast<int>(cols_u64);
    loaded.data_bytes = data_bytes;
    loaded.file_bytes = static_cast<std::uint64_t>(bytes.size());
    loaded.matrix.row_bits.assign(static_cast<std::size_t>(loaded.matrix.rows), 0);
    loaded.matrix.row_bit_offsets.assign(static_cast<std::size_t>(loaded.matrix.rows), 0);
    loaded.matrix.row_scales.assign(static_cast<std::size_t>(loaded.matrix.rows), 1.0f);
    loaded.row_sums.assign(static_cast<std::size_t>(loaded.matrix.rows), 0);

    std::uint64_t expected_row_bit_offset = 0;
    for (int row = 0; row < loaded.matrix.rows; ++row) {
        const std::size_t offset = static_cast<std::size_t>(row_meta_offset) + static_cast<std::size_t>(row) * kRowMetaBytes;
        const std::uint8_t bits = bytes[offset];
        if (bits < 2 || bits > 8) {
            throw std::runtime_error("invalid row bit width in ESMP metadata");
        }
        const std::uint64_t row_bit_offset = read_u64_le(bytes, offset + 8);
        if (row_bit_offset != expected_row_bit_offset) {
            throw std::runtime_error("non-contiguous row bit offsets in ESMP metadata");
        }
        loaded.matrix.row_bits[static_cast<std::size_t>(row)] = bits;
        loaded.matrix.row_scales[static_cast<std::size_t>(row)] = read_f32_le(bytes, offset + 4);
        loaded.matrix.row_bit_offsets[static_cast<std::size_t>(row)] = row_bit_offset;
        loaded.row_sums[static_cast<std::size_t>(row)] = static_cast<int>(read_i32_le(bytes, offset + 16));
        expected_row_bit_offset += static_cast<std::uint64_t>(bits) * static_cast<std::uint64_t>(loaded.matrix.cols);
    }
    const std::uint64_t expected_payload_bytes = (expected_row_bit_offset + 7u) / 8u;
    if (expected_payload_bytes != data_bytes) {
        throw std::runtime_error("ESMP payload byte count does not match row bit metadata");
    }
    loaded.matrix.bytes.assign(bytes.begin() + static_cast<std::ptrdiff_t>(data_offset), bytes.end());
    return loaded;
}

std::vector<float> random_vector(int n, std::uint32_t seed) {
    std::mt19937 rng(seed);
    std::normal_distribution<float> dist(0.0f, 1.0f);
    std::vector<float> values(static_cast<std::size_t>(n));
    for (float& value : values) {
        value = dist(rng);
    }
    return values;
}

std::vector<int> make_selected_rows(int rows, int active_rows) {
    std::vector<int> indices(static_cast<std::size_t>(active_rows));
    const double step = static_cast<double>(rows) / static_cast<double>(active_rows);
    for (int i = 0; i < active_rows; ++i) {
        indices[static_cast<std::size_t>(i)] = std::min(rows - 1, static_cast<int>(i * step));
    }
    return indices;
}

double average_bits(const std::vector<std::uint8_t>& bits) {
    if (bits.empty()) {
        return 0.0;
    }
    const double sum = std::accumulate(bits.begin(), bits.end(), 0.0);
    return sum / static_cast<double>(bits.size());
}

int count_high_rows(const std::vector<std::uint8_t>& bits, int threshold) {
    return static_cast<int>(std::count_if(bits.begin(), bits.end(), [threshold](std::uint8_t value) {
        return static_cast<int>(value) >= threshold;
    }));
}

template <typename Fn>
double time_ms(Fn&& fn, int iters, int warmup) {
    for (int i = 0; i < warmup; ++i) {
        fn();
    }
    const auto start = std::chrono::steady_clock::now();
    for (int i = 0; i < iters; ++i) {
        fn();
    }
    const auto end = std::chrono::steady_clock::now();
    return std::chrono::duration<double, std::milli>(end - start).count() / static_cast<double>(iters);
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        const EsmpMatrix loaded = read_esmp(options.input);
        const int rows = loaded.matrix.rows;
        const int cols = loaded.matrix.cols;
        const int active_rows = options.active_rows > 0 ? std::min(options.active_rows, rows) : 0;
        std::vector<float> x = random_vector(cols, options.seed);
        std::vector<float> y(static_cast<std::size_t>(rows), 0.0f);
        std::vector<float> y_selected(static_cast<std::size_t>(std::max(active_rows, 1)), 0.0f);
        std::vector<int> selected = active_rows > 0 ? make_selected_rows(rows, active_rows) : std::vector<int>{};

        const double full_ms = time_ms(
            [&]() { eigenskill::mixed_lowbit_dequant_gemv(loaded.matrix, x.data(), y.data()); },
            options.iters,
            options.warmup);

        double selected_ms = -1.0;
        if (active_rows > 0) {
            selected_ms = time_ms(
                [&]() {
                    eigenskill::mixed_lowbit_selected_rows_gemv(
                        loaded.matrix,
                        x.data(),
                        selected.data(),
                        active_rows,
                        y_selected.data());
                },
                options.iters,
                options.warmup);
        }

        const double package_mib = static_cast<double>(loaded.file_bytes) / (1024.0 * 1024.0);
        const double fp32_mib = static_cast<double>(rows) * static_cast<double>(cols) * sizeof(float) / (1024.0 * 1024.0);
        const double full_effective_mib_s = package_mib / std::max(full_ms / 1000.0, 1.0e-12);
        std::cout << std::fixed << std::setprecision(6);
        std::cout << "{\n";
        std::cout << "  \"ok\": true,\n";
        std::cout << "  \"input\": \"" << options.input << "\",\n";
        std::cout << "  \"rows\": " << rows << ",\n";
        std::cout << "  \"cols\": " << cols << ",\n";
        std::cout << "  \"iters\": " << options.iters << ",\n";
        std::cout << "  \"warmup\": " << options.warmup << ",\n";
        std::cout << "  \"avg_bits\": " << average_bits(loaded.matrix.row_bits) << ",\n";
        std::cout << "  \"rows_at_least_8bit\": " << count_high_rows(loaded.matrix.row_bits, 8) << ",\n";
        std::cout << "  \"payload_bytes\": " << loaded.data_bytes << ",\n";
        std::cout << "  \"file_bytes\": " << loaded.file_bytes << ",\n";
        std::cout << "  \"fp32_equivalent_bytes\": " << static_cast<std::uint64_t>(rows) * static_cast<std::uint64_t>(cols) * 4u << ",\n";
        std::cout << "  \"compression_ratio_vs_fp32\": " << (fp32_mib / std::max(package_mib, 1.0e-12)) << ",\n";
        std::cout << "  \"full_mixed_gemv_ms\": " << full_ms << ",\n";
        std::cout << "  \"full_effective_package_mib_per_s\": " << full_effective_mib_s << ",\n";
        std::cout << "  \"active_rows\": " << active_rows << ",\n";
        std::cout << "  \"selected_mixed_gemv_ms\": " << selected_ms << "\n";
        std::cout << "}\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
