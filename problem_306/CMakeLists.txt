cmake_minimum_required(VERSION 3.16)

project(problem306 CXX)

add_compile_options(
    -Wall
    -Wextra
    -Wshadow
    -Wpedantic
    -Werror
)

add_executable(solution solution.cpp)