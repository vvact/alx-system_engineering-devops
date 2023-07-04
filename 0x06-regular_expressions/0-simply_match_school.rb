#!/usr/bin/env ruby
# Regular Expression that  match school

pattern = /\bSchool\b/
text = ARGV[0]
matches = text.scan(pattern)
puts matches.join
