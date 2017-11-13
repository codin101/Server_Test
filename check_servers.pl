#!/usr/bin/perl


######## Property of Motorola Solutions ############
# Author: Patrick Eff                              #
# Date: 11/12/2017                                 #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################


use IO::Socket;
use Getopt::Std;
use XML::Simple;
use Data::Dumper;

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



################ MAIN ###################

my $xml_hash = XML::Simple->new( KeepRoot => 1, KeyAttr => 1, ForceArray => 1 );

my $response_hash = eval{ $xml_hash->XMLin( $CONFIG_FILE ) } ;

#print $response_hash->{servers}[0]->{hostname}[0];




