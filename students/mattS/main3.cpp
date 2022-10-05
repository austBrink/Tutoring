// Your program must use a 2-dimensional array of integers of 2 rows and 5
// columns. The first row must have the values 5, 10, 8, 7, and 3. The second
// row must have the values 4, 9, 6, 2, and 1
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

void print(std::string val);
void print(double val);
void printArray(int myArray[][5], int row, int column);

int array2D[2][5] = {{5,10,8,7,3},{4, 9, 6, 2, 1}};

int main () {
    printArray(array2D,2,5);
    std::ifstream input("number.txt");
    int newArray[2][5] = {0};
    std::string s;
    for (int i = 0; i < 2; i++)
    {
        std::getline(input, s);
        std::cout<<s<<std::endl;;
        std::istringstream iss(s);
        std::string num; 
        int j = 0;
        while (std::getline(iss, num, ',')) { 
            newArray[i][j] = std::stoi(num);
            j++;
        } 
    }
    printArray(newArray,2,5);
    return 0;
}

void printArray (int myArray[][5], int row, int column) {
    for(int i = 0; i<row; i++){
        for(int j = 0; j<column; j++){
            std::cout<<myArray[i][j]<<" ";
        }
        std::cout<<std::endl;
    }
}

void print(std::string val) {
    std::cout << val << std::endl;
}

void print(int val) {
    std::cout << val << std::endl;
}

void print(double val) {
    printf( "%f", val);
    std::cout<<std::endl;
}