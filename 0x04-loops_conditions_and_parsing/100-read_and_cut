#!/usr/bin/env bash
# Scripts that displays the content of the file /etc/passwd

while read -r line;
do
	echo "$line" | cut -d : -f 1,3,6
done < /etc/passwd
