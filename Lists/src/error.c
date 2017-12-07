#include <stdio.h>
#include <stdlib.h>

#include "include/error.h"

void fatal(const char *str)
{
	puts(str);
	exit(1);
}

