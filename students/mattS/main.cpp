#include <iostream>
int numberOfStudents = 0;
std::string studentNames[25] = {""};
int main() {
  do {
    std::cout << "please enter a valid number of students (1-25)" << std::endl;
    std::cin >> numberOfStudents;
  } while (numberOfStudents < 1 || numberOfStudents > 25);
  // get as many names as the user wants to enter.
  std::string temp;
  for (int i = 0; i < numberOfStudents; i++) {
    std::cout << "Enter the number " << i + 1 << " name" << std::endl;
    std::cin >> temp;
    studentNames[i] = temp;
  }

  // for (int i = 0; i < 25; i++) {
  //   if (studentNames[i].compare("") != 0) {
  //     std::cout << studentNames[i];
  //   }
  // }
  // now we must sort student names.
  // if .compare returns < 0 that means the second string is lexiconically less than the first string.
  // claim the first student name is the smallest.
  std::string first = studentNames[0];
  for(int i = 0; i <numberOfStudents; i++){
    if(studentNames[i].compare(first) < 0){
      first = studentNames[i];
    }
  }
  std::cout<<"The first student is..." << first << std::endl;
  
  std::string last = studentNames[0];
  for(int i = 0; i <numberOfStudents; i++){
    if(studentNames[i].compare(last) > 0){
      last = studentNames[i];
    }
  }
  std::cout<<"The last student is..." << last <<std::endl;
}