#!/usr/bin/perl -w 
use strict;
while(<>){
    s/[A-Za-z]//g;
    s/(.)/$1\n/g;
    print
}
