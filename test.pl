#!/usr/bin/perl

use strict;
use warnings;
use Response;
 
sub psgi_handler {
    my $env = shift;
 
    my $res = Plack::Response->new(200);
    $res->content_type('text/html');
    $res->body("Hello World");
 
    return $res->finalize;
}
