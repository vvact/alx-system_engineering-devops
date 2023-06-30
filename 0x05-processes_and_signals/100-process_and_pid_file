#!/usr/bin/env bash
# Create the file containing its PID
# Displays To infinty and beyond indefinetely
# Displays a string when receiving a sigterm signal
# Displays a string when receiving a SIGINT signal
# Deletes the created file and terminates itself when receiving a SIGQUIT
# or sigterm signal

PRID=$$
echo "$PRID" > /var/run/myscript.pid

handle_sigint()
{
	echo "Y U no love?!"
}
handle_sigquit()
{
	echo "I hate the kill command"
	rm -f /var/run/myscript.pid
	kill -9 $PRID
}

trap handle_sigint SIGINT
trap handle_sigquit SIGQUIT SIGTERM

while true
do
	echo "To infinity and beyond"
	sleep 2
done
