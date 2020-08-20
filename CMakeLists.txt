cmake_minimum_required(VERSION 3.17)
project(NLOSRender)

set(CMAKE_CXX_STANDARD 14)

find_package(OpenCV REQUIRED)
find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)

include_directories(render-mnist)
include_directories(render-mnist/src)
include_directories(${GLFW_INCLUDE_DIRS})

add_executable(NLOSRender
        render-mnist/src/display_0_initial.cpp
        render-mnist/src/display_1_cam.cpp
        render-mnist/src/display_2_fbo.cpp
        render-mnist/src/display_3_program.cpp
        render-mnist/src/display_4_loaddata.cpp
        render-mnist/src/display_5_draw.cpp
        render-mnist/src/display_6_render.cpp
        render-mnist/src/main.cpp
        render-mnist/src/renderclass.h
        render-mnist/model_normalized.mtl
        render-mnist/p2.fragmentshader
        render-mnist/p2.vertexshader
        render-mnist/pointlight.fragmentshader
        render-mnist/pointlight.vertexshader)

target_link_libraries(NLOSRender
        ${OpenCV_LIBS}
        ${OPENGL_LIBRARIES}
        ${GLFW3_LIBRARY} glfw GLEW
        )