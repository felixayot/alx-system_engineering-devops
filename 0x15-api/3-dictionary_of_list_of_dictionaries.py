#!/usr/bin/python3
"""Exports all employees' TODO lists in JSON format
   using this REST API https://jsonplaceholder.typicode.com/
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({e.get("id"):
                   [{"task":
                     t.get("title"),
                     "completed": t.get("completed"),
                     "username": e.get("username")
                     }
                    for t in requests.get(url + "todos",
                                          params={"userId":
                                                  e.get("id")}).json()]
                  for e in employees}, jsonfile)
