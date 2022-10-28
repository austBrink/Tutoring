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

int getTotal(int arr[][5], int row, int column);
double getAverage(int arr[][5], int row, int column);
int getRowTotal(int arr[][5], int row, int column);
int getColumnTotal(int arr[][5], int row, int column);
int getHighestInRow(int arr[][5], int row, int column);
int getLowestInRow(int arr[][5], int row, int column);


// int array2D[2][5] = {{5,10,8,7,3},{4, 9, 6, 2, 1}};

int main () {
    // read the data for the array from the file. its called numbers.txt
    std::ifstream input("numbers.txt");
    int array2D[2][5] = {0};
    std::string s;
    for (int i = 0; i < 2; i++)
    {
        std::getline(input, s);
        std::istringstream iss(s);
        std::string num; 
        int j = 0;
        while (std::getline(iss, num, ',')) { 
            array2D[i][j] = std::stoi(num);
            j++;
        } 
    }

    // first arg is array, second is the row number starting at 0, third is column number starting at 0. 
    printArray(array2D,2,5);
    print(getTotal(array2D,2,5));
    print(getAverage(array2D,2,5));

    print(getRowTotal(array2D,0,5));
    print(getRowTotal(array2D,1,5));

    print(getColumnTotal(array2D,2,0));
    print(getColumnTotal(array2D,2,1));
    print(getColumnTotal(array2D,2,2));
    print(getColumnTotal(array2D,2,3));
    print(getColumnTotal(array2D,2,4));

    print(getHighestInRow(array2D,0,5));
    print(getHighestInRow(array2D,1,5));

    print(getLowestInRow(array2D,0,5));
    print(getLowestInRow(array2D,1,5));


    return 0;
}

int getTotal(int arr[][5], int row, int column){
    int sum = 0;
    for (int i = 0; i < row; i++) {
        for(int j = 0; j < column; j++) {
            sum = sum + arr[i][j];
        }
        std::cout<<std::endl;
    }
    return sum;
}

double getAverage(int arr[][5], int row, int column){
    int sum = 0;
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < column; j++) {
            sum = sum + arr[i][j];
        }
        std::cout<<std::endl;
    }
    return double(sum) / double(double(row)*double(column));
}

int getRowTotal(int arr[][5], int row, int column){
    int rowTotal = 0;
    for(int j = 0; j < column; j++) {
        rowTotal = rowTotal + arr[row][j];
    }
    return rowTotal;
}

int getHighestInRow(int arr[][5], int row, int column){
    int max = arr[0][0];
    for(int j = 0; j < column; j++) {
        if(max < arr[row][j]){
            max = arr[row][j];
        }
    }
    return max;
}

int getLowestInRow(int arr[][5], int row, int column){
    int min = arr[0][0];
    for(int j = 0; j < column; j++) {
        if(min > arr[row][j]){
            min = arr[row][j];
        }
    }
    return min;
}

int getColumnTotal(int arr[][5], int row, int column){
    int columnTotal = 0;
    for(int i = 0; i < row; i++) {
        columnTotal = columnTotal + arr[i][column];
    }
    return columnTotal;
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