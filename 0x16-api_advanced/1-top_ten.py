#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the
first 1O hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Top 10 hot posts in using Reddit API"""
    res = requests.request(
        'GET',
        'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit),
        headers={
            'User-Agent': 'Reggy'
        },
        allow_redirects=False
    )

    if res.status_code == 200:
        try:
            posts = res.json().get('data').get('children')

            [print(post.get('data').get('title')) for post in posts]
        except Exception:
            pass
    else:
        print(None)
