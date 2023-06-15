# CMake 最低版本号要求
cmake_minimum_required(VERSION 3.0.0)
# 项目信息
project(display VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()
# 添加头文件路径
include_directories("${PROJECT_SOURCE_DIR}/include")
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
include_directories( "/usr/local/include/opencv4" )
# add_subdirectory(src) 子目录
# aux_source_directory(./src hello.cpp)
#add_library(display SHARED main.cpp)
# target_include_directories(${PROJECT_SOURCE_DIR}/include)
# target_include_directories(display
#     PRIVATE
#         ${PROJECT_SOURCE_DIR}/include
# )
# 指定生成目标
add_executable(main main.cpp src/hello.cpp src/opencv.cpp)
# 连接opencv库
target_link_libraries( main ${OpenCV_LIBS} )
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
