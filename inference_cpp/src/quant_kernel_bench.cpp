#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

#if defined(_MSC_VER)
#define EIGENSKILL_RESTRICT __restrict
#define EIGENSKILL_NOINLINE __declspec(noinline)
#else
#define EIGENSKILL_RESTRICT __restrict__
#define EIGENSKILL_NOINLINE __attribute__((noinline))
#endif

namespace eigenskill {

using Clock = std::chrono::steady_clock;

volatile float g_sink = 0.0f;

struct Options {
    std::vector<int> dims{512, 1024, 2048};
    std::vector<int> active_rows{16, 64, 256};
    int iters = 200;
    int warmup = 20;
    std::uint32_t seed = 20260604;
};

struct PackedInt4Matrix {
    int rows = 0;
    int cols = 0;
    std::vector<std::uint8_t> bytes;
    std::vector<float> row_scales;
};

struct Result {
    int d = 0;
    int active_rows = 0;
    double dense_ms = 0.0;
    double int4_ms = 0.0;
    double selected_ms = 0.0;
    double scalar_ms = 0.0;
    double int4_rel_l2 = 0.0;
    double selected_rel_l2 = 0.0;
    double int4_speedup = 0.0;
    double selected_speedup = 0.0;
    double scalar_speedup = 0.0;
};

std::vector<int> parse_list(const std::string& text) {
    std::vector<int> values;
    std::stringstream ss(text);
    std::string item;
    while (std::getline(ss, item, ',')) {
        if (!item.empty()) values.push_back(std::stoi(item));
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

std::vector<float> random_vector(std::size_t n, std::mt19937& rng, float scale = 1.0f) {
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
    if (active_rows <= 0) return rows;
    const double step = static_cast<double>(d) / static_cast<double>(active_rows);
    for (int i = 0; i < active_rows; ++i) {
        rows[static_cast<std::size_t>(i)] = std::min(d - 1, static_cast<int>(i * step));
    }
    return rows;
}

EIGENSKILL_NOINLINE void dense_gemv(const float* EIGENSKILL_RESTRICT w,
                                    const float* EIGENSKILL_RESTRICT x,
                                    float* EIGENSKILL_RESTRICT y,
                                    int rows,
                                    int cols) {
    for (int row = 0; row < rows; ++row) {
        const float* wr = w + static_cast<std::size_t>(row) * cols;
        float acc = 0.0f;
        for (int col = 0; col < cols; ++col) {
            acc += wr[col] * x[col];
        }
        y[row] = acc;
    }
}

EIGENSKILL_NOINLINE void selected_rows_gemv(const float* EIGENSKILL_RESTRICT w,
                                            const float* EIGENSKILL_RESTRICT x,
                                            const int* EIGENSKILL_RESTRICT rows,
                                            float* EIGENSKILL_RESTRICT y,
                                            int active_rows,
                                            int cols) {
    for (int out = 0; out < active_rows; ++out) {
        const int row = rows[out];
        const float* wr = w + static_cast<std::size_t>(row) * cols;
        float acc = 0.0f;
        for (int col = 0; col < cols; ++col) {
            acc += wr[col] * x[col];
        }
        y[out] = acc;
    }
}

EIGENSKILL_NOINLINE void scalar_skill_bypass(const float* EIGENSKILL_RESTRICT x,
                                             float* EIGENSKILL_RESTRICT y,
                                             int d,
                                             float lambda) {
    for (int i = 0; i < d; ++i) {
        y[i] = lambda * x[i];
    }
}

std::int8_t unpack_signed_nibble(std::uint8_t byte, bool high) {
    std::uint8_t nibble = high ? static_cast<std::uint8_t>(byte >> 4) : static_cast<std::uint8_t>(byte & 0x0f);
    const int signed_value = nibble >= 8 ? static_cast<int>(nibble) - 16 : static_cast<int>(nibble);
    return static_cast<std::int8_t>(signed_value);
}

PackedInt4Matrix pack_int4_per_row(const std::vector<float>& w, int rows, int cols) {
    PackedInt4Matrix packed;
    packed.rows = rows;
    packed.cols = cols;
    packed.bytes.assign((static_cast<std::size_t>(rows) * cols + 1) / 2, 0);
    packed.row_scales.assign(rows, 1.0f);

    for (int row = 0; row < rows; ++row) {
        float max_abs = 0.0f;
        for (int col = 0; col < cols; ++col) {
            max_abs = std::max(max_abs, std::fabs(w[static_cast<std::size_t>(row) * cols + col]));
        }
        const float scale = std::max(max_abs / 7.0f, 1.0e-8f);
        packed.row_scales[row] = scale;

        for (int col = 0; col < cols; ++col) {
            const float value = w[static_cast<std::size_t>(row) * cols + col] / scale;
            int q = static_cast<int>(std::nearbyint(value));
            q = std::max(-7, std::min(7, q));
            const std::uint8_t encoded = static_cast<std::uint8_t>(q < 0 ? q + 16 : q);
            const std::size_t linear = static_cast<std::size_t>(row) * cols + col;
            const std::size_t byte_index = linear / 2;
            if ((linear & 1u) == 0) {
                packed.bytes[byte_index] = static_cast<std::uint8_t>((packed.bytes[byte_index] & 0xf0u) | encoded);
            } else {
                packed.bytes[byte_index] = static_cast<std::uint8_t>((packed.bytes[byte_index] & 0x0fu) | (encoded << 4));
            }
        }
    }
    return packed;
}

EIGENSKILL_NOINLINE void int4_dequant_gemv(const PackedInt4Matrix& packed,
                                           const float* EIGENSKILL_RESTRICT x,
                                           float* EIGENSKILL_RESTRICT y) {
    const int rows = packed.rows;
    const int cols = packed.cols;
    for (int row = 0; row < rows; ++row) {
        float acc = 0.0f;
        const float scale = packed.row_scales[row];
        const std::size_t base = static_cast<std::size_t>(row) * cols;
        for (int col = 0; col < cols; ++col) {
            const std::size_t linear = base + col;
            const std::uint8_t byte = packed.bytes[linear / 2];
            const std::int8_t q = unpack_signed_nibble(byte, (linear & 1u) != 0);
            acc += static_cast<float>(q) * scale * x[col];
        }
        y[row] = acc;
    }
}

double rel_l2_error(const std::vector<float>& lhs, const std::vector<float>& rhs) {
    double err2 = 0.0;
    double ref2 = 0.0;
    const std::size_t n = std::min(lhs.size(), rhs.size());
    for (std::size_t i = 0; i < n; ++i) {
        const double diff = static_cast<double>(lhs[i]) - rhs[i];
        err2 += diff * diff;
        ref2 += static_cast<double>(rhs[i]) * rhs[i];
    }
    return std::sqrt(err2 / std::max(ref2, 1.0e-30));
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
    std::vector<float> x = random_vector(d, rng, 1.0f);
    std::vector<int> rows = make_active_rows(d, active_rows);
    PackedInt4Matrix packed = pack_int4_per_row(w, d, d);

    std::vector<float> y_dense(d, 0.0f);
    std::vector<float> y_int4(d, 0.0f);
    std::vector<float> y_selected(active_rows, 0.0f);
    std::vector<float> y_selected_ref(active_rows, 0.0f);
    std::vector<float> y_scalar(d, 0.0f);

    dense_gemv(w.data(), x.data(), y_dense.data(), d, d);
    int4_dequant_gemv(packed, x.data(), y_int4.data());
    selected_rows_gemv(w.data(), x.data(), rows.data(), y_selected.data(), active_rows, d);
    for (int i = 0; i < active_rows; ++i) {
        y_selected_ref[i] = y_dense[rows[i]];
    }
    scalar_skill_bypass(x.data(), y_scalar.data(), d, 0.875f);

    Result result;
    result.d = d;
    result.active_rows = active_rows;
    result.int4_rel_l2 = rel_l2_error(y_int4, y_dense);
    result.selected_rel_l2 = rel_l2_error(y_selected, y_selected_ref);

    result.dense_ms = time_ms(
        [&]() { dense_gemv(w.data(), x.data(), y_dense.data(), d, d); },
        y_dense,
        options.warmup,
        options.iters);
    result.int4_ms = time_ms(
        [&]() { int4_dequant_gemv(packed, x.data(), y_int4.data()); },
        y_int4,
        options.warmup,
        options.iters);
    result.selected_ms = time_ms(
        [&]() { selected_rows_gemv(w.data(), x.data(), rows.data(), y_selected.data(), active_rows, d); },
        y_selected,
        options.warmup,
        options.iters);
    result.scalar_ms = time_ms(
        [&]() { scalar_skill_bypass(x.data(), y_scalar.data(), d, 0.875f); },
        y_scalar,
        options.warmup,
        options.iters);

    result.int4_speedup = result.dense_ms / result.int4_ms;
    result.selected_speedup = result.dense_ms / result.selected_ms;
    result.scalar_speedup = result.dense_ms / result.scalar_ms;
    return result;
}

void print_header() {
    std::cout << std::setw(6) << "d"
              << std::setw(8) << "rows"
              << std::setw(12) << "dense_ms"
              << std::setw(12) << "int4_ms"
              << std::setw(12) << "sel_ms"
              << std::setw(12) << "scalar_ms"
              << std::setw(12) << "int4_x"
              << std::setw(12) << "sel_x"
              << std::setw(12) << "scalar_x"
              << std::setw(13) << "int4_err"
              << std::setw(13) << "sel_err"
              << '\n';
}

void print_result(const Result& r) {
    std::cout << std::setw(6) << r.d
              << std::setw(8) << r.active_rows
              << std::setw(12) << std::fixed << std::setprecision(6) << r.dense_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.int4_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.selected_ms
              << std::setw(12) << std::fixed << std::setprecision(6) << r.scalar_ms
              << std::setw(12) << std::fixed << std::setprecision(2) << r.int4_speedup
              << std::setw(12) << std::fixed << std::setprecision(2) << r.selected_speedup
              << std::setw(12) << std::fixed << std::setprecision(2) << r.scalar_speedup
              << std::setw(13) << std::scientific << std::setprecision(3) << r.int4_rel_l2
              << std::setw(13) << std::scientific << std::setprecision(3) << r.selected_rel_l2
              << '\n';
}

}  // namespace eigenskill

int main(int argc, char** argv) {
    try {
        const eigenskill::Options options = eigenskill::parse_args(argc, argv);
        std::cout << "EigenSkill-Q C++ quant kernel benchmark\n";
        std::cout << "paths: fp32 dense GEMV, packed int4 dequant GEMV, selected-row GEMV, scalar bypass\n";
        std::cout << "iters=" << options.iters
                  << " warmup=" << options.warmup
                  << " seed=" << options.seed
                  << "\n\n";

        eigenskill::print_header();
        for (int d : options.dims) {
            for (int rows : options.active_rows) {
                if (rows > d) continue;
                const eigenskill::Result result = eigenskill::benchmark_case(d, rows, options);
                eigenskill::print_result(result);
            }
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
