#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>
#include <sys/socket.h>
#include <arpa/inet.h>

static void fatal(const char *str)
{
	puts(str);
	exit(1);

}


int main(void)
{

	struct hostent *host = gethostbyname("www.youtube.com");
	if( host == NULL )
		fatal("gethostbyname() failed");

	

	return 0;
}//main
