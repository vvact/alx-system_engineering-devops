#!/usr/bin/python3
"""
returns info about employees TODO list progress using
RESTAPI
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        userid = sys.argv[1]

        api_url = 'https://jsonplaceholder.typicode.com/'
        user_url = api_url + 'users/{}'.format(userid)
        user_todos_url = api_url + 'users/{}/todos'.format(userid)

        # Requesrs te data
        user = requests.get(user_url).json()
        todos = requests.get(user_todos_url).json()

        titles = [todo.get('title') for todo in todos if todo.get('completed')]

        print("Employee {} is done with tasks({}/{}):".format(
            user.get('name'), len(titles), len(todos)))
        print('\n'.join(['\t {}'.format(title) for title in titles]))
