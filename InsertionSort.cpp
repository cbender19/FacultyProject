#include <iostream>
#include <fstream>

using namespace std;

//creates linked list
struct Node{
public:
  int data;
  Node *next;
};

//add values to the linked list
void append(struct Node** head, int n) {
  Node *temp = new Node;
  Node *last = *head;
  temp -> data = n;
  temp -> next = NULL;

  if(*head == NULL){
    *head = temp;
    return;
  }

  while(last -> next != NULL){
    last = last -> next;
  }

  last -> next = temp;
  return;
};

//deletes last value in linked list due to double values
Node* deleteLast(struct Node* head){
  if(head == NULL){
    return NULL;
  }

  if(head -> next == NULL){
    delete head;
    return NULL;
  }

  Node* secondLast = head;
  while(secondLast -> next -> next != NULL){
    secondLast = secondLast -> next;
  }

  delete (secondLast -> next);
  secondLast -> next = NULL;

  return head;
};

//displays the linked list
//used to keep track of what was going on with my list
void display(Node *node){
  while (node != NULL) {
    std::cout << node -> data << ", ";
    node = node -> next;
  }

  if(node == NULL){
    std::cout << endl;
  }
};

//sorts the linked list
void sort(struct Node** head){
  if((*head) == NULL || (*head) -> next == NULL){
    return;
  }
  Node* temp = (*head) -> next;
  while(temp != NULL){
    int ldata = temp -> data;
    int found = 0;
    Node* temp2 = (*head);
    while(temp2 != temp){
      if((temp2 -> data > temp -> data) && found == 0){
        ldata = temp2 -> data;
        temp2 -> data = temp -> data;
        found = 1;
        temp2 = temp2 -> next;
      }
      else{
        if(found == 1){
          int temp3 = ldata;
          ldata = temp2 -> data;
          temp2 -> data = temp3;
        }
        temp2 = temp2 -> next;
      }
    }
    temp2 -> data = ldata;
    temp = temp -> next;
  }
};

//wrtes to a new file
void write(struct Node* head){
  if(head == NULL){
    return;
  }
  else{
    ofstream myFile;
    myFile.open("outputFile.txt");
    Node* temp = head;
    while(temp != NULL){
      myFile << temp -> data << endl;
      temp = temp -> next;
    }
    myFile.close();
  }
};

//reads from file and puts values into a linked list
void read(struct Node* head, string fileName){
  ifstream myFile;
  myFile.open(fileName);
  int value;
  while(myFile){
    myFile >> value;
    append(&head, value);
  }
  deleteLast(head);
  sort(&head);
  write(head);
};

int main(int argc, char* argv[]) {
  if(argc < 2){
    std::cerr << "Usage: " << argv[0] << " FILENAME" << endl;
    return 1;
  }
  struct Node* head = NULL;
  std::string fileName = argv[1];
  read(head, fileName);

  return 0;
};
