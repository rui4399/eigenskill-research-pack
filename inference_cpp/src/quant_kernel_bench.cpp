#include "eigenskill/quant_kernels.hpp"

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

using Clock = std::chrono::steady_clock;

volatile float g_sink = 0.0f;

struct Options {
    std::vector<int> dims{512, 1024, 2048};
    std::vector<int> active_rows{16, 64, 256};
    int iters = 200;
    int warmup = 20;
    std::uint32_t seed = 20260604;
};

struct Result {
    int d = 0;
    int active_rows = 0;
    double dense_ms = 0.0;
    double dense_avx2_ms = 0.0;
    double int4_ms = 0.0;
    double int3_ms = 0.0;
    double mixed_ms = 0.0;
    double selected_ms = 0.0;
    double selected_avx2_ms = 0.0;
    double mixed_selected_ms = 0.0;
    double scalar_ms = 0.0;
    double dense_avx2_rel_l2 = 0.0;
    double int4_rel_l2 = 0.0;
    double int3_rel_l2 = 0.0;
    double mixed_rel_l2 = 0.0;
    double selected_rel_l2 = 0.0;
    double selected_avx2_rel_l2 = 0.0;
    double mixed_selected_rel_l2 = 0.0;
};

std::vector<int> parse_list(const std::string& text) {
    std::vector<int> values;
    std::stringstream ss(text);
    std::string item;
    while (std::getline(ss, item, ',')) {
        if (!item.empty()) {
            values.push_back(std::stoi(item));
        }
    }
    if (values.empty()) {
        throw std::runtime_error("empty integer list: " + text);
    }
    return values;
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

        if (arg == "--dims") {
            options.dims = parse_list(require_value("--dims"));
        } else if (arg == "--active-rows") {
            options.active_rows = parse_list(require_value("--active-rows"));
        } else if (arg == "--iters") {
            options.iters = std::stoi(require_value("--iters"));
        } else if (arg == "--warmup") {
            options.warmup = std::stoi(require_value("--warmup"));
        } else if (arg == "--seed") {
            options.seed = static_cast<std::uint32_t>(std::stoul(require_value("--seed")));
        } else if (arg == "--help" || arg == "-h") {
            std::cout
                << "Usage: quant_kernel_bench [--dims 512,1024,2048]\n"
                << "                          [--active-rows 16,64,256]\n"
                << "                          [--iters 200] [--warmup 20] [--seed 20260604]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.iters <= 0 || options.warmup < 0) {
        throw std::runtime_error("--iters must be positive and --warmup must be non-negative");
    }
    return options;
}

std::vector<float> random_vector(std::size_t n, std::mt19937& rng, float scale) {
    std::normal_distribution<float> dist(0.0f, scale);
    std::vector<float> values(n);
    for (float& value : values) {
        value = dist(rng);
    }
    return values;
}

std::vector<int> make_active_rows(int d, int active_rows) {
    active_rows = std::min(active_rows, d);
    std::vector<int> rows(static_cast<std::size_t>(active_rows));
    if (active_rows <= 0) {
        return rows;
    }
    const double step = static_cast<double>(d) / static_cast<double>(active_rows);
    for (int i = 0; i < active_rows; ++i) {
        rows[static_cast<std::size_t>(i)] = std::min(d - 1, static_cast<int>(i * step));
    }
    return rows;
}

template <typename Fn>
double time_ms(Fn&& fn, const std::vector<float>& output, int warmup, int iters) {
    for (int i = 0; i < warmup; ++i) {
        fn();
        if (!output.empty()) {
            g_sink += output[static_cast<std::size_t>(i) % output.size()];
        }
    }
    const auto start = Clock::now();
    for (int i = 0; i < iters; ++i) {
        fn();
        if (!output.empty()) {
            g_sink += output[static_cast<std::size_t>(i) % output.size()];
        }
    }
    const auto end = Clock::now();
    const double elapsed_ms = std::chrono::duration<double, std::milli>(end - start).count();
    return elapsed_ms / static_cast<double>(iters);
}

Result benchmark_case(int d, int active_rows, const Options& options) {
    if (active_rows <= 0 || active_rows > d) {
        throw std::runtime_error("active rows must be in [1, d]");
    }

    std::mt19937 rng(options.seed + static_cast<std::uint32_t>(d * 131 + active_rows * 17));
    std::vector<float> w = random_vector(static_cast<std::size_t>(d) * d, rng, 0.04f);
    std::vector<float> x = random_vector(static_cast<std::size_t>(d), rng, 1.0f);
    std::vector<int> rows = make_active_rows(d, active_rows);
    eigenskill::MatrixView matrix{w.data(), d, d};
    eigenskill::PackedInt4Matrix packed_int4 = eigenskill::pack_int4_per_row(w.data(), d, d);
    eigenskill::PackedLowBitMatrix packed_int3 = eigenskill::pack_lowbit_per_row(w.data(), d, d, 3);
    std::vector<std::uint8_t> row_bits(static_cast<std::size_t>(d), 4);
    for (int row = 0; row < d; ++row) {
        if (row % 16 == 0) {
            row_bits[static_cast<std::size_t>(row)] = 8;
        } else if (row % 5 == 0) {
            row_bits[static_cast<std::size_t>(row)] = 3;
        }
    }
    eigenskill::PackedMixedBitMatrix packed_mixed =
        eigenskill::pack_mixed_lowbit_per_row(w.data(), d, d, row_bits.data());

    std::vector<float> y_dense(static_cast<std::size_t>(d), 0.0f);
    std::vector<float> y_dense_avx2(static_cast<std::size_t>(d), 0.0f);
    std::vector<float> y_int4(static_cast<std::size_t>(d), 0.0f);
    std::vector<float> y_int3(static_cast<std::size_t>(d), 0.0f);
    std::vector<float> y_mixed(static_cast<std::size_t>(d), 0.0f);
    std::vector<float> y_selected(static_cast<std::size_t>(active_rows), 0.0f);
    std::vector<float> y_selected_avx2(static_cast<std::size_t>(active_rows), 0.0f);
    std::vector<float> y_selected_ref(static_cast<std::size_t>(active_rows), 0.0f);
    std::vector<float> y_mixed_selected(static_cast<std::size_t>(active_rows), 0.0f);
    std::vector<float> y_mixed_selected_ref(static_cast<std::size_t>(active_rows), 0.0f);
    std::vector<float> y_scalar(static_cast<std::size_t>(d), 0.0f);

    eigenskill::dense_gemv(matrix, x.data(), y_dense.data());
    eigenskill::dense_gemv_avx2(matrix, x.data(), y_dense_avx2.data());
    eigenskill::int4_dequant_gemv(packed_int4, x.data(), y_int4.data());
    eigenskill::lowbit_dequant_gemv(packed_int3, x.data(), y_int3.data());
    eigenskill::mixed_lowbit_dequant_gemv(packed_mixed, x.data(), y_mixed.data());
    eigenskill::selected_rows_gemv(matrix, x.data(), rows.data(), active_rows, y_selected.data());
    eigenskill::selected_rows_gemv_avx2(matrix, x.data(), rows.data(), active_rows, y_selected_avx2.data());
    eigenskill::mixed_lowbit_selected_rows_gemv(
        packed_mixed, x.data(), rows.data(), active_rows, y_mixed_selected.data());
    for (int i = 0; i < active_rows; ++i) {
        y_selected_ref[static_cast<std::size_t>(i)] = y_dense[static_cast<std::size_t>(rows[static_cast<std::size_t>(i)])];
        y_mixed_selected_ref[static_cast<std::size_t>(i)] =
            y_mixed[static_cast<std::size_t>(rows[static_cast<std::size_t>(i)])];
    }
    eigenskill::scalar_skill_bypass(x.data(), y_scalar.data(), d, 0.875f);

    Result result;
    result.d = d;
    result.active_rows = active_rows;
    result.dense_avx2_rel_l2 = eigenskill::rel_l2_error(y_dense_avx2.data(), y_dense.data(), d);
    result.int4_rel_l2 = eigenskill::rel_l2_error(y_int4.data(), y_dense.data(), d);
    result.int3_rel_l2 = eigenskill::rel_l2_error(y_int3.data(), y_dense.data(), d);
    result.mixed_rel_l2 = eigenskill::rel_l2_error(y_mixed.data(), y_dense.data(), d);
    result.selected_rel_l2 = eigenskill::rel_l2_error(y_selected.data(), y_selected_ref.data(), active_rows);
    result.selected_avx2_rel_l2 = eigenskill::rel_l2_error(y_selected_avx2.data(), y_selected_ref.data(), active_rows);
    result.mixed_selected_rel_l2 =
        eigenskill::rel_l2_error(y_mixed_selected.data(), y_mixed_selected_ref.data(), active_rows);

    result.dense_ms = time_ms([&]() { eigenskill::dense_gemv(matrix, x.data(), y_dense.data()); }, y_dense, options.warmup, options.iters);
    result.dense_avx2_ms = time_ms([&]() { eigenskill::dense_gemv_avx2(matrix, x.data(), y_dense_avx2.data()); }, y_dense_avx2, options.warmup, options.iters);
    result.int4_ms = time_ms([&]() { eigenskill::int4_dequant_gemv(packed_int4, x.data(), y_int4.data()); }, y_int4, options.warmup, options.iters);
    result.int3_ms = time_ms([&]() { eigenskill::lowbit_dequant_gemv(packed_int3, x.data(), y_int3.data()); }, y_int3, options.warmup, options.iters);
    result.mixed_ms =
        time_ms([&]() { eigenskill::mixed_lowbit_dequant_gemv(packed_mixed, x.data(), y_mixed.data()); },
                y_mixed,
                options.warmup,
                options.iters);
    result.selected_ms = time_ms([&]() { eigenskill::selected_rows_gemv(matrix, x.data(), rows.data(), active_rows, y_selected.data()); }, y_selected, options.warmup, options.iters);
    result.selected_avx2_ms = time_ms([&]() { eigenskill::selected_rows_gemv_avx2(matrix, x.data(), rows.data(), active_rows, y_selected_avx2.data()); }, y_selected_avx2, options.warmup, options.iters);
    result.mixed_selected_ms =
        time_ms([&]() {
            eigenskill::mixed_lowbit_selected_rows_gemv(
                packed_mixed, x.data(), rows.data(), active_rows, y_mixed_selected.data());
        },
                y_mixed_selected,
                options.warmup,
                options.iters);
    result.scalar_ms = time_ms([&]() { eigenskill::scalar_skill_bypass(x.data(), y_scalar.data(), d, 0.875f); }, y_scalar, options.warmup, options.iters);
    return result;
}

void print_header() {
    std::cout << std::setw(6) << "d"
              << std::setw(8) << "rows"
              << std::setw(12) << "dense_ms"
              << std::setw(12) << "davx_ms"
              << std::setw(12) << "int4_ms"
              << std::setw(12) << "int3_ms"
              << std::setw(12) << "mix_ms"
              << std::setw(12) << "sel_ms"
              << std::setw(12) << "selavx_ms"
              << std::setw(12) << "mixsel_ms"
              << std::setw(12) << "scalar_ms"
              << std::setw(12) << "davx_x"
              << std::setw(12) << "int4_x"
              << std::setw(12) << "int3_x"
              << std::setw(12) << "mix_x"
              << std::setw(12) << "sel_x"
              << std::setw(12) << "selavx_x"
              << std::setw(12) << "mixsel_x"
              << std::setw(12) << "scalar_x"
              << std::setw(13) << "davx_err"
              << std::setw(13) << "int4_err"
              << std::setw(13) << "int3_err"
              << std::setw(13) << "mix_err"
              << std::setw(13) << "sel_err"
              << std::setw(13) << "selavx_err"
              << std::setw(13) << "mixsel_err"
              << '\n';
}

void print_result(const Result& r) {
    std::cout << std::setw(6) << r.d
              << std::setw(8) << r.active_rows
              << std::setw(12) << std::fixed << std::setprecision(6) << r.dense_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.dense_avx2_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.int4_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.int3_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.mixed_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.selected_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.selected_avx2_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.mixed_selected_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.scalar_ms
              << std::setw(12) << std::fixed << std::setprecision(2) << r.dense_ms / r.dense_avx2_ms
              << std::setw(12) << std::fixed << std::setprecision(2) << r.dense_ms / r.int4_ms
              << std::setw(12) << std::fixed << std::setprecision(2) << r.dense_ms / r.int3_ms
              << std::setw(12) << std::fixed << std::setprecision(2) << r.dense_ms / r.mixed_ms
              << std::setw(12) << std::fixed << std::setprecision(2) << r.dense_ms / r.selected_ms
              << std::setw(12) << std::fixed << std::setprecision(2) << r.dense_ms / r.selected_avx2_ms
              << std::setw(12) << std::fixed << std::setprecision(2) << r.dense_ms / r.mixed_selected_ms
              << std::setw(12) << std::fixed << std::setprecision(2) << r.dense_ms / r.scalar_ms
              << std::setw(13) << std::scientific << std::setprecision(3) << r.dense_avx2_rel_l2
              << std::setw(13) << std::scientific << std::setprecision(3) << r.int4_rel_l2
              << std::setw(13) << std::scientific << std::setprecision(3) << r.int3_rel_l2
              << std::setw(13) << std::scientific << std::setprecision(3) << r.mixed_rel_l2
              << std::setw(13) << std::scientific << std::setprecision(3) << r.selected_rel_l2
              << std::setw(13) << std::scientific << std::setprecision(3) << r.selected_avx2_rel_l2
              << std::setw(13) << std::scientific << std::setprecision(3) << r.mixed_selected_rel_l2
              << '\n';
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        std::cout << "EigenSkill-Q C++ quant kernel benchmark\n";
        std::cout << "paths: fp32 GEMV, AVX2 fp32 GEMV when available, packed INT4/INT3/mixed-bit dequant GEMV, selected-row GEMV, scalar bypass\n";
        std::cout << "avx2=" << (eigenskill::has_avx2() ? "enabled" : "disabled") << "\n";
        std::cout << "iters=" << options.iters << " warmup=" << options.warmup << " seed=" << options.seed << "\n\n";

        print_header();
        for (int d : options.dims) {
            for (int rows : options.active_rows) {
                if (rows > d) {
                    continue;
                }
                print_result(benchmark_case(d, rows, options));
            }
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
