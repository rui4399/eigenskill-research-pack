// Row-wise mixed INT4/INT8 dequantized GEMV kernel for ARM NEON targets.
//
// Build example on device/NDK:
//   clang++ -O3 -std=c++17 -march=armv8.2-a+dotprod neon_mixed_decode.cpp -o neon_mixed_decode
//
// The ESMP packer stores signed symmetric rows. This file focuses on the hot
// decode + dot path that a Redmi K80 Pro runtime would call after loading the
// row metadata and packed bytes.

#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <random>
#include <stdexcept>
#include <vector>

#if defined(__ARM_NEON)
#include <arm_neon.h>
#define EIGENSKILL_HAS_NEON 1
#else
#define EIGENSKILL_HAS_NEON 0
#endif

namespace eigenskill_mobile {

struct MixedRows {
    int rows = 0;
    int cols = 0;
    const std::uint8_t* payload = nullptr;
    const std::uint8_t* row_bits = nullptr;
    const std::uint64_t* row_bit_offsets = nullptr;
    const float* row_scales = nullptr;
};

std::int8_t unpack_signed_bits(const std::uint8_t* bytes, std::uint64_t bit_offset, int bits) {
    std::uint8_t encoded = 0;
    for (int bit = 0; bit < bits; ++bit) {
        const std::uint64_t absolute = bit_offset + static_cast<std::uint64_t>(bit);
        encoded = static_cast<std::uint8_t>(
            encoded | (((bytes[absolute / 8] >> (absolute % 8)) & 1u) << bit));
    }
    const int sign = 1 << (bits - 1);
    const int full = 1 << bits;
    const int value = (encoded & sign) ? static_cast<int>(encoded) - full : static_cast<int>(encoded);
    return static_cast<std::int8_t>(value);
}

std::int8_t unpack_signed_nibble(std::uint8_t byte, bool high) {
    const std::uint8_t raw = high ? static_cast<std::uint8_t>(byte >> 4) : static_cast<std::uint8_t>(byte & 0x0f);
    return static_cast<std::int8_t>(raw >= 8 ? static_cast<int>(raw) - 16 : static_cast<int>(raw));
}

#if EIGENSKILL_HAS_NEON
float hsum_f32x4(float32x4_t value) {
    float32x2_t sum2 = vadd_f32(vget_low_f32(value), vget_high_f32(value));
    sum2 = vpadd_f32(sum2, sum2);
    return vget_lane_f32(sum2, 0);
}

float dot_int8_f32_neon(const std::int8_t* q, const float* x, int cols, float scale) {
    float32x4_t acc = vdupq_n_f32(0.0f);
    int col = 0;
    for (; col + 16 <= cols; col += 16) {
        const int8x16_t qv = vld1q_s8(q + col);
        const int16x8_t lo16 = vmovl_s8(vget_low_s8(qv));
        const int16x8_t hi16 = vmovl_s8(vget_high_s8(qv));
        const int32x4_t q0 = vmovl_s16(vget_low_s16(lo16));
        const int32x4_t q1 = vmovl_s16(vget_high_s16(lo16));
        const int32x4_t q2 = vmovl_s16(vget_low_s16(hi16));
        const int32x4_t q3 = vmovl_s16(vget_high_s16(hi16));
        acc = vmlaq_f32(acc, vcvtq_f32_s32(q0), vld1q_f32(x + col));
        acc = vmlaq_f32(acc, vcvtq_f32_s32(q1), vld1q_f32(x + col + 4));
        acc = vmlaq_f32(acc, vcvtq_f32_s32(q2), vld1q_f32(x + col + 8));
        acc = vmlaq_f32(acc, vcvtq_f32_s32(q3), vld1q_f32(x + col + 12));
    }
    float sum = hsum_f32x4(acc);
    for (; col < cols; ++col) {
        sum += static_cast<float>(q[col]) * x[col];
    }
    return sum * scale;
}

float dot_int4_f32_neon(const std::uint8_t* row_bytes, const float* x, int cols, float scale) {
    alignas(16) std::int8_t unpacked[32];
    float32x4_t acc = vdupq_n_f32(0.0f);
    int col = 0;
    for (; col + 32 <= cols; col += 32) {
        const std::uint8_t* block = row_bytes + col / 2;
        for (int i = 0; i < 16; ++i) {
            unpacked[2 * i] = unpack_signed_nibble(block[i], false);
            unpacked[2 * i + 1] = unpack_signed_nibble(block[i], true);
        }
        for (int offset = 0; offset < 32; offset += 16) {
            const int8x16_t qv = vld1q_s8(unpacked + offset);
            const int16x8_t lo16 = vmovl_s8(vget_low_s8(qv));
            const int16x8_t hi16 = vmovl_s8(vget_high_s8(qv));
            const int32x4_t q0 = vmovl_s16(vget_low_s16(lo16));
            const int32x4_t q1 = vmovl_s16(vget_high_s16(lo16));
            const int32x4_t q2 = vmovl_s16(vget_low_s16(hi16));
            const int32x4_t q3 = vmovl_s16(vget_high_s16(hi16));
            acc = vmlaq_f32(acc, vcvtq_f32_s32(q0), vld1q_f32(x + col + offset));
            acc = vmlaq_f32(acc, vcvtq_f32_s32(q1), vld1q_f32(x + col + offset + 4));
            acc = vmlaq_f32(acc, vcvtq_f32_s32(q2), vld1q_f32(x + col + offset + 8));
            acc = vmlaq_f32(acc, vcvtq_f32_s32(q3), vld1q_f32(x + col + offset + 12));
        }
    }
    float sum = hsum_f32x4(acc);
    for (; col < cols; ++col) {
        const std::uint8_t byte = row_bytes[col / 2];
        sum += static_cast<float>(unpack_signed_nibble(byte, (col & 1) != 0)) * x[col];
    }
    return sum * scale;
}
#endif

float dot_row_scalar(const MixedRows& matrix, int row, const float* x) {
    const int bits = static_cast<int>(matrix.row_bits[row]);
    const std::uint64_t row_offset = matrix.row_bit_offsets[row];
    const float scale = matrix.row_scales[row];
    float sum = 0.0f;
    for (int col = 0; col < matrix.cols; ++col) {
        const std::uint64_t bit_offset = row_offset + static_cast<std::uint64_t>(col) * bits;
        sum += static_cast<float>(unpack_signed_bits(matrix.payload, bit_offset, bits)) * x[col];
    }
    return sum * scale;
}

void mixed_dequant_gemv_neon(const MixedRows& matrix, const float* x, float* y) {
    if (matrix.rows <= 0 || matrix.cols <= 0 || !matrix.payload || !matrix.row_bits ||
        !matrix.row_bit_offsets || !matrix.row_scales || !x || !y) {
        throw std::invalid_argument("invalid mixed_dequant_gemv_neon input");
    }
    for (int row = 0; row < matrix.rows; ++row) {
        const int bits = static_cast<int>(matrix.row_bits[row]);
#if EIGENSKILL_HAS_NEON
        if (bits == 4 && (matrix.cols % 2) == 0) {
            y[row] = dot_int4_f32_neon(matrix.payload + matrix.row_bit_offsets[row] / 8, x, matrix.cols, matrix.row_scales[row]);
            continue;
        }
        if (bits == 8 && (matrix.row_bit_offsets[row] % 8) == 0) {
            y[row] = dot_int8_f32_neon(
                reinterpret_cast<const std::int8_t*>(matrix.payload + matrix.row_bit_offsets[row] / 8),
                x,
                matrix.cols,
                matrix.row_scales[row]);
            continue;
        }
#endif
        y[row] = dot_row_scalar(matrix, row, x);
    }
}

}  // namespace eigenskill_mobile

namespace {

void write_bits(std::vector<std::uint8_t>& bytes, std::uint64_t bit_offset, int bits, std::uint8_t value) {
    for (int bit = 0; bit < bits; ++bit) {
        const std::uint64_t absolute = bit_offset + static_cast<std::uint64_t>(bit);
        const std::uint8_t mask = static_cast<std::uint8_t>(1u << (absolute % 8));
        if (((value >> bit) & 1u) != 0) {
            bytes[absolute / 8] = static_cast<std::uint8_t>(bytes[absolute / 8] | mask);
        }
    }
}

struct Fixture {
    int rows = 0;
    int cols = 0;
    std::vector<float> weights;
    std::vector<float> x;
    std::vector<std::uint8_t> row_bits;
    std::vector<std::uint64_t> row_offsets;
    std::vector<float> scales;
    std::vector<std::uint8_t> payload;
};

Fixture make_fixture(int rows, int cols) {
    Fixture f;
    f.rows = rows;
    f.cols = cols;
    f.weights.resize(static_cast<std::size_t>(rows) * cols);
    f.x.resize(static_cast<std::size_t>(cols));
    f.row_bits.assign(static_cast<std::size_t>(rows), 4);
    f.row_offsets.assign(static_cast<std::size_t>(rows), 0);
    f.scales.assign(static_cast<std::size_t>(rows), 1.0f);
    std::mt19937 rng(20260605);
    std::normal_distribution<float> dist(0.0f, 0.04f);
    std::normal_distribution<float> xdist(0.0f, 1.0f);
    for (float& value : f.weights) {
        value = dist(rng);
    }
    for (float& value : f.x) {
        value = xdist(rng);
    }
    std::uint64_t total_bits = 0;
    for (int row = 0; row < rows; ++row) {
        f.row_bits[row] = (row % 16 == 0) ? 8 : 4;
        f.row_offsets[row] = total_bits;
        total_bits += static_cast<std::uint64_t>(f.row_bits[row]) * cols;
    }
    f.payload.assign(static_cast<std::size_t>((total_bits + 7) / 8), 0);
    for (int row = 0; row < rows; ++row) {
        const int bits = f.row_bits[row];
        const int qmax = (1 << (bits - 1)) - 1;
        float max_abs = 0.0f;
        for (int col = 0; col < cols; ++col) {
            max_abs = std::max(max_abs, std::fabs(f.weights[static_cast<std::size_t>(row) * cols + col]));
        }
        f.scales[row] = std::max(max_abs / static_cast<float>(qmax), 1.0e-8f);
        for (int col = 0; col < cols; ++col) {
            int q = static_cast<int>(std::nearbyint(f.weights[static_cast<std::size_t>(row) * cols + col] / f.scales[row]));
            q = std::max(-qmax, std::min(qmax, q));
            const int full = 1 << bits;
            const std::uint8_t encoded = static_cast<std::uint8_t>(q < 0 ? q + full : q);
            write_bits(f.payload, f.row_offsets[row] + static_cast<std::uint64_t>(col) * bits, bits, encoded);
        }
    }
    return f;
}

void dense_gemv(const Fixture& f, std::vector<float>& y) {
    y.assign(static_cast<std::size_t>(f.rows), 0.0f);
    for (int row = 0; row < f.rows; ++row) {
        float sum = 0.0f;
        for (int col = 0; col < f.cols; ++col) {
            sum += f.weights[static_cast<std::size_t>(row) * f.cols + col] * f.x[col];
        }
        y[row] = sum;
    }
}

double rel_l2(const std::vector<float>& a, const std::vector<float>& b) {
    double err2 = 0.0;
    double ref2 = 0.0;
    for (std::size_t i = 0; i < a.size(); ++i) {
        const double diff = static_cast<double>(a[i]) - static_cast<double>(b[i]);
        err2 += diff * diff;
        ref2 += static_cast<double>(b[i]) * static_cast<double>(b[i]);
    }
    return std::sqrt(err2 / std::max(ref2, 1.0e-30));
}

}  // namespace

int main(int argc, char** argv) {
    int rows = 512;
    int cols = 1024;
    int iters = 200;
    if (argc > 1) rows = std::atoi(argv[1]);
    if (argc > 2) cols = std::atoi(argv[2]);
    if (argc > 3) iters = std::atoi(argv[3]);
    Fixture f = make_fixture(rows, cols);
    eigenskill_mobile::MixedRows matrix{
        f.rows,
        f.cols,
        f.payload.data(),
        f.row_bits.data(),
        f.row_offsets.data(),
        f.scales.data(),
    };
    std::vector<float> dense;
    std::vector<float> mixed(static_cast<std::size_t>(rows), 0.0f);
    dense_gemv(f, dense);
    eigenskill_mobile::mixed_dequant_gemv_neon(matrix, f.x.data(), mixed.data());
    const double error = rel_l2(mixed, dense);

    const auto start = std::chrono::steady_clock::now();
    for (int i = 0; i < iters; ++i) {
        eigenskill_mobile::mixed_dequant_gemv_neon(matrix, f.x.data(), mixed.data());
    }
    const auto end = std::chrono::steady_clock::now();
    const double ms = std::chrono::duration<double, std::milli>(end - start).count() / std::max(iters, 1);
    std::cout << "{\n"
              << "  \"rows\": " << rows << ",\n"
              << "  \"cols\": " << cols << ",\n"
              << "  \"iters\": " << iters << ",\n"
              << "  \"neon_enabled\": " << (EIGENSKILL_HAS_NEON ? "true" : "false") << ",\n"
              << "  \"mixed_ms\": " << ms << ",\n"
              << "  \"rel_l2_vs_fp32_dense\": " << error << "\n"
              << "}\n";
    return std::isfinite(error) ? 0 : 1;
}
