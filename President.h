#ifndef President_H_
#define President_H_
#include "Worker.h"

using namespace std;

class President:class Worker{
protected:
  Worker w = null;
public:
  void work();
  void nextWorker(Worker worker);
};
#endif
