#include "eigenskill/esmp_format.hpp"
#include "eigenskill/quant_kernels.hpp"

#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Options {
    std::string input;
    int iters = 200;
    int warmup = 20;
    int active_rows = 0;
    std::uint32_t seed = 20260606;
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
        const eigenskill::EsmpMatrix loaded = eigenskill::read_esmp_matrix(options.input);
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
        const double selected_speedup_vs_full =
            selected_ms > 0.0 ? full_ms / selected_ms : -1.0;

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
        std::cout << "  \"selected_mixed_gemv_ms\": " << selected_ms << ",\n";
        std::cout << "  \"selected_speedup_vs_full_mixed_gemv\": " << selected_speedup_vs_full << "\n";
        std::cout << "}\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
