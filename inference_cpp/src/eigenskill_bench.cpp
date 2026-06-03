#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

#if defined(_MSC_VER)
#define EIGENSKILL_RESTRICT __restrict
#else
#define EIGENSKILL_RESTRICT __restrict__
#endif

namespace eigenskill {

using Clock = std::chrono::steady_clock;

volatile float g_sink = 0.0f;

struct Options {
    std::vector<int> dims{512, 1024, 2048};
    std::vector<int> ks{1, 4, 8, 16, 32};
    int iters = 200;
    int warmup = 20;
    std::uint32_t seed = 42;
};

struct Result {
    int d = 0;
    int k = 0;
    double dense_ms = 0.0;
    double skill_ms = 0.0;
    double dense_gflops = 0.0;
    double skill_gflops = 0.0;
    double speedup = 0.0;
    double rel_l2_error = 0.0;
};

std::vector<int> parse_list(const std::string& text) {
    std::vector<int> values;
    std::stringstream ss(text);
    std::string item;
    while (std::getline(ss, item, ',')) {
        if (item.empty()) continue;
        values.push_back(std::stoi(item));
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
        } else if (arg == "--ks") {
            options.ks = parse_list(require_value("--ks"));
        } else if (arg == "--iters") {
            options.iters = std::stoi(require_value("--iters"));
        } else if (arg == "--warmup") {
            options.warmup = std::stoi(require_value("--warmup"));
        } else if (arg == "--seed") {
            options.seed = static_cast<std::uint32_t>(std::stoul(require_value("--seed")));
        } else if (arg == "--help" || arg == "-h") {
            std::cout
                << "Usage: eigenskill_bench [--dims 512,1024,2048] [--ks 1,4,8,16,32]\n"
                << "                         [--iters 200] [--warmup 20] [--seed 42]\n";
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

void orthonormalize_columns(std::vector<float>& u, int d, int k) {
    for (int col = 0; col < k; ++col) {
        for (int prev = 0; prev < col; ++prev) {
            double dot = 0.0;
            for (int row = 0; row < d; ++row) {
                dot += static_cast<double>(u[static_cast<std::size_t>(row) * k + col]) *
                       u[static_cast<std::size_t>(row) * k + prev];
            }
            for (int row = 0; row < d; ++row) {
                u[static_cast<std::size_t>(row) * k + col] -=
                    static_cast<float>(dot) * u[static_cast<std::size_t>(row) * k + prev];
            }
        }

        double norm2 = 0.0;
        for (int row = 0; row < d; ++row) {
            const float value = u[static_cast<std::size_t>(row) * k + col];
            norm2 += static_cast<double>(value) * value;
        }
        const float inv_norm = static_cast<float>(1.0 / std::sqrt(std::max(norm2, 1e-20)));
        for (int row = 0; row < d; ++row) {
            u[static_cast<std::size_t>(row) * k + col] *= inv_norm;
        }
    }
}

std::vector<float> make_stable_a(int k, std::mt19937& rng) {
    std::vector<float> a(static_cast<std::size_t>(k) * k, 0.0f);
    std::normal_distribution<float> noise(0.0f, 0.03f);
    for (int row = 0; row < k; ++row) {
        for (int col = 0; col < k; ++col) {
            const float diagonal = row == col ? 0.75f + 0.02f * static_cast<float>(row + 1) : 0.0f;
            a[static_cast<std::size_t>(row) * k + col] = diagonal + noise(rng);
        }
    }
    return a;
}

std::vector<float> make_skill_input(const std::vector<float>& u, int d, int k, std::mt19937& rng) {
    std::vector<float> coeff = random_vector(k, rng, 1.0f);
    std::vector<float> x = random_vector(d, rng, 0.01f);
    for (int row = 0; row < d; ++row) {
        float acc = x[row];
        for (int col = 0; col < k; ++col) {
            acc += u[static_cast<std::size_t>(row) * k + col] * coeff[col];
        }
        x[row] = acc;
    }
    return x;
}

void dense_gemv(const float* EIGENSKILL_RESTRICT w,
                const float* EIGENSKILL_RESTRICT x,
                float* EIGENSKILL_RESTRICT y,
                int d) {
    for (int row = 0; row < d; ++row) {
        const float* wr = w + static_cast<std::size_t>(row) * d;
        float acc = 0.0f;
        for (int col = 0; col < d; ++col) {
            acc += wr[col] * x[col];
        }
        y[row] = acc;
    }
}

void low_rank_skill_path(const float* EIGENSKILL_RESTRICT u,
                         const float* EIGENSKILL_RESTRICT a,
                         const float* EIGENSKILL_RESTRICT x,
                         float* EIGENSKILL_RESTRICT scratch_z,
                         float* EIGENSKILL_RESTRICT scratch_z2,
                         float* EIGENSKILL_RESTRICT y,
                         int d,
                         int k) {
    for (int col = 0; col < k; ++col) {
        float acc = 0.0f;
        for (int row = 0; row < d; ++row) {
            acc += u[static_cast<std::size_t>(row) * k + col] * x[row];
        }
        scratch_z[col] = acc;
    }

    for (int row = 0; row < k; ++row) {
        const float* ar = a + static_cast<std::size_t>(row) * k;
        float acc = 0.0f;
        for (int col = 0; col < k; ++col) {
            acc += ar[col] * scratch_z[col];
        }
        scratch_z2[row] = acc;
    }

    for (int row = 0; row < d; ++row) {
        const float* ur = u + static_cast<std::size_t>(row) * k;
        float acc = 0.0f;
        for (int col = 0; col < k; ++col) {
            acc += ur[col] * scratch_z2[col];
        }
        y[row] = acc;
    }
}

std::vector<float> materialize_w_from_uau(const std::vector<float>& u,
                                          const std::vector<float>& a,
                                          int d,
                                          int k) {
    std::vector<float> temp(static_cast<std::size_t>(d) * k, 0.0f);
    std::vector<float> w(static_cast<std::size_t>(d) * d, 0.0f);

    // temp = U A
    for (int row = 0; row < d; ++row) {
        for (int col = 0; col < k; ++col) {
            float acc = 0.0f;
            for (int inner = 0; inner < k; ++inner) {
                acc += u[static_cast<std::size_t>(row) * k + inner] *
                       a[static_cast<std::size_t>(inner) * k + col];
            }
            temp[static_cast<std::size_t>(row) * k + col] = acc;
        }
    }

    // W = temp U^T
    for (int row = 0; row < d; ++row) {
        for (int col = 0; col < d; ++col) {
            float acc = 0.0f;
            for (int inner = 0; inner < k; ++inner) {
                acc += temp[static_cast<std::size_t>(row) * k + inner] *
                       u[static_cast<std::size_t>(col) * k + inner];
            }
            w[static_cast<std::size_t>(row) * d + col] = acc;
        }
    }
    return w;
}

double rel_l2_error(const std::vector<float>& lhs, const std::vector<float>& rhs) {
    double err2 = 0.0;
    double ref2 = 0.0;
    for (std::size_t i = 0; i < lhs.size(); ++i) {
        const double diff = static_cast<double>(lhs[i]) - rhs[i];
        err2 += diff * diff;
        ref2 += static_cast<double>(rhs[i]) * rhs[i];
    }
    return std::sqrt(err2 / std::max(ref2, 1e-30));
}

template <typename Fn>
double time_ms(Fn&& fn, const std::vector<float>& output, int warmup, int iters) {
    for (int i = 0; i < warmup; ++i) {
        fn();
    }
    const auto start = Clock::now();
    for (int i = 0; i < iters; ++i) {
        fn();
    }
    const auto end = Clock::now();
    g_sink += output.empty() ? 0.0f : output[static_cast<std::size_t>(iters) % output.size()];
    const double elapsed_ms =
        std::chrono::duration<double, std::milli>(end - start).count();
    return elapsed_ms / static_cast<double>(iters);
}

Result benchmark_case(int d, int k, const Options& options) {
    if (k > d) {
        throw std::runtime_error("k must be <= d");
    }

    std::mt19937 rng(options.seed + static_cast<std::uint32_t>(d * 131 + k * 17));
    std::vector<float> u = random_vector(static_cast<std::size_t>(d) * k, rng, 1.0f);
    orthonormalize_columns(u, d, k);
    std::vector<float> a = make_stable_a(k, rng);
    std::vector<float> x = make_skill_input(u, d, k, rng);
    std::vector<float> w = materialize_w_from_uau(u, a, d, k);

    std::vector<float> y_dense(d, 0.0f);
    std::vector<float> y_skill(d, 0.0f);
    std::vector<float> z(k, 0.0f);
    std::vector<float> z2(k, 0.0f);

    dense_gemv(w.data(), x.data(), y_dense.data(), d);
    low_rank_skill_path(u.data(), a.data(), x.data(), z.data(), z2.data(), y_skill.data(), d, k);

    Result result;
    result.d = d;
    result.k = k;
    result.rel_l2_error = rel_l2_error(y_skill, y_dense);

    result.dense_ms = time_ms(
        [&]() { dense_gemv(w.data(), x.data(), y_dense.data(), d); },
        y_dense,
        options.warmup,
        options.iters);

    result.skill_ms = time_ms(
        [&]() { low_rank_skill_path(u.data(), a.data(), x.data(), z.data(), z2.data(), y_skill.data(), d, k); },
        y_skill,
        options.warmup,
        options.iters);

    const double dense_flops = 2.0 * static_cast<double>(d) * d;
    const double skill_flops = 4.0 * static_cast<double>(d) * k +
                               2.0 * static_cast<double>(k) * k;
    result.dense_gflops = dense_flops / (result.dense_ms * 1.0e6);
    result.skill_gflops = skill_flops / (result.skill_ms * 1.0e6);
    result.speedup = result.dense_ms / result.skill_ms;
    return result;
}

void print_header() {
    std::cout << std::setw(6) << "d"
              << std::setw(5) << "k"
              << std::setw(13) << "dense_ms"
              << std::setw(13) << "skill_ms"
              << std::setw(11) << "speedup"
              << std::setw(15) << "dense_GF/s"
              << std::setw(15) << "skill_GF/s"
              << std::setw(15) << "rel_l2_err"
              << '\n';
}

void print_result(const Result& r) {
    std::cout << std::setw(6) << r.d
              << std::setw(5) << r.k
              << std::setw(13) << std::fixed << std::setprecision(6) << r.dense_ms
              << std::setw(13) << std::fixed << std::setprecision(6) << r.skill_ms
              << std::setw(11) << std::fixed << std::setprecision(2) << r.speedup
              << std::setw(15) << std::fixed << std::setprecision(3) << r.dense_gflops
              << std::setw(15) << std::fixed << std::setprecision(3) << r.skill_gflops
              << std::setw(15) << std::scientific << std::setprecision(3) << r.rel_l2_error
              << '\n';
}

}  // namespace eigenskill

int main(int argc, char** argv) {
    try {
        const eigenskill::Options options = eigenskill::parse_args(argc, argv);
        std::cout << "EigenSkill C++ microbenchmark: dense GEMV vs low-rank skill path\n";
        std::cout << "iters=" << options.iters
                  << " warmup=" << options.warmup
                  << " seed=" << options.seed
                  << "\n\n";

        eigenskill::print_header();
        for (int d : options.dims) {
            for (int k : options.ks) {
                if (k > d) continue;
                const eigenskill::Result result = eigenskill::benchmark_case(d, k, options);
                eigenskill::print_result(result);
            }
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
