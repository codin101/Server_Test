#!/usr/bin/perl

use Getopt::Std ;

use strict ;

my $CONFIG_FILE = "servers.txt" ;
my $numArgs = @ARGV ;

if( $numArgs == 1 )
{
	$CONFIG_FILE = $ARGV[0] ;

}

