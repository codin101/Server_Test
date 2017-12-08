#ifndef _LIST_H
#define _LIST_H

#include "node.h"

typedef struct List List;

struct List
{
	Node *head;
	Node *tail;
};

void append(List *list,int data);
void insertAt(List *list,int position,int data);
void reverseList(List *list);
void printList(List *list);

#endif
