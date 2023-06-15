cmake_minimum_required(VERSION 3.0.0)
project(display VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()

add_library(display main.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
