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

PackedInt4Matrix pack_int4_per_row(const float* w, int rows, int cols) {
    if (!w || rows <= 0 || cols <= 0) {
        throw std::invalid_argument("invalid INT4 pack input");
    }
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
    if (packed.rows <= 0 || packed.cols <= 0 || !x || !y) {
        throw std::invalid_argument("invalid INT4 GEMV input");
    }
    const std::size_t expected_bytes = (static_cast<std::size_t>(packed.rows) * packed.cols + 1) / 2;
    if (packed.bytes.size() != expected_bytes || packed.row_scales.size() != static_cast<std::size_t>(packed.rows)) {
        throw std::invalid_argument("inconsistent packed INT4 matrix");
    }
    for (int row = 0; row < packed.rows; ++row) {
        float acc = 0.0f;
        const float scale = packed.row_scales[row];
        const std::size_t base = static_cast<std::size_t>(row) * packed.cols;
        for (int col = 0; col < packed.cols; ++col) {
            const std::size_t linear = base + col;
            const std::uint8_t byte = packed.bytes[linear / 2];
            const std::int8_t q = unpack_signed_nibble(byte, (linear & 1u) != 0);
            acc += static_cast<float>(q) * scale * x[col];
        }
        y[row] = acc;
    }
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
