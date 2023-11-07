#!/usr/bin/python3
"""Module to query Reddit API for all subscribers."""
import requests


def number_of_subscribers(subreddit):
    """"Returns the total number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
        Mobile Safari/537.36"
    }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    results = resp.json().get("data")
    return results.get("subscribers")
