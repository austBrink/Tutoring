// Here are the topics to review for the exam: 
// low level vs. high level computer programming languages
// #include statement syntax data 
// type conversions in arithmetic expressions 
// integer values C++ treats as true and false 
// the switch statement 
// input and output file streams 
// loop types 
// local and global variables 
// the static keyword 
// how arrays work in C++ 
// 2-dimensional arrays 
// binary search algorithm linear search algorithm the function and contents of pointers character functions

#include <iostream>
#include <cctype>
#include <sstream>
#include <fstream>

void upper(std::string *s);
void lower(std::string *s);
void reverse(std::string *s);
void getUserString(std::string *s);
void print(std::string *s);
const int MY_NUMBER = 5;


int main (void) {

// // type conversions.... 
//     std::string x = "3";
//     int y = std::stoi(x);
//     std::cout<<y;   

//     // casting 
//     int a = 3;
//     int b = 5;

// //in line type conversion 
//     double rslt = double(b)/double(a);

    // 1 is true 
    // 0 is false

// SWITCH
    // switch(x) {
    //     case x = 2:
    //         thing();
    //         break;
    //     case 



    //     default:
    //         doThing()
    //         break;
    // }

    // 
    std::ifstream myFile;
    myFile.open("yo.txt");
    std::string thisLine = "";
    std::string wholeThing = "";

    int myArray[6][2] = {{1,3},{5,4}};
    
    std::cout << myArray[4];

    while(std::getline(myFile,thisLine,'\n')) {

    }





// do while (alwasy do it at least once )
// while (logical limit / control)
// for (numerical limits)

    




    return 0;
}