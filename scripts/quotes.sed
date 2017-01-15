#!/bin/sed -i.bak -f quotes.sed # applies changes to all files provided
s/ ''/ ``/g
s/^''/``/g
s/(''/(``/g
