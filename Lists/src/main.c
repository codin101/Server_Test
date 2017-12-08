#include <stdio.h>
#include <stdlib.h>

#include "list.h"
#include "error.h"

int main(int argc,char **args)
{

	List *list = (List *) calloc( 1, sizeof( List ) );
	if ( list == NULL )
		fatal("could not calloc()");

	int i;
	for( i = 0; i < 10; i++)
		append(list, i + 1);

	printList(list);

	reverseList(list);

	printList(list);

	insertAt(list,4,24);

	printList(list);

	return 0;

}
