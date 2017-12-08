#include <stdio.h>
#include <stdlib.h>

#include "error.h"

void fatal(const char *str)
{
	puts(str);
	exit(1);
}

