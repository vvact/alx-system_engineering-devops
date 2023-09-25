#!/usr/bin/python3
"""
returns info about employees TODO list progress using
RESTAPI
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    user = requests.get(url + "{}".format(argv[1])).json()
    todos = requests.get(url + "{}/todos".format(argv[1])).json()
    tasks = [todo.get('title') for todo in todos
             if todo.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(tasks), len(todos)))

    for task in tasks:
        print("\t {}".format(task))
