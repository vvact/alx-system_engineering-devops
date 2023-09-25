#!/usr/bin/python3
"""
Exports a user TODO ;ist as a CSV  file
"""
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

        csv_data = ['"{}","{}","{}","{}"'.format(
            user_id,
            user.get('username'),
            todo.get('completed'),
            todo.get('title')) for todo in todos]

        with open('{}.csv'.format(user_id), 'w') as csvf:
            csvf.write('\n'.join(csv_data))
