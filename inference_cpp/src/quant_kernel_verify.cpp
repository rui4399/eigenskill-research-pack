#include "eigenskill/quant_kernels.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Options {
    int dim = 512;
    int active_rows = 32;
    std::uint32_t seed = 20260604;
    double tolerance = 1.0e-4;
};

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
        if (arg == "--dim") {
            options.dim = std::stoi(require_value("--dim"));
        } else if (arg == "--active-rows") {
            options.active_rows = std::stoi(require_value("--active-rows"));
        } else if (arg == "--seed") {
            options.seed = static_cast<std::uint32_t>(std::stoul(require_value("--seed")));
        } else if (arg == "--tolerance") {
            options.tolerance = std::stod(require_value("--tolerance"));
        } else if (arg == "--help" || arg == "-h") {
            std::cout << "Usage: quant_kernel_verify [--dim 512] [--active-rows 32] [--seed 20260604] [--tolerance 1e-4]\n";
            std::exit(0);
        } else {
            throw std::runtime_error("unknown argument: " + arg);
        }
    }
    if (options.dim <= 0 || options.active_rows <= 0 || options.active_rows > options.dim || options.tolerance <= 0.0) {
        throw std::runtime_error("invalid --dim, --active-rows, or --tolerance");
    }
    return options;
}

std::vector<float> random_vector(std::size_t n, std::mt19937& rng, float scale) {
    std::normal_distribution<float> dist(0.0f, scale);
    std::vector<float> out(n);
    for (float& value : out) {
        value = dist(rng);
    }
    return out;
}

std::vector<int> make_active_rows(int dim, int active_rows) {
    std::vector<int> rows(static_cast<std::size_t>(active_rows));
    const double step = static_cast<double>(dim) / static_cast<double>(active_rows);
    for (int i = 0; i < active_rows; ++i) {
        rows[static_cast<std::size_t>(i)] = std::min(dim - 1, static_cast<int>(i * step));
    }
    return rows;
}

void print_bool(std::ostream& out, bool value) {
    out << (value ? "true" : "false");
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_args(argc, argv);
        std::mt19937 rng(options.seed);
        std::vector<float> w = random_vector(static_cast<std::size_t>(options.dim) * options.dim, rng, 0.04f);
        std::vector<float> x = random_vector(options.dim, rng, 1.0f);
        std::vector<int> rows = make_active_rows(options.dim, options.active_rows);

        eigenskill::MatrixView matrix{w.data(), options.dim, options.dim};
        eigenskill::PackedInt4Matrix int4 = eigenskill::pack_int4_per_row(w.data(), options.dim, options.dim);
        eigenskill::PackedLowBitMatrix int3 = eigenskill::pack_lowbit_per_row(w.data(), options.dim, options.dim, 3);

        std::vector<float> dense(options.dim, 0.0f);
        std::vector<float> dense_avx2(options.dim, 0.0f);
        std::vector<float> int4_out(options.dim, 0.0f);
        std::vector<float> int3_out(options.dim, 0.0f);
        std::vector<float> selected(options.active_rows, 0.0f);
        std::vector<float> selected_avx2(options.active_rows, 0.0f);
        std::vector<float> selected_ref(options.active_rows, 0.0f);
        std::vector<float> bypass(options.dim, 0.0f);
        std::vector<float> bypass_ref(options.dim, 0.0f);

        eigenskill::dense_gemv(matrix, x.data(), dense.data());
        eigenskill::dense_gemv_avx2(matrix, x.data(), dense_avx2.data());
        eigenskill::int4_dequant_gemv(int4, x.data(), int4_out.data());
        eigenskill::lowbit_dequant_gemv(int3, x.data(), int3_out.data());
        eigenskill::selected_rows_gemv(matrix, x.data(), rows.data(), options.active_rows, selected.data());
        eigenskill::selected_rows_gemv_avx2(matrix, x.data(), rows.data(), options.active_rows, selected_avx2.data());
        eigenskill::scalar_skill_bypass(x.data(), bypass.data(), options.dim, 0.875f);
        for (int i = 0; i < options.active_rows; ++i) {
            selected_ref[static_cast<std::size_t>(i)] = dense[static_cast<std::size_t>(rows[static_cast<std::size_t>(i)])];
        }
        for (int i = 0; i < options.dim; ++i) {
            bypass_ref[static_cast<std::size_t>(i)] = 0.875f * x[static_cast<std::size_t>(i)];
        }

        const double dense_avx2_err = eigenskill::rel_l2_error(dense_avx2.data(), dense.data(), options.dim);
        const double selected_err = eigenskill::rel_l2_error(selected.data(), selected_ref.data(), options.active_rows);
        const double selected_avx2_err = eigenskill::rel_l2_error(selected_avx2.data(), selected_ref.data(), options.active_rows);
        const double int4_err = eigenskill::rel_l2_error(int4_out.data(), dense.data(), options.dim);
        const double int3_err = eigenskill::rel_l2_error(int3_out.data(), dense.data(), options.dim);
        const double bypass_err = eigenskill::rel_l2_error(bypass.data(), bypass_ref.data(), options.dim);

        const bool dense_avx2_ok = dense_avx2_err <= options.tolerance;
        const bool selected_ok = selected_err <= options.tolerance;
        const bool selected_avx2_ok = selected_avx2_err <= options.tolerance;
        const bool int4_ok = std::isfinite(int4_err);
        const bool int3_ok = std::isfinite(int3_err);
        const bool bypass_ok = bypass_err <= options.tolerance;
        const bool ok = dense_avx2_ok && selected_ok && selected_avx2_ok && int4_ok && int3_ok && bypass_ok;

        std::cout << std::scientific << std::setprecision(9);
        std::cout << "{\n";
        std::cout << "  \"dim\": " << options.dim << ",\n";
        std::cout << "  \"active_rows\": " << options.active_rows << ",\n";
        std::cout << "  \"seed\": " << options.seed << ",\n";
        std::cout << "  \"tolerance\": " << options.tolerance << ",\n";
        std::cout << "  \"avx2\": ";
        print_bool(std::cout, eigenskill::has_avx2());
        std::cout << ",\n";
        std::cout << "  \"errors\": {\n";
        std::cout << "    \"dense_avx2_rel_l2\": " << dense_avx2_err << ",\n";
        std::cout << "    \"selected_rel_l2\": " << selected_err << ",\n";
        std::cout << "    \"selected_avx2_rel_l2\": " << selected_avx2_err << ",\n";
        std::cout << "    \"int4_rel_l2\": " << int4_err << ",\n";
        std::cout << "    \"int3_rel_l2\": " << int3_err << ",\n";
        std::cout << "    \"bypass_rel_l2\": " << bypass_err << "\n";
        std::cout << "  },\n";
        std::cout << "  \"checks\": {\n";
        std::cout << "    \"dense_avx2\": ";
        print_bool(std::cout, dense_avx2_ok);
        std::cout << ",\n";
        std::cout << "    \"selected\": ";
        print_bool(std::cout, selected_ok);
        std::cout << ",\n";
        std::cout << "    \"selected_avx2\": ";
        print_bool(std::cout, selected_avx2_ok);
        std::cout << ",\n";
        std::cout << "    \"int4_finite\": ";
        print_bool(std::cout, int4_ok);
        std::cout << ",\n";
        std::cout << "    \"int3_finite\": ";
        print_bool(std::cout, int3_ok);
        std::cout << ",\n";
        std::cout << "    \"bypass\": ";
        print_bool(std::cout, bypass_ok);
        std::cout << "\n";
        std::cout << "  },\n";
        std::cout << "  \"ok\": ";
        print_bool(std::cout, ok);
        std::cout << "\n";
        std::cout << "}\n";
        return ok ? 0 : 1;
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
