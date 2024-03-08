#!/usr/bin/python3
"""
Queries the API, parses the title of all hot articles, and prints
a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, count_list=[], next_page=None):
    """
    subreddit - subreddit you want to query
    word_list - A list of keywords to count
    count_list - List to store counts of each keyword
    next_page - keeps track of the pagination tkn for the next
    page of results
    """

    if not count_list:  # initializes count_list to empty
        for word in word_list:
            count_list.append(dict({'keyword': word,
                                   'count': 0}))

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if next_page:
        url += '?after={}'.format(next_page)

    headers = {'User-Agent': 'Reggy'}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return

    data = r.json()['data']

    posts = data['children']
    for post in posts:
        title = post['data']['title']
        for item in count_list:
            title_lower = title.lower()
            title_list = title_lower.split()
            item['count'] += title_list.count(item['keyword'].lower())

    next_page = data['after']
    if next_page is not None:
        return count_words(subreddit, word_list, count_list, next_page)
    else:
        # sort the list by count
        sorted_list = sorted(count_list,
                             key=lambda word: (word['count'], word['keyword']),
                             reverse=True)

    keywords_matched = 0
    for word in sorted_list:
        if word['count'] > 0:
            print('{}: {}'.format(word['keyword'], word['count']))
            keywords_matched += 1
    return
