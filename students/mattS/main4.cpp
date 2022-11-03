#include <iostream>


void printArray(int a[]);
int find(int a[], int thingToFind);
void outPut2 (int a[]);
int findAndCount (int a[], int thingToFind);
void outPut3 (int a[]);
void selectionSort(int n);
void output4();
int binarySearch(int arr[], int l, int r, int x);
void output5();
void output6();


int myArray[] = {23,17,5,90,12,44,38,84,77,3,66,55,1,19,37,88,8,97,25,50,75,61,49};
int binarySearchCount = 0;
int globalSearchCount = 0;
int main () {
    

    //output 1 or 6
    std::cout << "This is output 1 of 6:" <<std::endl;
    printArray(myArray);

    outPut2(myArray);

    outPut3(myArray);

    output4();

    output5();

    output6();

    return 0;
};

void printArray(int a[]) {
    
    for(int i = 0; i<23; i++){
        std::cout<< a[i] << std::endl;
    }
}

// lineaer search
int find (int a[], int thingToFind) {
    for(int i = 0; i<23; i++) {
        if(thingToFind == a[i]) {
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

// 25, 30, 50, 75, and 92
void outPut2 (int a[]) {
    std::cout<<"output 2 of 6:"<<std::endl;
    std::cout<<find(a,25)<<std::endl;
    std::cout<<find(a,30)<<std::endl;
    std::cout<<find(a,50)<<std::endl;
    std::cout<<find(a,75)<<std::endl;
    std::cout<<find(a,92)<<std::endl;
}

void outPut3 (int a[]) {
    std::cout<<"output 3 of 6"<<std::endl;
    std::cout<<findAndCount(a,25)<<std::endl;
    std::cout<<findAndCount(a,30)<<std::endl;
    std::cout<<findAndCount(a,50)<<std::endl;
    std::cout<<findAndCount(a,75)<<std::endl;
    std::cout<<findAndCount(a,92)<<std::endl;
}

// sort our array and ready it for binary search. 
void output4 (){
    selectionSort(23);
    std::cout << "This is output 4 of 6" <<std::endl;
    printArray(myArray);
}

// selection sort came from https://www.geeksforgeeks.org/selection-sort/
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
void selectionSort(int n)
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
        std::cout<< x << " was found at " << found << " searched " << binarySearchCount << " times." << std::endl;
    }
   
}

void output5() {
    // 25, 30, 50, 75, and 92.
    std::cout<<"Output 5 of 6:"<<std::endl;
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
}

void output6() {
    std::cout<<"Output 6 of 6:" <<std::endl;
    std::cout<<"The total search count was "<<globalSearchCount << std::endl;
}