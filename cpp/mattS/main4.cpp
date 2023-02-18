#include <iostream>

// function declarations
void printArray(int a[]);
int linearSearch(int a[], int thingToFind);
void outPut2 (int a[]);
int findAndCount (int a[], int thingToFind);
void outPut3 (int a[]);
void selectionSort(int n);
void output4();
int binarySearch(int arr[], int l, int r, int x);
void output5();
void output6();

int myArray[] = { 23,17,5,90,12,44,38,84,77,3,66,55,1,19,37,88,8,97,25,50,75,61,49 };
int binarySearchCount = 0;
int globalSearchCount = 0;

int main () {
    // output 1 or 6 print unsorted array 
    std::cout << "This is output 1 of 6:" <<std::endl;
    std::cout << "-----------------------------------------" << std::endl;
    printArray(myArray);
    std::cout << std::endl;

    // output 2 or 6. Print each linear search
    outPut2(myArray);

    // output 3 of 6 Print each linear search with a count 
    outPut3(myArray);

    // output 4 of 6, sort the array and show 
    output4();

    // ....
    output5();

    output6();

    return 0;
};

void printArray(int a[]) {  
    for (int i = 0; i<23; i++) {
        std::cout<< a[i];    
    }
    std::cout << std::endl;
}

// linear search
int linearSearch (int a[], int thingToFind) {
    for(int i = 0; i<23; i++) {
        if(thingToFind == a[i]) {
            // instead of 0 index say 1...
            return i+1;
        }
    }
    return -1;
}

// linear search with a count 
int findAndCount (int a[], int thingToFind) {
    int count = 0;
    for(int i = 0; i<23; i++) {
        count++;
        if(thingToFind == a[i]) {
            return count;
        }
    }
    return count;
}

// need to find ... 25, 30, 50, 75, and 92
void outPut2 (int a[]) {
    std::cout<<"this is output 2 of 6:"<<std::endl;
    std::cout << "-----------------------------------------" << std::endl;          std::cout<<linearSearch(a,25)<<", ";
    std::cout<<linearSearch(a,30)<<", ";
    std::cout<<linearSearch(a,50)<<", ";
    std::cout<<linearSearch(a,75)<<", ";
    std::cout<<linearSearch(a,92);
    std::cout<<std::endl<<std::endl;
}

void outPut3 (int a[]) {
    std::cout<<"this is output 3 of 6"<<std::endl;
    std::cout << "-----------------------------------------" << std::endl;  
    std::cout<<findAndCount(a,25)<<", ";
    std::cout<<findAndCount(a,30)<<", ";
    std::cout<<findAndCount(a,50)<<", ";
    std::cout<<findAndCount(a,75)<<", ";
    std::cout<<findAndCount(a,92)<<", ";
    std::cout<<std::endl<<std::endl;
}

// sort our array and ready it for binary search. 
void output4 (){
    // use selection sort to sort the array
    selectionSort(23);
    std::cout << "this is output 4 of 6" <<std::endl;
    std::cout << "-----------------------------------------" << std::endl;  
    printArray(myArray);
    std::cout<<std::endl;
}

// selection sort came from https://www.geeksforgeeks.org/selection-sort/
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
void selectionSort (int n)
{
    int i, j, min_idx;
 
    // One by one move boundary of
    // unsorted subarray
    for (i = 0; i < n-1; i++)
    {
        // Find the minimum element in
        // unsorted array
        min_idx = i;
        for (j = i+1; j < n; j++)
        if (myArray[j] < myArray[min_idx])
            min_idx = j;
 
        // Swap the found minimum element
        // with the first element
        if(min_idx!=i)
            swap(&myArray[min_idx], &myArray[i]);
    }
}
 

// came from https://www.geeksforgeeks.org/binary-search/
// A iterative binary search function. It returns
// location of x in given array arr[l..r] if present,
// otherwise -1
int binarySearch(int arr[], int l, int r, int x)
{
    while (l <= r) {
        // we added the count to show how many iterations of binary search we needed. 
        binarySearchCount ++;
        int m = l + (r - l) / 2;
 
        // Check if x is present at mid
        if (arr[m] == x)
            return m;
 
        // If x greater, ignore left half
        if (arr[m] < x)
            l = m + 1;
 
        // If x is smaller, ignore right half
        else
            r = m - 1;
    }
 
    // if we reach here, then element was
    // not present
    return -1;
}

void doBinarySearch(int arr[], int l, int r, int x) {
    int found = binarySearch(arr, l, r, x);
    // std::string result = "";
    if (found == -1) {
        std::cout<< x << " not found in array. searched " << binarySearchCount << " times"<<std::endl;
    } else {
        std::cout<< x << " was found at " << found << " searched " << binarySearchCount << " times" << std::endl;
    }
}

void output5() {
    // 25, 30, 50, 75, and 92.
    std::cout<<"this is output 5 of 6:"<<std::endl;
    std::cout << "-----------------------------------------" << std::endl;  
    doBinarySearch(myArray, 0, 22, 25);
    globalSearchCount += binarySearchCount;
    binarySearchCount = 0;
    doBinarySearch(myArray, 0, 22, 30);
    globalSearchCount += binarySearchCount;
    binarySearchCount = 0;
    doBinarySearch(myArray, 0, 22, 50);
    globalSearchCount += binarySearchCount;
    binarySearchCount = 0;
    doBinarySearch(myArray, 0, 22, 75);
    globalSearchCount += binarySearchCount;
    binarySearchCount = 0;
    doBinarySearch(myArray, 0, 22, 92);
    globalSearchCount += binarySearchCount;
    std::cout<<std::endl<<std::endl;
}

void output6() {
    std::cout<<"this is output 6 of 6:" <<std::endl;
    std::cout << "-----------------------------------------" << std::endl;  
    std::cout<<"The total search count was: "<< globalSearchCount << std::endl;
    std::cout<<std::endl<<std::endl;
}