#pragma once

#include "eigenskill/quant_kernels.hpp"

#include <cstdint>
#include <string>
#include <vector>

namespace eigenskill {

constexpr const char* kEsmpFormat = "ESMPQ001";
constexpr std::uint32_t kEsmpVersion = 1;
constexpr std::uint32_t kEsmpHeaderBytes = 64;
constexpr std::uint32_t kEsmpRowMetaBytes = 24;
constexpr std::uint32_t kEsmpQuantSchemeSignedSymmetricPerRow = 1;

struct EsmpMatrix {
    PackedMixedBitMatrix matrix;
    std::vector<int> row_sums;
    std::uint64_t data_bytes = 0;
    std::uint64_t file_bytes = 0;
};

std::uint64_t esmp_total_package_bytes(int rows, std::uint64_t payload_bytes);

void write_esmp_matrix(
    const std::string& path,
    const PackedMixedBitMatrix& packed,
    const std::vector<int>& row_sums);

EsmpMatrix read_esmp_matrix(const std::string& path);

}  // namespace eigenskill
