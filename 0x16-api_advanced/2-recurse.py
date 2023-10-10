#!/usr/bin/python3
"""
returna a list containing the title of all hot articles for a
given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], next_page=None, count=0):
    """
    subreddit = subreddit you want to query
    host_list = a list that will store the titles of hot posts
    next_page = A token used for pagination to retrieve the nxt page of rslts
    Initially when you make the first request to the API
    next_page is set to None because you are fetching the 1st page of results
    count = A counter to keep track of the no. of posts processed
    after and the next_page holds the same value
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if next_page:
        url += '?after={}'.format(next_page)
    headers = {'User-Agent': 'Reggy'}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None

    # python dict from json object
    data = r.json()['data']

    # get lists of pages
    posts = data['children']
    for post in posts:
        count = count + 1
        hot_list.append(post['data']['title'])

    next_page = data['after']
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    else:
        return hot_list
