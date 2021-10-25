#include "Student.h"
#include<iostream>

using namespace std;

Student::work(){
  std::cout << "My work is to get projects and assignments done on time." << endl;

  w.work();
}

Student::nextWorker(Worker worker){
  w = worker;
}
