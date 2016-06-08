#!/usr/bin/perl -w
use strict;

my $ras_pi_IP;
my $nmap = `nmap -p T:22 192.168.1.0/26`;
$nmap =~ s/\nStarting Nmap.*?\n//; # delete 2 intro lines
my @textblocks = split(/\n\n/, $nmap);
for (@textblocks){
    next if /Nmap done/;
    my ($host, $updown, $header, $port) = split(/\n/);
    if ($port =~ /open/){
	$host =~ s/Nmap scan report for 192/192/;
	$ras_pi_IP = $host;
	last;
    }
}

die("No open port 22 found" . $!) if not defined($ras_pi_IP);

my $cmd = 'rsync pi@' . $ras_pi_IP .
    ':/var/www/database/temperature.db temperature.new 2> /dev/null';
print $cmd . "\n";
system($cmd);
