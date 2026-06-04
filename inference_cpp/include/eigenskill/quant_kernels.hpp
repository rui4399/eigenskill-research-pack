#pragma once

#include <cstdint>
#include <vector>

namespace eigenskill {

struct MatrixView {
    const float* data = nullptr;
    int rows = 0;
    int cols = 0;
};

struct PackedInt4Matrix {
    int rows = 0;
    int cols = 0;
    std::vector<std::uint8_t> bytes;
    std::vector<float> row_scales;
};

bool has_avx2() noexcept;

float dot_product_scalar(const float* a, const float* b, int n);
float dot_product_avx2(const float* a, const float* b, int n);

void dense_gemv(MatrixView w, const float* x, float* y);
void dense_gemv_avx2(MatrixView w, const float* x, float* y);

void selected_rows_gemv(MatrixView w, const float* x, const int* rows, int active_rows, float* y);
void selected_rows_gemv_avx2(MatrixView w, const float* x, const int* rows, int active_rows, float* y);

void scalar_skill_bypass(const float* x, float* y, int n, float lambda);

PackedInt4Matrix pack_int4_per_row(const float* w, int rows, int cols);
std::int8_t unpack_signed_nibble(std::uint8_t byte, bool high);
void int4_dequant_gemv(const PackedInt4Matrix& packed, const float* x, float* y);

double rel_l2_error(const float* lhs, const float* rhs, int n);

}  // namespace eigenskill
