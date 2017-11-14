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

	struct hostent *host = gethostbyname("www.wbal.com");
	if( host == NULL )
		fatal("gethostbyname() failed");

	struct in_addr_t *addr = (struct in_addr_t *) host->h_addr_list[0];
	
	struct sockaddr_in server;
	bzero(&server,sizeof(server));

	memcpy(&server.sin_addr.s_addr,addr,sizeof(server.sin_addr));
	server.sin_port = htons(80);
	server.sin_family = AF_INET;

	int sockfd = socket(AF_INET,SOCK_STREAM,0);

	if( connect(sockfd,(struct sockaddr *)&server,sizeof(server)) < 0)
		fatal("connect()");
	
	send(sockfd,"GET / HTTP/1.1\r\n\r\n",strlen("GET / HTTP/1.1\r\n\r\n"),0);

	char buff[1024];
	int n;
	while( ( n = recv(sockfd,buff,sizeof(buff),0) ) > 0 )
	{
			buff[n] = '\0';
			printf("%s",buff);

	}
	

	return 0;
}//main
