#!/usr/bin/perl

use IO::Socket;
use Getopt::Std;
use XML::Simple ;

use strict ;
use warnings ;

my $CONFIG_FILE = "servers.xml";

sub usage()
{
	print "usage: ./check_servers.pl <servers.xml>\n";
	exit 1;
}

sub runTest($)
{
	my $server = shift ;

}	

sub char_handler
{
	;
}

sub default_handler
{
	;
}	

my $parser = new XML::Parser(ErrorContext => 1);

$parser->setHandlers(Char => \&char_handler,Default => \&default_handler);

$parser->parsefile($CONFIG_FILE);





