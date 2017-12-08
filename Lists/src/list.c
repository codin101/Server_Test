#include <stdio.h>
#include <stdlib.h>

#include "list.h"

void printList(List *list)
{
	if( list == NULL )
		return ;

	Node *p = list->head;
	while( p != NULL )
	{
		printf("%d\n",p->data);
		p = p->next;
	}	
}

void append(List *list,int data)
{
	
	if( list == NULL )
		return ;

	Node *node = (Node *) calloc( 1, sizeof( Node ) );
	if (node == NULL )
		return ;

	node->data = data;
	node->next = NULL; // calloc() should memset(0)

	if( list->head == NULL )
		list->head = node;
	else if( list->head->next == NULL )
		list->head->next = node;
	else
		list->tail->next = node;

	list->tail = node;
}

void reverseList(List *list)
{
	if( list == NULL )
		return ;

	Node *prev = NULL;
	Node *curr = list->head;
	Node *next = list->head->next;

	while( next != NULL )
	{
		curr->next = prev;
		prev = curr;
		curr = next;
		next = next->next;
	}	
	
	curr->next = prev;
	list->head = curr;
}

void insertAt(List *list,int position,int data)
{
	if( list == NULL || position < 1 )
		return ;

	Node *node = (Node *) calloc( 1, sizeof( Node ) );
	if( node == NULL )
		return ;

	node->data = data;
	node->next = NULL;
		
	Node *p = list->head;

	if( position == 1)
	{
		node->next = p;
		list->head = node;
	}
	else
	{
		int i = 1;
		while( ( i++ + 1 ) < position )
			p = p->next;
		
		node->next = p->next;
		p->next = node;
	}	
}
