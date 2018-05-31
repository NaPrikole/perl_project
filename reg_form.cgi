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

my $error = "";


my $regexp =~ /[A-Za-z-_0-9]/;
#if ($login eq ""){
if ($login !~ /^[A-Za-z0-9_-]{3,16}$/) {
   
   print "Registration faled !!!";
   print '<meta http-equiv="refresh" content="0;url=index.cgi">';
   return 0;  
}
elsif ( $password !~ /^[A-Za-z0-9_-]{3,16}$/){
#elsif ($password ne $regexp || $password eq "") {
   
   print "Registration faled!!!";
   print '<meta http-equiv="refresh" content="0;url=index.cgi">';
   return 0;
}


my $dbh = DBI->connect("DBI:mysql:user1:localhost", 'user1', 'user1');
my $sql = "INSERT INTO users (name, password) 
VALUES ('$login', '$password')";
my $sth = $dbh->prepare($sql);
   $sth->execute;
print "Congratiolations - registration is seccessful !!!";
print '<meta http-equiv="refresh" content="0;url=index.cgi">';













