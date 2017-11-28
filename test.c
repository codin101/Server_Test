#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

static int retCode = 0 ;

int main(void)
{	

	int fd = open("aFile", O_RDONLY | O_NONBLOCK);
	if( fd < 0 )
		return 1;
	

	char buff[512];
	int n = read(fd,buff,sizeof(buff));
	printf("Read %d bytes: \n",n);
	buff[n] = '\0';
	
	puts("the end");
	exit(retCode);
}//main
