#!/usr/bin/python3
"""
Converts a user TODO list as to json data
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]

        api_url = 'https://jsonplaceholder.typicode.com/'
        user_url = api_url + 'users/{}'.format(user_id)
        user_todos_url = api_url + 'users/{}/todos'.format(user_id)

        # Requesrs te data
        user = requests.get(user_url).json()
        todos = requests.get(user_todos_url).json()

        json_data = [
                {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user.get('username')
                }
                for todo in todos]

        with open('{}.json'.format(user_id), 'w') as jsonf:
            json.dump({user_id: json_data}, jsonf)
