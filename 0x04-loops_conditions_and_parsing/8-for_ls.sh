#!/usr/bin/env bash
# This script displays the content of the current directory in a list format, showing only the part of the name after the first dash

for file in *; # * reps all files and directories
do
	#checks if the file is not hidden
	if [[ "${file:0:1}" != "." ]]; #0 means start, 1 is length
	then
		# Extract the part of the name after the first dash
		name="${file#*-}"
		echo "$name"
	fi
done
