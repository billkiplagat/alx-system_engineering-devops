#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""


import json
import requests
from sys import argv

if __name__ == '__main__':
    # Create a session to reuse connections for multiple requests
    sessionReq = requests.Session()
    emp_id = argv[1]
    idURL = ('https://jsonplaceholder.typicode.com/users/{}/todos'
             .format(emp_id))
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)

    # Send requests to get employee's TODO list and name
    employee = sessionReq.get(idURL)
    employee_name = sessionReq.get(nameURL)

    # Parse JSON response to get the employee's username
    json_req = employee.json()
    usr = employee_name.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    updateUser[emp_id] = totalTasks

    file_Json = emp_id + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
