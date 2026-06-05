cmake_minimum_required(VERSION 3.16)

project(eigenskill_cpp_artifacts LANGUAGES CXX)

include(CTest)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT MSVC)
  add_compile_options(-O3 -Wall -Wextra -Wpedantic)
else()
  add_compile_options(/O2 /W4)
endif()

add_library(eigenskill_quant_kernels STATIC src/quant_kernels.cpp)
target_include_directories(eigenskill_quant_kernels PUBLIC include)

add_executable(eigenskill_bench src/eigenskill_bench.cpp)
add_executable(quant_policy_bypass src/quant_policy_bypass.cpp)
add_executable(quant_kernel_bench src/quant_kernel_bench.cpp)
add_executable(quant_kernel_verify src/quant_kernel_verify.cpp)
add_executable(quant_allocation_planner src/quant_allocation_planner.cpp)
add_executable(quant_result_summarizer src/quant_result_summarizer.cpp)
add_executable(quant_evidence_matrix src/quant_evidence_matrix.cpp)
add_executable(quant_consensus_audit src/quant_consensus_audit.cpp)
add_executable(quant_sensitivity_stability src/quant_sensitivity_stability.cpp)
add_executable(quant_budget_curve_summary src/quant_budget_curve_summary.cpp)
add_executable(quant_consensus_builder src/quant_consensus_builder.cpp)
add_executable(baseline_install_probe src/baseline_install_probe.cpp)
add_executable(gpu_guard_summary src/gpu_guard_summary.cpp)
add_executable(quant_swap_search_summary src/quant_swap_search_summary.cpp)
target_link_libraries(quant_kernel_bench PRIVATE eigenskill_quant_kernels)
target_link_libraries(quant_kernel_verify PRIVATE eigenskill_quant_kernels)

if(BUILD_TESTING)
  add_test(
    NAME quant_kernel_verify_smoke
    COMMAND quant_kernel_verify --dim 512 --active-rows 32
  )
  add_test(
    NAME quant_allocation_planner_smoke
    COMMAND quant_allocation_planner --csv ${CMAKE_CURRENT_SOURCE_DIR}/testdata/allocation_fixture.csv --budget-avg-bits 4.8 --emit csv
  )
  add_test(
    NAME quant_result_summarizer_smoke
    COMMAND quant_result_summarizer --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/ppl_summary_fixture.json --dataset fixture --emit csv
  )
  add_test(
    NAME quant_evidence_matrix_smoke
    COMMAND quant_evidence_matrix --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/ppl_summary_fixture.json --dataset fixture --emit markdown
  )
  add_test(
    NAME quant_evidence_matrix_json_smoke
    COMMAND quant_evidence_matrix --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/ppl_summary_fixture.json --dataset fixture --emit json
  )
  add_test(
    NAME quant_consensus_audit_smoke
    COMMAND quant_consensus_audit
      --left ${CMAKE_CURRENT_SOURCE_DIR}/testdata/allocation_left_fixture.json
      --right ${CMAKE_CURRENT_SOURCE_DIR}/testdata/allocation_right_fixture.json
      --consensus ${CMAKE_CURRENT_SOURCE_DIR}/testdata/allocation_consensus_fixture.json
      --label fixture
      --emit csv
  )
  add_test(
    NAME quant_sensitivity_stability_smoke
    COMMAND quant_sensitivity_stability
      --left ${CMAKE_CURRENT_SOURCE_DIR}/testdata/sensitivity_left_fixture.json
      --right ${CMAKE_CURRENT_SOURCE_DIR}/testdata/sensitivity_right_fixture.json
      --left-name fixture_left
      --right-name fixture_right
      --top-k 1,2,3
      --emit csv
  )
  add_test(
    NAME quant_budget_curve_summary_smoke
    COMMAND quant_budget_curve_summary
      --input fixture=${CMAKE_CURRENT_SOURCE_DIR}/testdata/ppl_summary_fixture.json
      --emit csv
      --no-write
  )
  add_test(
    NAME quant_consensus_builder_smoke
    COMMAND quant_consensus_builder
      --left ${CMAKE_CURRENT_SOURCE_DIR}/testdata/allocation_left_fixture.json
      --right ${CMAKE_CURRENT_SOURCE_DIR}/testdata/allocation_right_fixture.json
      --budget-avg-bits 5.0
      --emit json
      --no-write
  )
  add_test(
    NAME baseline_install_probe_smoke
    COMMAND baseline_install_probe
      --log full=${CMAKE_CURRENT_SOURCE_DIR}/testdata/baseline_install_timeout_fixture.log
      --log nodeps=${CMAKE_CURRENT_SOURCE_DIR}/testdata/baseline_install_nodeps_success_fixture.log
      --emit json
  )
  add_test(
    NAME gpu_guard_summary_smoke
    COMMAND gpu_guard_summary
      --input fixture=${CMAKE_CURRENT_SOURCE_DIR}/testdata/gpu_guard_fixture.json
      --emit json
  )
  add_test(
    NAME quant_swap_search_summary_smoke
    COMMAND quant_swap_search_summary
      --summary ${CMAKE_CURRENT_SOURCE_DIR}/testdata/swap_search_fixture.json
      --guard ${CMAKE_CURRENT_SOURCE_DIR}/testdata/gpu_guard_fixture.json
      --label fixture
      --emit json
  )
endif()

if(NOT MSVC AND (CMAKE_SYSTEM_PROCESSOR MATCHES "x86_64|AMD64|amd64"))
  target_compile_options(eigenskill_quant_kernels PRIVATE -mavx2)
  target_compile_options(quant_kernel_bench PRIVATE -mavx2)
  target_compile_options(quant_kernel_verify PRIVATE -mavx2)
endif()
