#include "eigenskill/esmp_format.hpp"

#include <algorithm>
#include <array>
#include <cstring>
#include <fstream>
#include <limits>
#include <stdexcept>

namespace eigenskill {

namespace {

constexpr std::array<char, 8> kMagic{{'E', 'S', 'M', 'P', 'Q', '0', '0', '1'}};

void write_u32_le(std::ostream& out, std::uint32_t value) {
    for (int i = 0; i < 4; ++i) {
        out.put(static_cast<char>((value >> (8 * i)) & 0xffu));
    }
}

void write_i32_le(std::ostream& out, std::int32_t value) {
    write_u32_le(out, static_cast<std::uint32_t>(value));
}

void write_u64_le(std::ostream& out, std::uint64_t value) {
    for (int i = 0; i < 8; ++i) {
        out.put(static_cast<char>((value >> (8 * i)) & 0xffu));
    }
}

void write_f32_le(std::ostream& out, float value) {
    std::uint32_t raw = 0;
    static_assert(sizeof(raw) == sizeof(value), "float must be 32-bit");
    std::memcpy(&raw, &value, sizeof(raw));
    write_u32_le(out, raw);
}

std::uint32_t read_u32_le(const std::vector<std::uint8_t>& bytes, std::size_t offset) {
    if (offset + 4 > bytes.size()) {
        throw std::runtime_error("truncated ESMP u32 field");
    }
    std::uint32_t value = 0;
    for (int i = 0; i < 4; ++i) {
        value |= static_cast<std::uint32_t>(bytes[offset + static_cast<std::size_t>(i)]) << (8 * i);
    }
    return value;
}

std::int32_t read_i32_le(const std::vector<std::uint8_t>& bytes, std::size_t offset) {
    return static_cast<std::int32_t>(read_u32_le(bytes, offset));
}

std::uint64_t read_u64_le(const std::vector<std::uint8_t>& bytes, std::size_t offset) {
    if (offset + 8 > bytes.size()) {
        throw std::runtime_error("truncated ESMP u64 field");
    }
    std::uint64_t value = 0;
    for (int i = 0; i < 8; ++i) {
        value |= static_cast<std::uint64_t>(bytes[offset + static_cast<std::size_t>(i)]) << (8 * i);
    }
    return value;
}

float read_f32_le(const std::vector<std::uint8_t>& bytes, std::size_t offset) {
    const std::uint32_t raw = read_u32_le(bytes, offset);
    float value = 0.0f;
    std::memcpy(&value, &raw, sizeof(value));
    return value;
}

}  // namespace

std::uint64_t esmp_total_package_bytes(int rows, std::uint64_t payload_bytes) {
    if (rows <= 0) {
        throw std::invalid_argument("ESMP rows must be positive");
    }
    return static_cast<std::uint64_t>(kEsmpHeaderBytes) +
           static_cast<std::uint64_t>(rows) * static_cast<std::uint64_t>(kEsmpRowMetaBytes) +
           payload_bytes;
}

void write_esmp_matrix(
    const std::string& path,
    const PackedMixedBitMatrix& packed,
    const std::vector<int>& row_sums) {
    if (packed.rows <= 0 || packed.cols <= 0 ||
        packed.row_bits.size() != static_cast<std::size_t>(packed.rows) ||
        packed.row_scales.size() != static_cast<std::size_t>(packed.rows) ||
        packed.row_bit_offsets.size() != static_cast<std::size_t>(packed.rows) ||
        row_sums.size() != static_cast<std::size_t>(packed.rows)) {
        throw std::runtime_error("inconsistent ESMP matrix metadata");
    }

    const std::uint64_t row_meta_offset = kEsmpHeaderBytes;
    const std::uint64_t data_offset =
        row_meta_offset + static_cast<std::uint64_t>(packed.rows) * static_cast<std::uint64_t>(kEsmpRowMetaBytes);
    std::ofstream out(path, std::ios::binary);
    if (!out) {
        throw std::runtime_error("failed to create ESMP output: " + path);
    }

    out.write(kMagic.data(), static_cast<std::streamsize>(kMagic.size()));
    write_u32_le(out, kEsmpVersion);
    write_u32_le(out, kEsmpHeaderBytes);
    write_u64_le(out, static_cast<std::uint64_t>(packed.rows));
    write_u64_le(out, static_cast<std::uint64_t>(packed.cols));
    write_u64_le(out, row_meta_offset);
    write_u64_le(out, data_offset);
    write_u64_le(out, static_cast<std::uint64_t>(packed.bytes.size()));
    write_u32_le(out, kEsmpQuantSchemeSignedSymmetricPerRow);
    write_u32_le(out, 0);

    std::uint64_t expected_row_bit_offset = 0;
    for (int row = 0; row < packed.rows; ++row) {
        const std::size_t index = static_cast<std::size_t>(row);
        const std::uint8_t bits = packed.row_bits[index];
        if (bits < 2 || bits > 8 || packed.row_bit_offsets[index] != expected_row_bit_offset) {
            throw std::runtime_error("invalid ESMP row metadata before write");
        }
        out.put(static_cast<char>(bits));
        out.put(0);
        out.put(0);
        out.put(0);
        write_f32_le(out, packed.row_scales[index]);
        write_u64_le(out, packed.row_bit_offsets[index]);
        write_i32_le(out, static_cast<std::int32_t>(row_sums[index]));
        write_u32_le(out, 0);
        expected_row_bit_offset += static_cast<std::uint64_t>(bits) * static_cast<std::uint64_t>(packed.cols);
    }

    const std::uint64_t expected_payload_bytes = (expected_row_bit_offset + 7u) / 8u;
    if (expected_payload_bytes != static_cast<std::uint64_t>(packed.bytes.size())) {
        throw std::runtime_error("ESMP payload byte count does not match row metadata before write");
    }

    out.write(reinterpret_cast<const char*>(packed.bytes.data()), static_cast<std::streamsize>(packed.bytes.size()));
    if (!out) {
        throw std::runtime_error("failed while writing ESMP output: " + path);
    }
}

EsmpMatrix read_esmp_matrix(const std::string& path) {
    std::ifstream in(path, std::ios::binary);
    if (!in) {
        throw std::runtime_error("failed to open ESMP file: " + path);
    }
    in.seekg(0, std::ios::end);
    const std::streamoff size = in.tellg();
    in.seekg(0, std::ios::beg);
    if (size < static_cast<std::streamoff>(kEsmpHeaderBytes)) {
        throw std::runtime_error("ESMP file is smaller than header");
    }
    std::vector<std::uint8_t> bytes(static_cast<std::size_t>(size));
    in.read(reinterpret_cast<char*>(bytes.data()), size);
    if (!in) {
        throw std::runtime_error("failed to read ESMP file: " + path);
    }
    if (!std::equal(kMagic.begin(), kMagic.end(), reinterpret_cast<const char*>(bytes.data()))) {
        throw std::runtime_error("bad ESMP magic");
    }

    const std::uint32_t version = read_u32_le(bytes, 8);
    const std::uint32_t header_bytes = read_u32_le(bytes, 12);
    const std::uint64_t rows_u64 = read_u64_le(bytes, 16);
    const std::uint64_t cols_u64 = read_u64_le(bytes, 24);
    const std::uint64_t row_meta_offset = read_u64_le(bytes, 32);
    const std::uint64_t data_offset = read_u64_le(bytes, 40);
    const std::uint64_t data_bytes = read_u64_le(bytes, 48);
    const std::uint32_t quant_scheme = read_u32_le(bytes, 56);
    if (version != kEsmpVersion || header_bytes != kEsmpHeaderBytes ||
        quant_scheme != kEsmpQuantSchemeSignedSymmetricPerRow) {
        throw std::runtime_error("unsupported ESMP version/header/quant scheme");
    }
    if (rows_u64 == 0 || cols_u64 == 0 || rows_u64 > static_cast<std::uint64_t>(std::numeric_limits<int>::max()) ||
        cols_u64 > static_cast<std::uint64_t>(std::numeric_limits<int>::max())) {
        throw std::runtime_error("invalid ESMP dimensions");
    }

    const std::uint64_t expected_meta_end =
        row_meta_offset + rows_u64 * static_cast<std::uint64_t>(kEsmpRowMetaBytes);
    if (row_meta_offset != kEsmpHeaderBytes || data_offset != expected_meta_end ||
        data_offset + data_bytes != bytes.size()) {
        throw std::runtime_error("inconsistent ESMP offsets or payload length");
    }

    EsmpMatrix loaded;
    loaded.matrix.rows = static_cast<int>(rows_u64);
    loaded.matrix.cols = static_cast<int>(cols_u64);
    loaded.data_bytes = data_bytes;
    loaded.file_bytes = static_cast<std::uint64_t>(bytes.size());
    loaded.matrix.row_bits.assign(static_cast<std::size_t>(loaded.matrix.rows), 0);
    loaded.matrix.row_bit_offsets.assign(static_cast<std::size_t>(loaded.matrix.rows), 0);
    loaded.matrix.row_scales.assign(static_cast<std::size_t>(loaded.matrix.rows), 1.0f);
    loaded.row_sums.assign(static_cast<std::size_t>(loaded.matrix.rows), 0);

    std::uint64_t expected_row_bit_offset = 0;
    for (int row = 0; row < loaded.matrix.rows; ++row) {
        const std::size_t offset =
            static_cast<std::size_t>(row_meta_offset) + static_cast<std::size_t>(row) * kEsmpRowMetaBytes;
        const std::uint8_t bits = bytes[offset];
        if (bits < 2 || bits > 8) {
            throw std::runtime_error("invalid row bit width in ESMP metadata");
        }
        const std::uint64_t row_bit_offset = read_u64_le(bytes, offset + 8);
        if (row_bit_offset != expected_row_bit_offset) {
            throw std::runtime_error("non-contiguous row bit offsets in ESMP metadata");
        }
        loaded.matrix.row_bits[static_cast<std::size_t>(row)] = bits;
        loaded.matrix.row_scales[static_cast<std::size_t>(row)] = read_f32_le(bytes, offset + 4);
        loaded.matrix.row_bit_offsets[static_cast<std::size_t>(row)] = row_bit_offset;
        loaded.row_sums[static_cast<std::size_t>(row)] = static_cast<int>(read_i32_le(bytes, offset + 16));
        expected_row_bit_offset += static_cast<std::uint64_t>(bits) * static_cast<std::uint64_t>(loaded.matrix.cols);
    }

    const std::uint64_t expected_payload_bytes = (expected_row_bit_offset + 7u) / 8u;
    if (expected_payload_bytes != data_bytes) {
        throw std::runtime_error("ESMP payload byte count does not match row bit metadata");
    }
    loaded.matrix.bytes.assign(bytes.begin() + static_cast<std::ptrdiff_t>(data_offset), bytes.end());
    return loaded;
}

}  // namespace eigenskill
