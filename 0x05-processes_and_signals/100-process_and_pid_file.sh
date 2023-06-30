#!/usr/bin/env bash
# Create the file containing its PID
# Displays To infinty and beyond indefinetely
# Displays a string when receiving a sigterm signal
# Displays a string when receiving a SIGINT signal
# Deletes the created file and terminates itself when receiving a SIGQUIT
# or sigterm signal

echo $$ >> /var/run/myscript.pid

# Fuction to handle sigterm signal
handle_sigterm()
{
	echo "I hate the kill command"
	rm /var/run/my_script.pid
	exit
}

# Function to handle SIGINT signal
handle_sigint()
{
	echo "Y U no love me?!"
}
# Function to handle SIGQUIT signal
handle_sigquit()
{
	rm /var/run/my_script.pid
	exit
}
# Display messages indefinitely
trap handle_sigterm SIGTERM
trap handle_sigint SIGINT
trap handle_sigquit SIGQUIT

#Display mesages indefinitely
while true
do
	echo "To infinity and beyond"
	sleep 2
done
