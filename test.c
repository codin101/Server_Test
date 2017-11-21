#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{	

	const char *str1 = "stdout";
	const char *str2 = "stderr";

	write(1,str1,strlen(str1));
	write(2,str2,strlen(str2));
		
	return 0;

}//main
