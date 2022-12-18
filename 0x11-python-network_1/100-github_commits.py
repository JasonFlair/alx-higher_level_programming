#!/usr/bin/python3
"""
lists 10 commits (from the most recent to oldest) of the repository
 “rails” by the user “rails” or
 anyone you specify in the terminal args
"""
import requests
import sys

if __name__ == "__main__":
    # set parameters for the url
    base_url = "https://api.github.com/repos"
    OWNER = sys.argv[2]
    REPO = sys.argv[1]
    headers = {"Accept": "application/vnd.github+json"}

    response = requests.get(f"{base_url}/{OWNER}/{REPO}/commits", headers=headers)
    commits_json = response.json()
    # print the SHA and author name for each commit
    print(f"{commits_json['sha']}: {commits_json['name']['author']}")
    """refer to https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28 documentation if you get 
    confused in future lol """