#!/usr/bin/python3
"""Module to query the Reddit API for titles of hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed
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
        "limit": 10
    }
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if resp.status_code == 404:
        print("None")
        return
    results = resp.json().get("data")
    [print(i.get("data").get("title")) for i in results.get("children")]
