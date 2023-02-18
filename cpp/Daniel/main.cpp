#include <iostream>


int main () {
   std::cout <<"LOOPS"<< std::endl;
   // for loop (range of numbers) number loop. 
   // print the range of number 1-10 
   // while loop (while a condition is true) value based loop
   // while the user login is true, display welcome
   // first print a range of number to the screen...
   // forward or ascending loop
   for(int i = 0; i <= 10; i++) {
        std::cout<<i<<std::endl;
   }
   std::cout<<"==========================="<<std::endl;
    // descending loop
    // each run of a loop is called an iteration 
   for(int i = 10; i > 0; i-=2) {
        std::cout<<i<<std::endl;
   }
   // while loops 
   int isNewUser = 1; // 1 is true 0 is false
   // I wanted to print hello to the screen while isNewUser is true / 1
    while (isNewUser == 1) {
        std::cout<<"Hello, New user"<<std::endl;
        isNewUser = 0;
    }
    int counter = 0;
    while (counter < 10) {
        std::cout<<counter<<std::endl;
        counter++;
    }
}