#!/usr/bin/env/ ruby
# hb matches the literal characters hb at the beginning
# (t{2,5})captures the letter t repeated 2 to 5 times using a quantifier
# {2, 5} and n matches the n at the end
# The script prints the matchss seperated by \n

pattern /hb(t{2, 5})n/
TEXT = ARGV[0]
matches = text.scan(pattern)
puts matches.join("\n")
