#ifndef Student_H_
#define Student_H_
#include "Worker.h"

using namespace std;

class Student:class Worker{
protected:
  Worker w = null;
public:
  void work();
  void nextWorker(Worker worker);
};
#endif
