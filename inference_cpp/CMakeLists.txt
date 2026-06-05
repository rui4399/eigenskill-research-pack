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
add_executable(quant_random_baseline_audit src/quant_random_baseline_audit.cpp)
add_executable(quant_ppl_summary_merge src/quant_ppl_summary_merge.cpp)
add_executable(quant_seed_coverage_check src/quant_seed_coverage_check.cpp)
add_executable(quant_chunked_eval_plan src/quant_chunked_eval_plan.cpp)
add_executable(quant_consensus_audit src/quant_consensus_audit.cpp)
add_executable(quant_sensitivity_stability src/quant_sensitivity_stability.cpp)
add_executable(quant_budget_curve_summary src/quant_budget_curve_summary.cpp)
add_executable(quant_consensus_builder src/quant_consensus_builder.cpp)
add_executable(baseline_install_probe src/baseline_install_probe.cpp)
add_executable(gpu_guard_summary src/gpu_guard_summary.cpp)
add_executable(quant_swap_search_summary src/quant_swap_search_summary.cpp)
add_executable(quant_transfer_matrix src/quant_transfer_matrix.cpp)
add_executable(quant_task_eval_summary src/quant_task_eval_summary.cpp)
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
    NAME quant_random_baseline_audit_smoke
    COMMAND quant_random_baseline_audit --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/ppl_summary_fixture.json --dataset fixture --emit json
  )
  add_test(
    NAME quant_ppl_summary_merge_smoke
    COMMAND quant_ppl_summary_merge
      --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/ppl_summary_merge_left_fixture.json
      --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/ppl_summary_merge_right_fixture.json
      --out ${CMAKE_CURRENT_BINARY_DIR}/ppl_summary_merge_smoke.json
  )
  set_tests_properties(
    quant_ppl_summary_merge_smoke
    PROPERTIES FIXTURES_SETUP ppl_summary_merge_smoke_file
  )
  add_test(
    NAME quant_ppl_summary_merge_audit_smoke
    COMMAND quant_random_baseline_audit
      --input ${CMAKE_CURRENT_BINARY_DIR}/ppl_summary_merge_smoke.json
      --dataset fixture
      --target wikitext_c4_consensus
      --emit json
  )
  set_tests_properties(
    quant_ppl_summary_merge_audit_smoke
    PROPERTIES FIXTURES_REQUIRED ppl_summary_merge_smoke_file
  )
  add_test(
    NAME quant_seed_coverage_check_smoke
    COMMAND quant_seed_coverage_check
      --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/seed_coverage_left_fixture.json
      --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/seed_coverage_right_fixture.json
      --prefix random_budget_seed_
      --start 1
      --end 4
      --require-name fp16
      --require-name uniform_int4
      --emit json
  )
  add_test(
    NAME quant_seed_coverage_check_duplicate_fails
    COMMAND quant_seed_coverage_check
      --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/seed_coverage_left_fixture.json
      --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/seed_coverage_right_fixture.json
      --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/seed_coverage_duplicate_fixture.json
      --prefix random_budget_seed_
      --start 1
      --end 4
      --emit json
  )
  set_tests_properties(
    quant_seed_coverage_check_duplicate_fails
    PROPERTIES WILL_FAIL TRUE
  )
  add_test(
    NAME quant_chunked_eval_plan_bash_smoke
    COMMAND quant_chunked_eval_plan --emit bash
  )
  add_test(
    NAME quant_chunked_eval_plan_markdown_smoke
    COMMAND quant_chunked_eval_plan --emit markdown
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
    NAME quant_sensitivity_stability_json_smoke
    COMMAND quant_sensitivity_stability
      --left ${CMAKE_CURRENT_SOURCE_DIR}/testdata/sensitivity_left_fixture.json
      --right ${CMAKE_CURRENT_SOURCE_DIR}/testdata/sensitivity_right_fixture.json
      --left-name fixture_left
      --right-name fixture_right
      --top-k 1,2,3
      --emit json
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
  add_test(
    NAME quant_transfer_matrix_smoke
    COMMAND quant_transfer_matrix
      --case fixture=${CMAKE_CURRENT_SOURCE_DIR}/testdata/transfer_summary_fixture.json
      --guard ${CMAKE_CURRENT_SOURCE_DIR}/testdata/gpu_guard_fixture.json
      --emit json
  )
  add_test(
    NAME quant_task_eval_summary_smoke
    COMMAND quant_task_eval_summary
      --input ${CMAKE_CURRENT_SOURCE_DIR}/testdata/task_eval_fixture.json
      --label fixture
      --emit json
  )
endif()

if(NOT MSVC AND (CMAKE_SYSTEM_PROCESSOR MATCHES "x86_64|AMD64|amd64"))
  target_compile_options(eigenskill_quant_kernels PRIVATE -mavx2)
  target_compile_options(quant_kernel_bench PRIVATE -mavx2)
  target_compile_options(quant_kernel_verify PRIVATE -mavx2)
endif()
