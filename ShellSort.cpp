#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

//displays vector so i can see whats going on
void display(vector<int> v, int n){
  for(int i = 0; i < n; i++){
    std::cout << v[i] << " ";
  }
  std::cout << endl;
}

//wrtes to a new file
void write(vector<int> v, int n){
  ofstream myFile;
  myFile.open("outputFile.txt");
  for(auto i = v.begin(); i != v.end()-1; i++){
    myFile << *i << endl;
  }
  myFile.close();
};

//sorts vector using shellsort
void shellSort(vector<int> v, int n){
  for(int gap = n / 2; gap > 0; gap /= 2){
    for(int i = gap; i < n; i+= 1){
      int temp = v[i];
      int j;
      for(j = i; j >= gap && v[j - gap] > temp; j -= gap){
        v[j] = v[j - gap];
      }
    v[j] = temp;
    }
  }
  write(v, n);
};

//reads from file and puts values into a linked list
void read(vector<int> v, string fileName){
  ifstream myFile;
  myFile.open(fileName);
  int n = -1;
  int value;
  while(myFile){
    myFile >> value;
    v.push_back(value);
    n++;
  }
  shellSort(v, n);
};

int main(int argc, char* argv[]) {
  if(argc < 2){
    std::cerr << "Usage: " << argv[0] << " FILENAME" << endl;
    return 1;
  }
  std::vector<int> v;
  std::string fileName = argv[1];
  read(v, fileName);

  return 0;
};
