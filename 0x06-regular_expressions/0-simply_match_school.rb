#!/usr/bin/env ruby
# Regular Expression that  match school
# \b is a word boundary anchor that ensures the pattern matches only when 
# School is a complete word and not part of a larger word
# ARGV[0], allows us to access the first commandline arg ie
# ./match.rb "Best School", "Best School is the first arg that will
# be assigned to text var
# scan returns an array of all matches found in the text
# puts prints the matched results by joing the elems of the matches
pattern = /\bSchool\b/
text = ARGV[0]
matches = text.scan(pattern)
puts matches.join
