#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the
first 1O hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'Reggy'}

    try:
        res = requests.get(url, headers=headers,
                           allow_redirects=False)
        if res.status_code == 200:
            posts = res.json().get('data').get('children')
            for i in range(10):
                print(posts[i].get('data').get('title'))
        else:
            pass
    except Exception:
        print("None")
