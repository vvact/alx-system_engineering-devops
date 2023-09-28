#!/usr/bin/env bash
# A bash script that display the contents of a file using the whie loop + IFS
while IFS=':' read -r -a fields;
do
	echo "The user ${fields[0]} is part of the ${fields[3]} gang, lives in ${fields[5]} and \
		rides ${fields[2]}'s place is protected by the passcode ${fields[1]}, more \
		info about the user here: ${fields[4]}"
done < /etc/passwd; 	
