
#include "hello.hpp"


hello::hello(/* args */)
{
    printf("hello init\r\n");
}

void hello::say() {
    printf("say hello the world\r\n");
}

hello::~hello()
{
}
