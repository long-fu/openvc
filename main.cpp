#include <iostream>

#include "hello.hpp"
#include "opencv.hpp"

void say_hello(){
    hello h = hello();
    h.say();
    std::cout << "Hello, from display!\n";
}


void show_image() {
    auto cv = opencv();
    cv.show_image("/home/haoshuai/code/opencv/datasets/bus.jpg");
}

void show_video() {
    auto cv = opencv();
    cv.show_video("/home/haoshuai/视频/1.mkv");
}

int main(int argc, char const *argv[])
{
    show_video();
    say_hello();
    return 0;
}
