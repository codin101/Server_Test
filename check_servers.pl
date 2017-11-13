#!/usr/bin/perl


######## Property of Motorola Solutions ############
# Author: Patrick Eff                              #
# Date: 11/12/2017                                 #
####################################################

use IO::Socket;
use XML::Simple;
use Getopt::Long;
use Data::Dumper;
use Sys::Hostname;

use strict ;
use warnings ;
use feature qw(say);

my $debug = 0 ;
my $CONFIG_FILE = "servers.xml";

sub usage()
{
	say "usage: ./check_servers.pl <servers.xml> <-d>";
	exit 1;
}

sub fatal($)
{
	say "$_[0]";
	exit 1;
}

sub runTest($$)
{
	my $server = shift ;
	my $port = shift ;
	
	say "HN: $server\tPort: $port" if $debug ;

	my $inetAddr = gethostbyname($server); # binary forma, not an IP
	my $sock_addr = sockaddr_in($port,$inetAddr);

	socket(SOCK_FD,AF_INET,SOCK_STREAM,getprotobyname("tcp")) || fatal("could not open socket()");	
	connect(SOCK_FD,$sock_addr) || die "could not connect()\n" ;

	say "Connected to $server:80";
	
#	my $GET_REQ = "GET / HTTP/1.1\r\nUser-Agent: my-own\r\nHost: $server\r\nAccept: */*\r\n\r\n";
#	send(SOCK_FD,$GET_REQ,0);

}

################ MAIN ###################

# IP:Port tcp connect)) -> remote

my $parser = new XML::Simple;
my $d = $parser->XMLin($CONFIG_FILE);   
my @arr = @{ $d->{'server'} } ;

foreach my $entry(@arr)
{
	
	my $port = $entry->{port};
	my $hostName = $entry->{hostname};
	
	runTest($hostName,$port);
}


