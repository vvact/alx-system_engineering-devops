#!/usr/bin/python3
"""
Module that queries the Reddit API and returns the number
of total subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # set custom User-Agent header to avoid 'Too Many request Error'
    # It identifiesthe source of the HTTP request to the Reddit servers

    headers = {'User-Agent': 'Reggy'}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()

        return data['data']['subscribers']
    else:
        return 0
