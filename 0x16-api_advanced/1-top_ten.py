#!/usr/bin/python3
"""
this doc for module
"""
import requests

# headers = {"User-Agent": "MyCustomUserAgent/1.0"}
headers = {
    "User-Agent": "lMyCustomUserAgent/1.0"
}
params = {
    "limit": 10
}


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
