#!/usr/bin/perl
use lib '/home/user1/public_html/perltest/libs';
use CGI qw(:cgi-lib :escapeHTML :unescapeHTML);
use CGI::Carp qw(fatalsToBrowser);
use File::Basename qw(dirname);
use lib dirname(__FILE__) . '/libs';
use Data::Dumper;
use Tools::FileSystem;
use DBI;
use Template;
#use HTML::Template;

my $dbh = DBI->connect("DBI:mysql:user1:localhost", 'user1', 'user1');
my $sql = q/select * from articles/;
my $sth = $dbh->prepare($sql);
   $sth->execute;

my $rows;
push @{$rows}, $_ while $_ = $sth->fetchrow_hashref();
 


	my $template = HTML::Template->new(filename => 'index.html');
    
	$template->param(ROWS => $rows);

print "Content-Type: text/html\n\n", $template->output;

$dbh->disconnect();






