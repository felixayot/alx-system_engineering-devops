#!/usr/bin/python3
"""Module to query the Reddit API for a list of hot articles."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursively returns a list of titles of all hot posts
       for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-agent":
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
        Mobile Safari/537.36"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if resp.status_code == 404:
        return None

    results = resp.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for i in results.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
