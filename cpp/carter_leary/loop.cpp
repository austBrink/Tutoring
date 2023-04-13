#include <iostream>

int main() {
    
    // DO WHILE 
    // IT should run from 1 - 5 
    // in a while we need to explicitly declare a control value.
    std::cout << "DO WHILE LOOP" << std::endl;
    int i = 1;
    do {
        std::cout << "i = " << i; 
        if (i == 5) {
            std::cout<<std::endl;
        } else {
            std::cout << ", ";
        }
        i++;
    } while (i <= 5);

    // NOW FOR THE FOR LOOP 
    
    std::cout << "FOR LOOP" << std::endl;

    for (int i = 1; i <= 5; i++){
        std::cout << "i = " << i; 
        if (i == 5) {
            std::cout << std::endl;
        } else {
            std::cout << ", ";
        }
    }

    // set i back to one....
    i = 1;
    std::cout << "REGULAR WHILE LOOP" << std::endl;
    while (i <= 5) {
        std::cout << "i = " << i; 
        if (i == 5) {
            std::cout<<std::endl;
        } else {
            std::cout << ", ";
        }
        i++;
    }

    return 0;
}
