#!/usr/bin/python3
"""Module to query the Reddit API for a list of hot articles."""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list of titles of all hot posts
       for a given subreddit.
    """
    headers = {
        "User-agent":
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
        Mobile Safari/537.36"
    }
    try:
        if after:
            count = requests.get("https://www.reddit.com/r/{}/hot.json?\
                                 after={}".format(subreddit, after),
                                 headers=headers).json().get("data")
        else:
            count = requests.get("https://www.reddit.com/r/{}/hot.json".format
                                 (subreddit),
                                 headers=headers).json().get("data")
        hot_list += [i.get("data").get("title")
                     for i in count.get("children")]
        if count.get("after"):
            return recurse(subreddit, hot_list, after=count.get("after"))
        return hot_list
    except Exception:
        return None


if __name__ == "__main__":
    recurse(sys.argv[1])
