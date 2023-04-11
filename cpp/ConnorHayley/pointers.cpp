#include <iostream>
#include <stdio.h>

// DECLARE functions before DEFINING LATER
void loadArrayWithScores(int *arr, int SIZE);
int getNumberOfScores();
void printPointerArray(int *arr, int SIZE);
void move(int *myArray, int n);
void sort(int *myArray, int n);
double getAverage(int *arr, int SIZE);
void dropLowestScore(int *arr, int *arrSmall, int SIZE);

int main() {

  int NUM_OF_SCORES = getNumberOfScores();
  int *scores = new int[NUM_OF_SCORES];

  loadArrayWithScores(scores, NUM_OF_SCORES);

  std::cout<<"GRADES BEFORE SORTING: ";
  printPointerArray(scores, NUM_OF_SCORES);
  std::cout << std::endl;

  sort(scores, NUM_OF_SCORES);

  std::cout << "SORTED GRADES: ";
  printPointerArray(scores, NUM_OF_SCORES);
  std::cout << std::endl;

  std::cout << "AVERAGE GRADE: ";
  std::cout << getAverage(scores, NUM_OF_SCORES) << std::endl;

  int small = NUM_OF_SCORES - 1;

  int *scoresWithDrop = new int[small];

  dropLowestScore(scores, scoresWithDrop, NUM_OF_SCORES);

  std::cout << "GRADES WITHOUT LOWEST: ";
  printPointerArray(scoresWithDrop, NUM_OF_SCORES - 1);
  std::cout << std::endl;

  std::cout << "NEW AVERAGE: ";
  std::cout << getAverage(scoresWithDrop, NUM_OF_SCORES-1) << std::endl;
}

int getNumberOfScores() {
  int userInt;
  std::cout << "How many grades are we processing? ";
  std::cin >> userInt;
  return userInt;
}

void loadArrayWithScores(int *arr, int SIZE) {
  int tempInt;
  for (int i = 0; i < SIZE; i++) {
    std::cout << "GRADE: " << i + 1 << ": ";
    std::cin >> tempInt;
    // dont read a negative number...
    while (tempInt < 0) {
      std::cout << "Only non-negatives please: " << std::endl;
      std::cin >> tempInt;
    }
    arr[i] = tempInt;
  }
}

void printPointerArray(int *arr, int SIZE) {
  for (int i = 0; i < SIZE; i++) {
    std::cout << arr[i];
    if (i + 1 != SIZE) {
      std::cout << ", ";
    }
  }
}

void move(int *xp, int *yp) {
  int temp = *xp;
  *xp = *yp;
  *yp = temp;
}

void sort(int *myArray, int n) {
  int i, j, min_idx;

  for (i = 0; i < n - 1; i++) {

    min_idx = i;
    for (j = i + 1; j < n; j++)
      if (myArray[j] < myArray[min_idx]) {
        min_idx = j;
      }

    if (min_idx != i) {
      move(&myArray[min_idx], &myArray[i]);
    }
      
  }
}

double getAverage(int *arr, int SIZE) {
  int sum = 0;
  for (int i = 0; i < SIZE; i++) {
    sum += arr[i];
  }
  return (sum + 0.00) / SIZE;
}

void dropLowestScore(int *arr, int *arrSmall, int SIZE) {
  for (int i = 0; i < SIZE - 1; i++) {
    arrSmall[i] = arr[i + 1];
  }
}
