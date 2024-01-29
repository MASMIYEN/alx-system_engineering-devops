#!/usr/bin/python3
""" gather data from API """
import requests
import sys


def main():
    """ main function """
    id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/'
    users = f'users?id={id}'
    todos = f'todos?userId={id}'
    done = f'todos?userId={id}&completed=true'
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

"""

Employee *NAME* is done with tasks(*DONE*/*TOTAL*):
     *TITLE*
     *TITLE*
     *TITLE*


https://jsonplaceholder.typicode.com/users?id=1
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
https://jsonplaceholder.typicode.com/todos?userId=5
[
  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  },
  ]

https://jsonplaceholder.typicode.com/todos?userId=5&completed=true
https://jsonplaceholder.typicode.com/todos?userId=5&completed=false
  """
