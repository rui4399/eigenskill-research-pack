cmake_minimum_required(VERSION 3.16)

project(eigenskill_cpp_artifacts LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT MSVC)
  add_compile_options(-O3 -Wall -Wextra -Wpedantic)
else()
  add_compile_options(/O2 /W4)
endif()

add_executable(eigenskill_bench src/eigenskill_bench.cpp)
add_executable(quant_policy_bypass src/quant_policy_bypass.cpp)
add_executable(quant_kernel_bench src/quant_kernel_bench.cpp)
