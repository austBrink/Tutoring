#include <iostream>

int main () {
   std::cout <<"LOOP PROGRAM"<< std::endl;
   
   // create a program that opens and stays running while the user input is not Q. 
   // there will be a menu display, with an option to print an array to the screen. 

   // first I will make my program data.
   char userChoice = ' ';
   int myArray[] = {1,2,3,4,5,6,7};

   // while loop to keep the program alive until the user wants to quit.
   while(userChoice != 'Q') {
    std::cout << "Enter Q to quit. Enter P to print" <<std::endl;
    std::cin >> userChoice;
    if(userChoice == 'P') {
        // print an array 
        for(int i = 0; i < 7; i++){
            std::cout<<myArray[i]<<std::endl;
        }
    }
   }

}