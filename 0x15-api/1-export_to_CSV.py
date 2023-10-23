#!/usr/bin/python3
"""Exports given employee IDs' TODO list progress in CSV format
   using this REST API https://jsonplaceholder.typicode.com/
"""
import requests
import sys
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    employee = requests.get(url + "users/{}".format(userId)).json()
    username = employee.get("username")
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.csv".format(userId), "w", newline="") as csvfile:
        written = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [written.writerow([userId, username, t.get("completed"),
                           t.get("title")]) for t in todos]
