#!/usr/bin/env bash
# Script that checks whether a file exists or not

file="school"


#checks if the file exists
if [ -e "$file" ];
then
	echo "school file exists"

	#checks if the file is empty
	if [ -s "$file" ];
	then
		echo "school file is not empty"
	else
		echo "school file is empty"
	fi

	#checks if the file is a regular file
	if [ -f "$file" ];
	then
		echo "school is a regular file"
	fi
else
	echo "school file does not exist"
fi
