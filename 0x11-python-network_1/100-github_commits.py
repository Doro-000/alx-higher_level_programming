#!/usr/bin/python3
"""takes a repository name and an owner name and
lists 10 commits (from the most recent to oldest)"""
from sys import argv
from requests import get

if __name__ == "__main__":
    url = "https://api.github.com/repos"
    owner = argv[2]
    repo = argv[1]
    url = url + "/" + owner + "/" + repo + "/" + "commits"
    limit = {"per_page": 10}
    response = get(url, params=limit)
    for commmit in response.json():
        sha = commmit.get("sha")
<<<<<<< HEAD
        author = commmit.get("author").get("login")
        get_name = get("https://api.github.com/users/{}".format(author)).json()
        name = get_name.get("name")
        print("{}: {}".format(sha, name))
=======
        author = commmit.get("author").get("name")
        print("{}: {}".format(sha, author))
>>>>>>> 03b93f0109da4125464a91ff661b5e80223e958e
