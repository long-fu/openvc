#include <iostream>

#include "hello.hpp"

void say_hello(){
    hello h = hello();
    h.say();
    std::cout << "Hello, from display!\n";
}


int main(int argc, char const *argv[])
{
    /* code */
    say_hello();
    return 0;
}
