#include<iostream>

class Node {
    public:
    Node(int _val, Node *_next) {
        val = _val;
        next = _next; 
    };
    int val;
    Node *next;
};

Node* sumList(Node *num1, Node *num2) {
    int carry = 0,val1,val2;
    Node *res = new Node(0,NULL);
    Node *start = res;
    Node *previous;
    if (num1 == NULL && num2 == NULL) {
        return NULL;
    }
    while (num1 != NULL || num2 != NULL) {
        if (num1 != NULL) {
            val1 = num1 -> val;
            num1 = num1 -> next;
        }
        else    val1 = 0;
        if (num2 != NULL) {
            val2 = num2 -> val;
            num2 = num2 -> next;
        }
        else    val2 = 0;
        res -> val = (val1 + val2 + carry) % 10;
        carry =  (val1 + val2 + carry) / 10;
        res -> next = new Node(0,NULL);
        previous = res;
        res = res -> next;
    }
    if (carry == 1)     res -> val = 1;
    else    previous -> next = NULL;
    return (start);
}

int main()
{
    Node *test;

    Node *num1 = new Node(6,new Node(1,new Node(7,NULL)));
    Node *num2 = new Node(2,new Node(9,new Node(5,NULL)));
    test = sumList(num1,num2);
    std::cout << test -> val << test -> next -> val << test -> next -> next-> val << test -> next -> next-> next -> val; 
}