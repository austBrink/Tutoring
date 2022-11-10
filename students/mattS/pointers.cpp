#include <iostream>

int main () {
    int myNumber = 7;
    int *myNumberLocation = &myNumber;
    std::cout << myNumber << std::endl;
    std::cout << *myNumberLocation << std::endl;
    std::cout << *myNumberLocation << std::endl;
    std::cout << "hello world" << std::endl;
}