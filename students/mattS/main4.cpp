#include <iostream>


void printArray(int a[]);
int find(int a[], int thingToFind);
void outPut2 (int a[]);
int findAndCount (int a[], int thingToFind);
void outPut3 (int a[]);
void selectionSort(int n);


int myArray[] = {23,17,5,90,12,44,38,84,77,3,66,55,1,19,37,88,8,97,25,50,75,61,49};
int main () {
    
   

    //output 1 or 6
    std::cout << "This is output 1 or 6" <<std::endl;
    printArray(myArray);

    outPut2(myArray);

    outPut3 (myArray);

    selectionSort(23);

    std::cout << "This is output 4 or 6" <<std::endl;
    printArray(myArray);

    return 0;
};

void printArray(int a[]) {
    
    for(int i = 0; i<23; i++){
        std::cout<< a[i] << std::endl;
    }
}

int find (int a[], int thingToFind) {
    for(int i = 0; i<23; i++) {
        if(thingToFind == a[i]) {
            return i+1;
        }
    }
    return -1;
}

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
    std::cout<<"output 2 of 6"<<std::endl;
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

