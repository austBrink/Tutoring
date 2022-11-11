#include <iostream>

void print(std::string x, bool newLine);
void print(int x, bool newLine);
void loadArrayWithScores(int *arr, int SIZE);
int getUserInteger();
void printArray(int *arr, int SIZE);


int main () {
    // we have a size defined by the user. 
    // now allocate a new array with this size...
    int SIZE = getUserInteger();
    int *scores = new int(SIZE);

    loadArrayWithScores(scores, SIZE);
    printArray(scores, SIZE);

    // now we need the scores from the user. 
    // use the getUserInteger function to store scores in array....
}

void print(std::string x, bool newLine) {
    if (newLine) {
        std::cout << x << std::endl;
        return;
    }
    std::cout << x;
}

void print(int x, bool newLine) {
    if (newLine) {
        std::cout << x << std::endl;
        return;
    }
    std::cout << x;
}

int getUserInteger() {
    int userInt;
    print("Please enter the amount of scores: ", false);
    std::cin >> userInt;
    return userInt;
}

void loadArrayWithScores(int *arr, int SIZE) {
    int temp;
    for(int i = 0; i < SIZE; i++) {
        std::cout << "print score number " << i+1 << ": ";
        std::cin >> temp;
        // check to see if temp is positive....
        while (temp < 0) {
            print("Please enter a valid number: ", false);
            std::cin >> temp;
        }
        arr[i] = temp;
    }
}

void printArray(int *arr, int SIZE) {
    print("scores: { ", false);
    for (int i = 0; i < SIZE; i++) {
        print(arr[i], false);
        if(i+1 != SIZE){
            print(", ", false);
        }
    }
    print(" }", false);
}
