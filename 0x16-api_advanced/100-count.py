#!/usr/bin/python3
"""Module to query the Reddit API for a list of hot articles."""
import requests


def count_words(subreddit, word_list, occurrences={}, after="", count=0):
    """Parses the titles of all hot articles,
       and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 \
        Mobile Safari/537.36"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                num = len([t for t in title if t == word.lower()])
                if occurrences.get(word) is None:
                    occurrences[word] = num
                else:
                    occurrences[word] += num

    if after is None:
        if len(occurrences) == 0:
            return
        occurrences = sorted(occurrences.items(),
                             key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in occurrences]
    else:
        count_words(subreddit, word_list, occurrences, after, count)
