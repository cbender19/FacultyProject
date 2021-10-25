#ifndef Worker_H_
#define Worker_H_
#include<iostream>

using namespace std;

class Worker{
protected:
  Worker w = null;
public:
  void virtual work();
  void virtual nextWorker(Worker w);
};
#endif
