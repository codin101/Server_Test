#!/usr/bin/perl

use Socket;


sub fatal($)
{

	print "$_[0]\n";
	exit 1;
}

### MAIN ###



socket(SOCK_FD,AF_INET,SOCK_STREAM,getprotobyname("c")) || fatal("socket()") ;

$host = "wbal.com";
$port = 80;

connect(SOCK_FD, pack_sockaddr_in($port,inet_aton($host))) || fatal("connect()") ;

$get = "GET / HTTP/1.1\r\nHost: www.wbal.com\r\nConnection: keep-alive\r\nUser-Agent: Chrome\r\nAccept: text/html\r\n";
$line ;
send(SOCK_FD,$get,length($get));
while($line = <SOCK_FD>)
{
	print $line ;
}

