#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""


import requests
from sys import argv


if __name__ == "__main__":
    # Create a session to reuse connections for multiple requests
    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    # Send requests to get employee's TODO list and name
    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    # Parse JSON response to get the employee's username
    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = 0

    # Count the number of completed tasks
    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
