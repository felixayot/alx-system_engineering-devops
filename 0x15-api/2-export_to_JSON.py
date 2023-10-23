#!/usr/bin/python3
"""Exports given employee IDs' TODO list progress in JSON format
   using this REST API https://jsonplaceholder.typicode.com/
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    employee = requests.get(url + "users/{}".format(userId)).json()
    username = employee.get("username")
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.json".format(userId), "w") as jsonfile:
        json.dump({userId: [{"task": t.get("title"), "completed":
                             t.get("completed"), "username": username}
                            for t in todos]}, jsonfile)
