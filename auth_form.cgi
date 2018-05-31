#!/usr/bin/perl

use lib '/home/user1/public_html/perltest/libs';
use strict;
use warnings;
use CGI;
use CGI::Carp;
use DBI;


print "Content-type: text/html; charset=utf-8\n\n";

my $cgi = new CGI;


my $login = $cgi->param('login');
my $password = $cgi->param('password');

print $login;
print $password;












