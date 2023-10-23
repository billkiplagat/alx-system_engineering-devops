#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the CSV format.
"""

import csv
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

    totalTasks = 0

    # Count the number of completed tasks
    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    fileCSV = emp_id + '.csv'
    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([emp_id, usr, i.get('completed'), i.get('title')])
