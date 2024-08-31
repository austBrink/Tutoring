/**
 * To explain and review pointers
 */
#include<iostream>


int main () {

    int anInt = 10; // no big deal, just an int

    int *anIntPointer = &anInt; // we just assigned an int address to the address of our int. 
    // a pointer that points to the address of the int we have

    int aCopyOfInt = *anIntPointer; // we just grabbed what lives at the address that anIntPointer is keeping.


    return 0;
} 