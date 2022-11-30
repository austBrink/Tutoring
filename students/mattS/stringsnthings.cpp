/* 

1) Using Visual Studio or your selected IDE, create a single C++ program
solution to meet the requirements for Chapter #10 Programming Challenge
#11 “Case Manipulator” on page 609 of the textbook.
3) Your program must input the string “Calhoun Community College” (without
the quotes) from either the keyboard or a file for your program submission,
and you must store this text in a C++ C-string.
4) You must develop and call the specified 3 functions of reverse, lower, and
upper, in that order, from your main function. Each function call must use
the same initial C-string input in Step #3.
5) You must obtain the correct results by displaying all characters converted to
the opposite case for uppercase and lowercase characters, otherwise not
changed, based on each function’s conversion requirements.
6) Package your IDE screen snapshot, your complete C++ source code, and
your output screen snapshot(s) for your program’s execution, with your
personal information at the top of the page, in a single Word or PDF file and
submit by the due date/time.

*/
#include <iostream>
#include <cctype>
#include <sstream>

void upper(std::string *s);
void lower(std::string *s);
void reverse(std::string *s);
void getUserString(std::string *s);
void print(std::string *s);

int main (void) {
    std::string *myString = new std::string;
    getUserString(myString);
    // std::cout << *myString << std::endl;

    reverse(myString);
    print(myString);

    upper(myString);
    print(myString);

    lower(myString);
    print(myString);

    
    return 0;
}

void getUserString(std::string *s) {
    std::cout << "Please Enter a string" << std::endl;
    std::getline(std::cin, *s);
    // std::cin >> *s;
}

void upper(std::string *s){
    std::string::iterator si;
    for(si = s->begin(); si < s->end(); si++){
        *si = toupper(*si);
        // std::cout<<*si<<std::endl;
    }
}

void lower(std::string *s){
    std::string::iterator si;
    for(si = s->begin(); si < s->end(); si++){
        *si = tolower(*si);
        // std::cout<<*si<<std::endl;
    }
}

void reverse(std::string *s){
    std::string::iterator si;
    for (si = s->begin(); si < s->end(); si++) {
        // isupper didn't like checking a dereferenced string iterator pointer....
        // use char instead.... 
        char c = *si;
        if (isupper(c)) {
            *si = tolower(*si);
        } else {
            *si = toupper(*si);
        }
    }
}

void print(std::string *s){
    std::cout<< *s <<std::endl;
}
