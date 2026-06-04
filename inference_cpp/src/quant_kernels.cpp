#include "eigenskill/quant_kernels.hpp"

#include <algorithm>
#include <cmath>
#include <stdexcept>

#if defined(__AVX2__) || (defined(_MSC_VER) && defined(__AVX2__))
#include <immintrin.h>
#define EIGENSKILL_KERNEL_HAS_AVX2 1
#else
#define EIGENSKILL_KERNEL_HAS_AVX2 0
#endif

#if defined(_MSC_VER)
#define EIGENSKILL_RESTRICT __restrict
#define EIGENSKILL_NOINLINE __declspec(noinline)
#else
#define EIGENSKILL_RESTRICT __restrict__
#define EIGENSKILL_NOINLINE __attribute__((noinline))
#endif

namespace eigenskill {

namespace {

void require_matrix(MatrixView w) {
    if (!w.data || w.rows <= 0 || w.cols <= 0) {
        throw std::invalid_argument("invalid matrix view");
    }
}

#if EIGENSKILL_KERNEL_HAS_AVX2
float horizontal_sum_avx(__m256 value) {
    __m128 low = _mm256_castps256_ps128(value);
    __m128 high = _mm256_extractf128_ps(value, 1);
    __m128 sum = _mm_add_ps(low, high);
    sum = _mm_hadd_ps(sum, sum);
    sum = _mm_hadd_ps(sum, sum);
    return _mm_cvtss_f32(sum);
}
#endif

}  // namespace

bool has_avx2() noexcept {
    return EIGENSKILL_KERNEL_HAS_AVX2 != 0;
}

EIGENSKILL_NOINLINE float dot_product_scalar(const float* EIGENSKILL_RESTRICT a,
                                             const float* EIGENSKILL_RESTRICT b,
                                             int n) {
    if (!a || !b || n < 0) {
        throw std::invalid_argument("invalid dot product input");
    }
    float acc = 0.0f;
    for (int i = 0; i < n; ++i) {
        acc += a[i] * b[i];
    }
    return acc;
}

EIGENSKILL_NOINLINE float dot_product_avx2(const float* EIGENSKILL_RESTRICT a,
                                           const float* EIGENSKILL_RESTRICT b,
                                           int n) {
    if (!a || !b || n < 0) {
        throw std::invalid_argument("invalid dot product input");
    }
#if EIGENSKILL_KERNEL_HAS_AVX2
    __m256 acc = _mm256_setzero_ps();
    int i = 0;
    for (; i + 8 <= n; i += 8) {
        const __m256 va = _mm256_loadu_ps(a + i);
        const __m256 vb = _mm256_loadu_ps(b + i);
        acc = _mm256_add_ps(acc, _mm256_mul_ps(va, vb));
    }
    float sum = horizontal_sum_avx(acc);
    for (; i < n; ++i) {
        sum += a[i] * b[i];
    }
    return sum;
#else
    return dot_product_scalar(a, b, n);
#endif
}

EIGENSKILL_NOINLINE void dense_gemv(MatrixView w, const float* EIGENSKILL_RESTRICT x, float* EIGENSKILL_RESTRICT y) {
    require_matrix(w);
    if (!x || !y) {
        throw std::invalid_argument("invalid dense GEMV vector");
    }
    for (int row = 0; row < w.rows; ++row) {
        const float* wr = w.data + static_cast<std::size_t>(row) * w.cols;
        y[row] = dot_product_scalar(wr, x, w.cols);
    }
}

EIGENSKILL_NOINLINE void dense_gemv_avx2(MatrixView w, const float* EIGENSKILL_RESTRICT x, float* EIGENSKILL_RESTRICT y) {
    require_matrix(w);
    if (!x || !y) {
        throw std::invalid_argument("invalid AVX2 dense GEMV vector");
    }
    for (int row = 0; row < w.rows; ++row) {
        const float* wr = w.data + static_cast<std::size_t>(row) * w.cols;
        y[row] = dot_product_avx2(wr, x, w.cols);
    }
}

EIGENSKILL_NOINLINE void selected_rows_gemv(MatrixView w,
                                            const float* EIGENSKILL_RESTRICT x,
                                            const int* EIGENSKILL_RESTRICT rows,
                                            int active_rows,
                                            float* EIGENSKILL_RESTRICT y) {
    require_matrix(w);
    if (!x || !rows || !y || active_rows < 0) {
        throw std::invalid_argument("invalid selected-row GEMV input");
    }
    for (int out = 0; out < active_rows; ++out) {
        const int row = rows[out];
        if (row < 0 || row >= w.rows) {
            throw std::out_of_range("selected row index out of range");
        }
        const float* wr = w.data + static_cast<std::size_t>(row) * w.cols;
        y[out] = dot_product_scalar(wr, x, w.cols);
    }
}

EIGENSKILL_NOINLINE void selected_rows_gemv_avx2(MatrixView w,
                                                 const float* EIGENSKILL_RESTRICT x,
                                                 const int* EIGENSKILL_RESTRICT rows,
                                                 int active_rows,
                                                 float* EIGENSKILL_RESTRICT y) {
    require_matrix(w);
    if (!x || !rows || !y || active_rows < 0) {
        throw std::invalid_argument("invalid selected-row AVX2 GEMV input");
    }
    for (int out = 0; out < active_rows; ++out) {
        const int row = rows[out];
        if (row < 0 || row >= w.rows) {
            throw std::out_of_range("selected row index out of range");
        }
        const float* wr = w.data + static_cast<std::size_t>(row) * w.cols;
        y[out] = dot_product_avx2(wr, x, w.cols);
    }
}

EIGENSKILL_NOINLINE void scalar_skill_bypass(const float* EIGENSKILL_RESTRICT x,
                                             float* EIGENSKILL_RESTRICT y,
                                             int n,
                                             float lambda) {
    if (!x || !y || n < 0) {
        throw std::invalid_argument("invalid scalar bypass input");
    }
    for (int i = 0; i < n; ++i) {
        y[i] = lambda * x[i];
    }
}

std::int8_t unpack_signed_nibble(std::uint8_t byte, bool high) {
    const std::uint8_t nibble = high ? static_cast<std::uint8_t>(byte >> 4) : static_cast<std::uint8_t>(byte & 0x0f);
    const int signed_value = nibble >= 8 ? static_cast<int>(nibble) - 16 : static_cast<int>(nibble);
    return static_cast<std::int8_t>(signed_value);
}

void write_bits(std::vector<std::uint8_t>& bytes, std::size_t bit_offset, int bits, std::uint8_t value) {
    for (int bit = 0; bit < bits; ++bit) {
        const bool one = ((value >> bit) & 1u) != 0;
        const std::size_t absolute = bit_offset + static_cast<std::size_t>(bit);
        const std::size_t byte_index = absolute / 8;
        const std::uint8_t mask = static_cast<std::uint8_t>(1u << (absolute % 8));
        if (one) {
            bytes[byte_index] = static_cast<std::uint8_t>(bytes[byte_index] | mask);
        } else {
            bytes[byte_index] = static_cast<std::uint8_t>(bytes[byte_index] & ~mask);
        }
    }
}

std::int8_t unpack_signed_bits(const std::uint8_t* bytes, std::size_t bit_offset, int bits) {
    if (!bytes || bits <= 0 || bits > 7) {
        throw std::invalid_argument("invalid signed bit unpack input");
    }
    std::uint8_t encoded = 0;
    for (int bit = 0; bit < bits; ++bit) {
        const std::size_t absolute = bit_offset + static_cast<std::size_t>(bit);
        const std::uint8_t byte = bytes[absolute / 8];
        const std::uint8_t one = static_cast<std::uint8_t>((byte >> (absolute % 8)) & 1u);
        encoded = static_cast<std::uint8_t>(encoded | (one << bit));
    }
    const int sign = 1 << (bits - 1);
    const int full = 1 << bits;
    const int signed_value = (encoded & sign) ? static_cast<int>(encoded) - full : static_cast<int>(encoded);
    return static_cast<std::int8_t>(signed_value);
}

PackedLowBitMatrix pack_lowbit_per_row(const float* w, int rows, int cols, int bits) {
    if (!w || rows <= 0 || cols <= 0) {
        throw std::invalid_argument("invalid low-bit pack input");
    }
    if (bits < 2 || bits > 7) {
        throw std::invalid_argument("low-bit pack supports 2..7 bits");
    }
    PackedLowBitMatrix packed;
    packed.rows = rows;
    packed.cols = cols;
    packed.bits = bits;
    const std::size_t values = static_cast<std::size_t>(rows) * cols;
    packed.bytes.assign((values * static_cast<std::size_t>(bits) + 7) / 8, 0);
    packed.row_scales.assign(rows, 1.0f);
    const int qmax = (1 << (bits - 1)) - 1;

    for (int row = 0; row < rows; ++row) {
        float max_abs = 0.0f;
        for (int col = 0; col < cols; ++col) {
            max_abs = std::max(max_abs, std::fabs(w[static_cast<std::size_t>(row) * cols + col]));
        }
        const float scale = std::max(max_abs / static_cast<float>(qmax), 1.0e-8f);
        packed.row_scales[row] = scale;
        for (int col = 0; col < cols; ++col) {
            const float value = w[static_cast<std::size_t>(row) * cols + col] / scale;
            int q = static_cast<int>(std::nearbyint(value));
            q = std::max(-qmax, std::min(qmax, q));
            const int full = 1 << bits;
            const std::uint8_t encoded = static_cast<std::uint8_t>(q < 0 ? q + full : q);
            const std::size_t linear = static_cast<std::size_t>(row) * cols + col;
            write_bits(packed.bytes, linear * static_cast<std::size_t>(bits), bits, encoded);
        }
    }
    return packed;
}

PackedInt4Matrix pack_int4_per_row(const float* w, int rows, int cols) {
    PackedLowBitMatrix low = pack_lowbit_per_row(w, rows, cols, 4);
    PackedInt4Matrix packed;
    packed.rows = low.rows;
    packed.cols = low.cols;
    packed.bytes = std::move(low.bytes);
    packed.row_scales = std::move(low.row_scales);
    return packed;
}

EIGENSKILL_NOINLINE void lowbit_dequant_gemv(const PackedLowBitMatrix& packed,
                                             const float* EIGENSKILL_RESTRICT x,
                                             float* EIGENSKILL_RESTRICT y) {
    if (packed.rows <= 0 || packed.cols <= 0 || packed.bits < 2 || packed.bits > 7 || !x || !y) {
        throw std::invalid_argument("invalid low-bit GEMV input");
    }
    const std::size_t values = static_cast<std::size_t>(packed.rows) * packed.cols;
    const std::size_t expected_bytes = (values * static_cast<std::size_t>(packed.bits) + 7) / 8;
    if (packed.bytes.size() != expected_bytes || packed.row_scales.size() != static_cast<std::size_t>(packed.rows)) {
        throw std::invalid_argument("inconsistent packed low-bit matrix");
    }
    for (int row = 0; row < packed.rows; ++row) {
        float acc = 0.0f;
        const float scale = packed.row_scales[row];
        const std::size_t base = static_cast<std::size_t>(row) * packed.cols;
        for (int col = 0; col < packed.cols; ++col) {
            const std::size_t linear = base + col;
            const std::int8_t q = unpack_signed_bits(
                packed.bytes.data(),
                linear * static_cast<std::size_t>(packed.bits),
                packed.bits);
            acc += static_cast<float>(q) * scale * x[col];
        }
        y[row] = acc;
    }
}

EIGENSKILL_NOINLINE void int4_dequant_gemv(const PackedInt4Matrix& packed,
                                           const float* EIGENSKILL_RESTRICT x,
                                           float* EIGENSKILL_RESTRICT y) {
    if (packed.rows <= 0 || packed.cols <= 0 || !x || !y) {
        throw std::invalid_argument("invalid INT4 GEMV input");
    }
    PackedLowBitMatrix low;
    low.rows = packed.rows;
    low.cols = packed.cols;
    low.bits = 4;
    low.bytes = packed.bytes;
    low.row_scales = packed.row_scales;
    lowbit_dequant_gemv(low, x, y);
}

double rel_l2_error(const float* lhs, const float* rhs, int n) {
    if (!lhs || !rhs || n < 0) {
        throw std::invalid_argument("invalid rel_l2 input");
    }
    double err2 = 0.0;
    double ref2 = 0.0;
    for (int i = 0; i < n; ++i) {
        const double diff = static_cast<double>(lhs[i]) - rhs[i];
        err2 += diff * diff;
        ref2 += static_cast<double>(rhs[i]) * rhs[i];
    }
    return std::sqrt(err2 / std::max(ref2, 1.0e-30));
}

}  // namespace eigenskill
