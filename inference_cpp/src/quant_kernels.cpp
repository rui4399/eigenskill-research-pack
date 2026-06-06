#include "eigenskill/quant_kernels.hpp"

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <stdexcept>
#include <vector>

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

void require_mixed_matrix(const PackedMixedBitMatrix& packed) {
    if (packed.rows <= 0 || packed.cols <= 0 ||
        packed.row_bits.size() != static_cast<std::size_t>(packed.rows) ||
        packed.row_bit_offsets.size() != static_cast<std::size_t>(packed.rows) ||
        packed.row_scales.size() != static_cast<std::size_t>(packed.rows)) {
        throw std::invalid_argument("inconsistent mixed low-bit matrix metadata");
    }

    std::uint64_t expected_bits = 0;
    for (int row = 0; row < packed.rows; ++row) {
        const std::size_t index = static_cast<std::size_t>(row);
        const int bits = static_cast<int>(packed.row_bits[index]);
        if (bits < 2 || bits > 8) {
            throw std::invalid_argument("mixed low-bit matrix supports 2..8 bits per row");
        }
        if (packed.row_bit_offsets[index] != expected_bits) {
            throw std::invalid_argument("mixed low-bit row offsets are not contiguous");
        }
        expected_bits += static_cast<std::uint64_t>(bits) * static_cast<std::uint64_t>(packed.cols);
    }
    const std::size_t expected_bytes = static_cast<std::size_t>((expected_bits + 7u) / 8u);
    if (packed.bytes.size() != expected_bytes) {
        throw std::invalid_argument("inconsistent mixed low-bit matrix storage");
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

inline __m128i sign_extend_int4_bytes(__m128i nibbles) {
    const __m128i low_mask = _mm_set1_epi8(0x0f);
    const __m128i sign = _mm_set1_epi8(0x08);
    nibbles = _mm_and_si128(nibbles, low_mask);
    return _mm_sub_epi8(_mm_xor_si128(nibbles, sign), sign);
}

inline __m256 dot_i8_f32_block8(__m128i q8, const float* EIGENSKILL_RESTRICT x) {
    const __m256 q = _mm256_cvtepi32_ps(_mm256_cvtepi8_epi32(q8));
    const __m256 vx = _mm256_loadu_ps(x);
    return _mm256_mul_ps(q, vx);
}

inline __m256i unpack_int4x32_to_i8x32(const std::uint8_t* EIGENSKILL_RESTRICT row_bytes) {
    const __m128i packed = _mm_loadu_si128(reinterpret_cast<const __m128i*>(row_bytes));
    const __m128i lo = sign_extend_int4_bytes(packed);
    const __m128i hi = sign_extend_int4_bytes(_mm_srli_epi16(packed, 4));
    const __m128i interleaved0 = _mm_unpacklo_epi8(lo, hi);
    const __m128i interleaved1 = _mm_unpackhi_epi8(lo, hi);
    return _mm256_set_m128i(interleaved1, interleaved0);
}

inline int horizontal_sum_i32_avx2(__m256i value) {
    const __m128i low = _mm256_castsi256_si128(value);
    const __m128i high = _mm256_extracti128_si256(value, 1);
    __m128i sum = _mm_add_epi32(low, high);
    sum = _mm_add_epi32(sum, _mm_shuffle_epi32(sum, _MM_SHUFFLE(2, 3, 0, 1)));
    sum = _mm_add_epi32(sum, _mm_shuffle_epi32(sum, _MM_SHUFFLE(1, 0, 3, 2)));
    return _mm_cvtsi128_si32(sum);
}

float int4_row_dot_avx2(const std::uint8_t* EIGENSKILL_RESTRICT row_bytes,
                        const float* EIGENSKILL_RESTRICT x,
                        int cols,
                        float scale) {
    __m256 acc = _mm256_setzero_ps();
    int col = 0;
    int byte_index = 0;
    for (; col + 32 <= cols; col += 32, byte_index += 16) {
        const __m256i q32 = unpack_int4x32_to_i8x32(row_bytes + byte_index);
        const __m128i interleaved0 = _mm256_castsi256_si128(q32);
        const __m128i interleaved1 = _mm256_extracti128_si256(q32, 1);
        acc = _mm256_add_ps(acc, dot_i8_f32_block8(interleaved0, x + col));
        acc = _mm256_add_ps(acc, dot_i8_f32_block8(_mm_srli_si128(interleaved0, 8), x + col + 8));
        acc = _mm256_add_ps(acc, dot_i8_f32_block8(interleaved1, x + col + 16));
        acc = _mm256_add_ps(acc, dot_i8_f32_block8(_mm_srli_si128(interleaved1, 8), x + col + 24));
    }
    float sum = horizontal_sum_avx(acc);
    for (; col < cols; ++col) {
        const std::uint8_t byte = row_bytes[static_cast<std::size_t>(col / 2)];
        const std::int8_t q = unpack_signed_nibble(byte, (col & 1) != 0);
        sum += static_cast<float>(q) * x[col];
    }
    return sum * scale;
}

int int4_u8_row_dot_maddubs_avx2(const std::uint8_t* EIGENSKILL_RESTRICT row_bytes,
                                 const std::uint8_t* EIGENSKILL_RESTRICT x_u8,
                                 int cols) {
    __m256i acc32 = _mm256_setzero_si256();
    const __m256i ones16 = _mm256_set1_epi16(1);
    int col = 0;
    int byte_index = 0;
    for (; col + 32 <= cols; col += 32, byte_index += 16) {
        const __m256i qx = _mm256_loadu_si256(reinterpret_cast<const __m256i*>(x_u8 + col));
        const __m256i qw = unpack_int4x32_to_i8x32(row_bytes + byte_index);
        const __m256i pair16 = _mm256_maddubs_epi16(qx, qw);
        const __m256i sum32 = _mm256_madd_epi16(pair16, ones16);
        acc32 = _mm256_add_epi32(acc32, sum32);
    }
    int sum = horizontal_sum_i32_avx2(acc32);
    for (; col < cols; ++col) {
        const std::uint8_t byte = row_bytes[static_cast<std::size_t>(col / 2)];
        const std::int8_t q = unpack_signed_nibble(byte, (col & 1) != 0);
        sum += static_cast<int>(x_u8[col]) * static_cast<int>(q);
    }
    return sum;
}
#endif

struct QuantizedU8Activation {
    std::vector<std::uint8_t> values;
    float scale = 1.0f;
    int zero_point = 128;
};

QuantizedU8Activation quantize_activation_u8(const float* x, int n) {
    if (!x || n <= 0) {
        throw std::invalid_argument("invalid activation quantization input");
    }
    float max_abs = 0.0f;
    for (int i = 0; i < n; ++i) {
        max_abs = std::max(max_abs, std::fabs(x[i]));
    }
    QuantizedU8Activation q;
    q.values.resize(static_cast<std::size_t>(n));
    q.scale = std::max(max_abs / 127.0f, 1.0e-8f);
    for (int i = 0; i < n; ++i) {
        int encoded = static_cast<int>(std::nearbyint(x[i] / q.scale)) + q.zero_point;
        encoded = std::max(0, std::min(255, encoded));
        q.values[static_cast<std::size_t>(i)] = static_cast<std::uint8_t>(encoded);
    }
    return q;
}

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
    if (!bytes || bits <= 0 || bits > 8) {
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
    if (bits < 2 || bits > 8) {
        throw std::invalid_argument("low-bit pack supports 2..8 bits");
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
    packed.row_sums.assign(static_cast<std::size_t>(rows), 0);
    for (int row = 0; row < rows; ++row) {
        int sum = 0;
        const std::size_t base = static_cast<std::size_t>(row) * cols;
        for (int col = 0; col < cols; ++col) {
            sum += static_cast<int>(unpack_signed_bits(packed.bytes.data(), (base + static_cast<std::size_t>(col)) * 4u, 4));
        }
        packed.row_sums[static_cast<std::size_t>(row)] = sum;
    }
    return packed;
}

EIGENSKILL_NOINLINE void lowbit_dequant_gemv(const PackedLowBitMatrix& packed,
                                             const float* EIGENSKILL_RESTRICT x,
                                             float* EIGENSKILL_RESTRICT y) {
    if (packed.rows <= 0 || packed.cols <= 0 || packed.bits < 2 || packed.bits > 8 || !x || !y) {
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

PackedMixedBitMatrix pack_mixed_lowbit_per_row(const float* w, int rows, int cols, const std::uint8_t* row_bits) {
    if (!w || !row_bits || rows <= 0 || cols <= 0) {
        throw std::invalid_argument("invalid mixed low-bit pack input");
    }

    PackedMixedBitMatrix packed;
    packed.rows = rows;
    packed.cols = cols;
    packed.row_bits.assign(row_bits, row_bits + rows);
    packed.row_bit_offsets.assign(static_cast<std::size_t>(rows), 0);
    packed.row_scales.assign(static_cast<std::size_t>(rows), 1.0f);

    std::uint64_t total_bits = 0;
    for (int row = 0; row < rows; ++row) {
        const int bits = static_cast<int>(packed.row_bits[static_cast<std::size_t>(row)]);
        if (bits < 2 || bits > 8) {
            throw std::invalid_argument("mixed low-bit pack supports 2..8 bits per row");
        }
        packed.row_bit_offsets[static_cast<std::size_t>(row)] = total_bits;
        total_bits += static_cast<std::uint64_t>(bits) * static_cast<std::uint64_t>(cols);
    }
    packed.bytes.assign(static_cast<std::size_t>((total_bits + 7u) / 8u), 0);

    for (int row = 0; row < rows; ++row) {
        const int bits = static_cast<int>(packed.row_bits[static_cast<std::size_t>(row)]);
        const int qmax = (1 << (bits - 1)) - 1;
        float max_abs = 0.0f;
        for (int col = 0; col < cols; ++col) {
            max_abs = std::max(max_abs, std::fabs(w[static_cast<std::size_t>(row) * cols + col]));
        }
        const float scale = std::max(max_abs / static_cast<float>(qmax), 1.0e-8f);
        packed.row_scales[static_cast<std::size_t>(row)] = scale;
        const std::uint64_t row_offset = packed.row_bit_offsets[static_cast<std::size_t>(row)];
        for (int col = 0; col < cols; ++col) {
            const float value = w[static_cast<std::size_t>(row) * cols + col] / scale;
            int q = static_cast<int>(std::nearbyint(value));
            q = std::max(-qmax, std::min(qmax, q));
            const int full = 1 << bits;
            const std::uint8_t encoded = static_cast<std::uint8_t>(q < 0 ? q + full : q);
            const std::uint64_t bit_offset = row_offset + static_cast<std::uint64_t>(col) * static_cast<std::uint64_t>(bits);
            write_bits(packed.bytes, static_cast<std::size_t>(bit_offset), bits, encoded);
        }
    }
    return packed;
}

EIGENSKILL_NOINLINE void mixed_lowbit_dequant_gemv(const PackedMixedBitMatrix& packed,
                                                   const float* EIGENSKILL_RESTRICT x,
                                                   float* EIGENSKILL_RESTRICT y) {
    if (!x || !y) {
        throw std::invalid_argument("invalid mixed low-bit GEMV input");
    }
    require_mixed_matrix(packed);
    for (int row = 0; row < packed.rows; ++row) {
        const int bits = static_cast<int>(packed.row_bits[static_cast<std::size_t>(row)]);
        float acc = 0.0f;
        const float scale = packed.row_scales[static_cast<std::size_t>(row)];
        const std::uint64_t row_offset = packed.row_bit_offsets[static_cast<std::size_t>(row)];
        for (int col = 0; col < packed.cols; ++col) {
            const std::uint64_t bit_offset = row_offset + static_cast<std::uint64_t>(col) * static_cast<std::uint64_t>(bits);
            const std::int8_t q = unpack_signed_bits(packed.bytes.data(), static_cast<std::size_t>(bit_offset), bits);
            acc += static_cast<float>(q) * scale * x[col];
        }
        y[row] = acc;
    }
}

EIGENSKILL_NOINLINE void mixed_lowbit_selected_rows_gemv(const PackedMixedBitMatrix& packed,
                                                        const float* EIGENSKILL_RESTRICT x,
                                                        const int* EIGENSKILL_RESTRICT rows,
                                                        int active_rows,
                                                        float* EIGENSKILL_RESTRICT y) {
    if (!x || !rows || !y || active_rows < 0) {
        throw std::invalid_argument("invalid mixed selected-row GEMV input");
    }
    require_mixed_matrix(packed);
    for (int out = 0; out < active_rows; ++out) {
        const int row = rows[out];
        if (row < 0 || row >= packed.rows) {
            throw std::out_of_range("mixed selected row index out of range");
        }
        const int bits = static_cast<int>(packed.row_bits[static_cast<std::size_t>(row)]);
        float acc = 0.0f;
        const float scale = packed.row_scales[static_cast<std::size_t>(row)];
        const std::uint64_t row_offset = packed.row_bit_offsets[static_cast<std::size_t>(row)];
        for (int col = 0; col < packed.cols; ++col) {
            const std::uint64_t bit_offset = row_offset + static_cast<std::uint64_t>(col) * static_cast<std::uint64_t>(bits);
            const std::int8_t q = unpack_signed_bits(packed.bytes.data(), static_cast<std::size_t>(bit_offset), bits);
            acc += static_cast<float>(q) * scale * x[col];
        }
        y[out] = acc;
    }
}

EIGENSKILL_NOINLINE void int4_dequant_gemv(const PackedInt4Matrix& packed,
                                           const float* EIGENSKILL_RESTRICT x,
                                           float* EIGENSKILL_RESTRICT y) {
    if (packed.rows <= 0 || packed.cols <= 0 || !x || !y) {
        throw std::invalid_argument("invalid INT4 GEMV input");
    }
    const std::size_t values = static_cast<std::size_t>(packed.rows) * packed.cols;
    const std::size_t expected_bytes = (values + 1u) / 2u;
    if (packed.bytes.size() != expected_bytes ||
        packed.row_scales.size() != static_cast<std::size_t>(packed.rows) ||
        (!packed.row_sums.empty() && packed.row_sums.size() != static_cast<std::size_t>(packed.rows))) {
        throw std::invalid_argument("inconsistent packed INT4 matrix");
    }
#if EIGENSKILL_KERNEL_HAS_AVX2
    if ((packed.cols % 2) == 0) {
        const std::size_t row_bytes = static_cast<std::size_t>(packed.cols) / 2u;
        for (int row = 0; row < packed.rows; ++row) {
            y[row] = int4_row_dot_avx2(
                packed.bytes.data() + static_cast<std::size_t>(row) * row_bytes,
                x,
                packed.cols,
                packed.row_scales[static_cast<std::size_t>(row)]);
        }
        return;
    }
#endif
    if ((packed.cols % 2) == 0) {
        const std::size_t row_bytes = static_cast<std::size_t>(packed.cols) / 2u;
        for (int row = 0; row < packed.rows; ++row) {
            const std::uint8_t* bytes = packed.bytes.data() + static_cast<std::size_t>(row) * row_bytes;
            const float scale = packed.row_scales[static_cast<std::size_t>(row)];
            float acc = 0.0f;
            for (int col = 0; col < packed.cols; ++col) {
                const std::uint8_t byte = bytes[static_cast<std::size_t>(col / 2)];
                const std::int8_t q = unpack_signed_nibble(byte, (col & 1) != 0);
                acc += static_cast<float>(q) * scale * x[col];
            }
            y[row] = acc;
        }
        return;
    }
    PackedLowBitMatrix low;
    low.rows = packed.rows;
    low.cols = packed.cols;
    low.bits = 4;
    low.bytes = packed.bytes;
    low.row_scales = packed.row_scales;
    lowbit_dequant_gemv(low, x, y);
}

EIGENSKILL_NOINLINE void int4_selected_rows_gemv(const PackedInt4Matrix& packed,
                                                 const float* EIGENSKILL_RESTRICT x,
                                                 const int* EIGENSKILL_RESTRICT rows,
                                                 int active_rows,
                                                 float* EIGENSKILL_RESTRICT y) {
    if (packed.rows <= 0 || packed.cols <= 0 || !x || !rows || !y || active_rows < 0) {
        throw std::invalid_argument("invalid selected-row INT4 GEMV input");
    }
    const std::size_t values = static_cast<std::size_t>(packed.rows) * packed.cols;
    const std::size_t expected_bytes = (values + 1u) / 2u;
    if (packed.bytes.size() != expected_bytes ||
        packed.row_scales.size() != static_cast<std::size_t>(packed.rows) ||
        (!packed.row_sums.empty() && packed.row_sums.size() != static_cast<std::size_t>(packed.rows))) {
        throw std::invalid_argument("inconsistent packed INT4 matrix");
    }
    if ((packed.cols % 2) != 0) {
        for (int out = 0; out < active_rows; ++out) {
            const int row = rows[out];
            if (row < 0 || row >= packed.rows) {
                throw std::out_of_range("selected INT4 row index out of range");
            }
            float acc = 0.0f;
            const float scale = packed.row_scales[static_cast<std::size_t>(row)];
            const std::size_t base = static_cast<std::size_t>(row) * packed.cols;
            for (int col = 0; col < packed.cols; ++col) {
                const std::size_t linear = base + col;
                const std::int8_t q = unpack_signed_bits(packed.bytes.data(), linear * 4u, 4);
                acc += static_cast<float>(q) * scale * x[col];
            }
            y[out] = acc;
        }
        return;
    }
    const std::size_t row_bytes = static_cast<std::size_t>(packed.cols) / 2u;
    for (int out = 0; out < active_rows; ++out) {
        const int row = rows[out];
        if (row < 0 || row >= packed.rows) {
            throw std::out_of_range("selected INT4 row index out of range");
        }
        const std::uint8_t* bytes = packed.bytes.data() + static_cast<std::size_t>(row) * row_bytes;
#if EIGENSKILL_KERNEL_HAS_AVX2
        y[out] = int4_row_dot_avx2(bytes, x, packed.cols, packed.row_scales[static_cast<std::size_t>(row)]);
#else
        const float scale = packed.row_scales[static_cast<std::size_t>(row)];
        float acc = 0.0f;
        for (int col = 0; col < packed.cols; ++col) {
            const std::uint8_t byte = bytes[static_cast<std::size_t>(col / 2)];
            const std::int8_t q = unpack_signed_nibble(byte, (col & 1) != 0);
            acc += static_cast<float>(q) * scale * x[col];
        }
        y[out] = acc;
#endif
    }
}

EIGENSKILL_NOINLINE void int4_maddubs_gemv(const PackedInt4Matrix& packed,
                                           const float* EIGENSKILL_RESTRICT x,
                                           float* EIGENSKILL_RESTRICT y) {
    if (packed.rows <= 0 || packed.cols <= 0 || !x || !y) {
        throw std::invalid_argument("invalid INT4 maddubs GEMV input");
    }
    const std::size_t values = static_cast<std::size_t>(packed.rows) * packed.cols;
    const std::size_t expected_bytes = (values + 1u) / 2u;
    if (packed.bytes.size() != expected_bytes ||
        packed.row_scales.size() != static_cast<std::size_t>(packed.rows) ||
        packed.row_sums.size() != static_cast<std::size_t>(packed.rows)) {
        throw std::invalid_argument("inconsistent packed INT4 maddubs matrix");
    }
#if EIGENSKILL_KERNEL_HAS_AVX2
    if ((packed.cols % 2) == 0) {
        const QuantizedU8Activation qx = quantize_activation_u8(x, packed.cols);
        const std::size_t row_bytes = static_cast<std::size_t>(packed.cols) / 2u;
        for (int row = 0; row < packed.rows; ++row) {
            const int raw = int4_u8_row_dot_maddubs_avx2(
                packed.bytes.data() + static_cast<std::size_t>(row) * row_bytes,
                qx.values.data(),
                packed.cols);
            const int corrected = raw - qx.zero_point * packed.row_sums[static_cast<std::size_t>(row)];
            y[row] = static_cast<float>(corrected) * qx.scale * packed.row_scales[static_cast<std::size_t>(row)];
        }
        return;
    }
#endif
    int4_dequant_gemv(packed, x, y);
}

EIGENSKILL_NOINLINE void int4_maddubs_selected_rows_gemv(const PackedInt4Matrix& packed,
                                                         const float* EIGENSKILL_RESTRICT x,
                                                         const int* EIGENSKILL_RESTRICT rows,
                                                         int active_rows,
                                                         float* EIGENSKILL_RESTRICT y) {
    if (packed.rows <= 0 || packed.cols <= 0 || !x || !rows || !y || active_rows < 0) {
        throw std::invalid_argument("invalid selected-row INT4 maddubs GEMV input");
    }
    const std::size_t values = static_cast<std::size_t>(packed.rows) * packed.cols;
    const std::size_t expected_bytes = (values + 1u) / 2u;
    if (packed.bytes.size() != expected_bytes ||
        packed.row_scales.size() != static_cast<std::size_t>(packed.rows) ||
        packed.row_sums.size() != static_cast<std::size_t>(packed.rows)) {
        throw std::invalid_argument("inconsistent packed INT4 maddubs matrix");
    }
#if EIGENSKILL_KERNEL_HAS_AVX2
    if ((packed.cols % 2) == 0) {
        const QuantizedU8Activation qx = quantize_activation_u8(x, packed.cols);
        const std::size_t row_bytes = static_cast<std::size_t>(packed.cols) / 2u;
        for (int out = 0; out < active_rows; ++out) {
            const int row = rows[out];
            if (row < 0 || row >= packed.rows) {
                throw std::out_of_range("selected INT4 maddubs row index out of range");
            }
            const int raw = int4_u8_row_dot_maddubs_avx2(
                packed.bytes.data() + static_cast<std::size_t>(row) * row_bytes,
                qx.values.data(),
                packed.cols);
            const int corrected = raw - qx.zero_point * packed.row_sums[static_cast<std::size_t>(row)];
            y[out] = static_cast<float>(corrected) * qx.scale * packed.row_scales[static_cast<std::size_t>(row)];
        }
        return;
    }
#endif
    int4_selected_rows_gemv(packed, x, rows, active_rows, y);
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
