#include <iostream>
#include <cctype>
#include <sstream>

void print(std::string *s);
void print(std::string s);
void print(int *i);
void print(int i);


int main (void) {
    
    int mynumber = 10;
    print(mynumber);

    int *myIntPtr = new int;
    *myIntPtr = 11;
    std::cout << myIntPtr << std::endl;
    std::cout << *myIntPtr << std::endl;

    return 0;
}

void print(std::string *s){
    std::cout<< *s <<std::endl;
}

void print(std::string s){
    std::cout<< s <<std::endl;
}

void print(int *i){
    std::cout<< *i <<std::endl;
}

void print(int i){
    std::cout<< i <<std::endl;
}