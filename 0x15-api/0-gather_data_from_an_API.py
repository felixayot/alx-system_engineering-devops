#!/usr/bin/python3
"""Returns information about given employee IDs' TODO list progress
   using this REST API https://jsonplaceholder.typicode.com/
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    done_tasks = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(employee.get("name"),
                                                          len(done_tasks),
                                                          len(todos)))
    [print("\t {}".format(d)) for d in done_tasks]
