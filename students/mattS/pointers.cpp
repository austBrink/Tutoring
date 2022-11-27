#include <iostream>

/* This assignment is due by midnight Sunday as noted in the Syllabus No late
submissions will be accepted for credit 1) Using Visual Studio or your selected
IDE, create a single C++ program solution to meet the requirements for both
Chapter #9 Programming Challenge #2 “Test Scores #1” and Challenge #3 “Drop
Lowest Score” on page 553 of the textbook.

2) You must use good programming style as shown in the examples in the textbook
to include ample comments in your source code. You must include helpful
information in a header block such as the program description, the source of
your program, your name, and the date.

3) Your program must input test scores from your choice of either the keyboard
or a file.

4) Your program must include input validation to not accept negative scores, and
show that your validation checking works by inputting an invalid score of -60
first, and then inputting and accepting the following required scores: 90, 85,
100, 93, 87, 75, 100, 88, 97, and 82.

5) You must store the 10 input scores into a 10-element array in dynamically
allocated memory. Your dynamically allocated memory must be freed when no longer
needed at the end of your program.

6) You must have a function to sort your array elements in ascending order with
the function’s parameter for the array using a pointer. You may use any sorting
algorithm you want.

 7) You must display your 10 sorted array elements.

 8) You must have a function to calculate the average of the array’s elements
with the function’s parameter for the array using a pointer.

 9) You must get the correct average value of the 10 array elements and display
the calculated average.

 10) In the same program execution you must then drop the lowest score, and call
the average function again to get the correct average value for the remaining 9
scores, and display the correct calculated average.

 11) Package your IDE screen snapshot, your complete C++ source code, and your
output screen snapshot(s) for your program’s execution, with your personal
information at the top of the page, in a single Word or PDF file and submit by
the due date/time.
*/

void print(std::string x, bool newLine);
void print(int x, bool newLine);
void print(double x, bool newLine);
void loadArrayWithScores(int *arr, int SIZE);
int getUserInteger();
void printArray(int *arr, int SIZE);
void selectionSort(int *myArray, int n);
double getAverage(int *arr, int SIZE);
void removeFirstItemFromArray(int *arr, int *arrSmall, int SIZE);

int main() {
  // we have a size defined by the user.
  // now allocate a new array with this size...
  int SIZE = getUserInteger();
  int *scores = new int[SIZE];

  loadArrayWithScores(scores, SIZE);
  printArray(scores, SIZE);

  selectionSort(scores, SIZE);
  // sort(SIZE, scores);
  printArray(scores, SIZE);

  print(getAverage(scores, SIZE), true);

  int small = SIZE - 1;

  int *scoresWithDrop = new int[small];

  removeFirstItemFromArray(scores, scoresWithDrop, SIZE);

  printArray(scoresWithDrop, SIZE - 1);

  print(getAverage(scoresWithDrop, SIZE-1), true);

  // now we need the scores from the user.
  // use the getUserInteger function to store scores in array....
}

#include <stdio.h>

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

void print(double x, bool newLine) {
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
  for (int i = 0; i < SIZE; i++) {
    std::cout << "Score number " << i + 1 << ": ";
    std::cin >> temp;
    // check to see if temp is positive.... Input validation
    while (temp < 0) {
      print("Please enter a number greater than 0: ", false);
      std::cin >> temp;
    }
    arr[i] = temp;
  }
}

void printArray(int *arr, int SIZE) {
  print("scores: { ", false);
  for (int i = 0; i < SIZE; i++) {
    print(arr[i], false);
    if (i + 1 != SIZE) {
      print(", ", false);
    }
  }
  print(" }", true);
}

void swap(int *xp, int *yp) {
  int temp = *xp;
  *xp = *yp;
  *yp = temp;
}

void selectionSort(int *myArray, int n) {
  int i, j, min_idx;

  // One by one move boundary of
  // unsorted subarray
  for (i = 0; i < n - 1; i++) {
    // Find the minimum element in
    // unsorted array
    min_idx = i;
    for (j = i + 1; j < n; j++)
      if (myArray[j] < myArray[min_idx])
        min_idx = j;

    // Swap the found minimum element
    // with the first element
    if (min_idx != i)
      swap(&myArray[min_idx], &myArray[i]);
  }
}

double getAverage(int *arr, int SIZE) {
  int sum = 0;
  for (int i = 0; i < SIZE; i++) {
    sum += arr[i];
  }
  return (sum + 0.0) / SIZE;
}

void removeFirstItemFromArray(int *arr, int *arrSmall, int SIZE) {
  // index from one to skip the first element.
  std::cout << "the array" << std::endl;
  for (int i = 0; i < SIZE - 1; i++) {
    arrSmall[i] = arr[i + 1];
  }
}
