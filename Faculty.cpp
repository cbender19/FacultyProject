#include "Faculty.h"
#include<iostream>

using namespace std;

Faculty::work(){
  std::cout << "My work is to teach and help students to reach their goals.
  Als, I evaluate the student's projects and assignments" << endl;

  w.work();
}

Faculty::nextWorker(Worker worker){
  w = worker;
}
