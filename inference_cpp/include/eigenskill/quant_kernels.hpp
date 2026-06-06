#pragma once

#include <cstdint>
#include <cstddef>
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
    std::vector<int> row_sums;
};

struct PackedLowBitMatrix {
    int rows = 0;
    int cols = 0;
    int bits = 0;
    std::vector<std::uint8_t> bytes;
    std::vector<float> row_scales;
};

struct PackedMixedBitMatrix {
    int rows = 0;
    int cols = 0;
    std::vector<std::uint8_t> row_bits;
    std::vector<std::uint64_t> row_bit_offsets;
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
void int4_selected_rows_gemv(
    const PackedInt4Matrix& packed,
    const float* x,
    const int* rows,
    int active_rows,
    float* y);
void int4_maddubs_gemv(const PackedInt4Matrix& packed, const float* x, float* y);
void int4_maddubs_selected_rows_gemv(
    const PackedInt4Matrix& packed,
    const float* x,
    const int* rows,
    int active_rows,
    float* y);

PackedLowBitMatrix pack_lowbit_per_row(const float* w, int rows, int cols, int bits);
std::int8_t unpack_signed_bits(const std::uint8_t* bytes, std::size_t bit_offset, int bits);
void lowbit_dequant_gemv(const PackedLowBitMatrix& packed, const float* x, float* y);

PackedMixedBitMatrix pack_mixed_lowbit_per_row(const float* w, int rows, int cols, const std::uint8_t* row_bits);
void mixed_lowbit_dequant_gemv(const PackedMixedBitMatrix& packed, const float* x, float* y);
void mixed_lowbit_selected_rows_gemv(
    const PackedMixedBitMatrix& packed,
    const float* x,
    const int* rows,
    int active_rows,
    float* y);

double rel_l2_error(const float* lhs, const float* rhs, int n);

}  // namespace eigenskill
