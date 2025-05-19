#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* link;
} Node;

Node* creatNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->link = NULL;
    return newNode;
}

void insertNode(Node* head, int data) {
    Node* newNode = creatNode(data);
    if (head == NULL) {
        head = newNode;
        newNode->link = head;
    } else {
        Node* tmp = head;
        while (tmp->link != head)
            tmp = tmp->link;

        tmp->link = newNode;
        newNode->link = head;
    }
}

void deleteNode(Node* head, int data) {
    Node* curr = head;
    Node* prev = NULL;
    
}

Node* head = NULL;