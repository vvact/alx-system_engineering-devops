#!/usr/bin/python3
"""
Exports all todos as json file from
the url endpoints
"""
import json
import requests
import sys

# Endpoint urls
api_url = 'https://jsonplaceholder.typicode.com/'
users_url = api_url + 'users'
todos_url = api_url + 'todos'


if __name__ == "__main__":

    # Requests users data
    users = requests.get(users_url).json()

    with open("todo_all_employees.json", 'w') as jsonf:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(todos_url,
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonf)
