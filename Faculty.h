#ifndef Faculty_H_
#define Faculty_H_
#include "Worker.h"

using namespace std;

class Factulty: class Worker{
protected:
  Worker w = null;
public:
  void work();
  void nextWorker(Worker worker);
};
#endif
