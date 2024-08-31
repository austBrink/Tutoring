/**
 * To explain and review pointers
 */
#include<iostream>

// remember, good habit to declare your functions
void passByReference(int &x); 
void passByValue(int x);
void print(int x);

/**
 * @brief  increment x by one
 * 
 * Illustrates pass by reference
 * 
 * @param  x:  The integer you want to increment
 * 
 * @return void
 */
void passByReference(int &x) {
    ++x;
}

// doxygen comments
/**
 * @brief  increment x by one
 * 
 * Illustrates pass by value
 * 
 * @param  x:  the integer you want to increment
 * 
 * @return void
 */
void passByValue(int x){
    ++x;
}


/**
 * @brief  cout stuff
 * 
 * abbreviate the std::cout process to print stuff
 * 
 * @param  x:  the integer you want to increment
 * 
 * @return void
 */
void print(int x) {
    std::cout << x;
    std::cout << std::endl;
}


int main () {
    
    // declared a integer on the stack. No big deal.
    // REMEMBER stuff in a function is typically on the stack and gets destoyed after function exit.
    // This is in contrast to stuff on the heap, which is anything created with the new operator
    int myInteger = 4;

    // show what we have
    print(myInteger);

    // So pass by value just means our function is going to make a copy of what we gave it and work with that.
    passByValue(myInteger);

    // see? this will just print what we have above
    print(myInteger);

    // this function has a '&' in front of the parameter which means we are passing this value by reference.
    // not a copy, this will access the variable as it is in the scope that called this function.
    // you can see that demonstrated by the fact x STAYTED incremented after we called this function
    passByReference(myInteger);

    print(myInteger);

    return 0;
} 