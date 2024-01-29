#!/usr/bin/python3
""" gather data from API """
import sys
import requests

def main():
    """ main function """
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/'
    users = f'users?id={id}'
    todos = f'todos?userId={id}'
    done =  f'todos?userId={id}&completed=true'
    not_done = f'todos?userId={id}&completed=false'
    user_data = requests.get(url + users).json()
    name = user_data[0].get('name')
    todos_data = requests.get(url + todos).json()
    done_data = requests.get(url + done).json()
    done_ = len(done_data)
    total_done = len(todos_data)
    print(f'Employee {name} is done with tasks({done_}/{total_done}):')
    for task in done_data:
        print(f'\t {task.get("title")}')


if __name__ == "__main__":
    main()
