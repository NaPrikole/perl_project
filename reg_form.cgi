#!/usr/bin/perl

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


my $regexp =~ /[A-Za-z][0-9]_-/;

if ($login eq "") {
   print "Registration faled !!!";
   print '<meta http-equiv="refresh" content="1;url=http://192.168.0.15/~user1/perltest/index.cgi">';

}
elsif ($password eq "") {
   print "Registration faled!!!";
   print '<meta http-equiv="refresh" content="1;url=http://192.168.0.15/~user1/perltest/index.cgi">';

}

else {
my $dbh = DBI->connect("DBI:mysql:user1:localhost", 'user1', 'user1');
my $sql = "INSERT INTO users (name, password) 
VALUES ('$login', '$password')";
my $sth = $dbh->prepare($sql);
   $sth->execute;
print "Congratiolations - registration is seccessful !!!";
print '<meta http-equiv="refresh" content="1;url=http://192.168.0.15/~user1/perltest/index.cgi">';
}












