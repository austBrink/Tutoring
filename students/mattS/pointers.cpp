#include <iostream>

// This assignment is due by midnight Sunday as noted in the Syllabus No late submissions will be accepted for credit 1) Using Visual Studio or your selected IDE, create a single C++ program solution to meet the requirements for both Chapter #9 Programming Challenge #2 “Test Scores #1” and Challenge #3 “Drop Lowest Score” on page 553 of the textbook. 2) You must use good programming style as shown in the examples in the textbook to include ample comments in your source code. You must include helpful information in a header block such as the program description, the source of your program, your name, and the date. 3) Your program must input test scores from your choice of either the keyboard or a file. 4) Your program must include input validation to not accept negative scores, and show that your validation checking works by inputting an invalid score of -60 first, and then inputting and accepting the following required scores: 90, 85, 100, 93, 87, 75, 100, 88, 97, and 82. 5) You must store the 10 input scores into a 10-element array in dynamically allocated memory. Your dynamically allocated memory must be freed when no longer needed at the end of your program. 6) You must have a function to sort your array elements in ascending order with the function’s parameter for the array using a pointer. You may use any sorting algorithm you want. 7) You must display your 10 sorted array elements. 8) You must have a function to calculate the average of the array’s elements with the function’s parameter for the array using a pointer. 9) You must get the correct average value of the 10 array elements and display the calculated average. 10) In the same program execution you must then drop the lowest score, and call the average function again to get the correct average value for the remaining 9 scores, and display the correct calculated average. 11) Package your IDE screen snapshot, your complete C++ source code, and your output screen snapshot(s) for your program’s execution, with your personal information at the top of the page, in a single Word or PDF file and submit by the due date/time.

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
