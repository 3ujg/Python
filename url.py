import requests

otsing = input("Sisesta märksõna: ")
url = "https://dummyjson.com/users"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    for user in users['users']:
        if otsing in user['username']:
            print(f"Id: {user['id']}")
            print(f"Name: {user['firstName']} {['lastName']}")
            print(f"Username: {user['username']}")
            break 
        else:
            print("Midagi läks valesti proovi uuesti") 
else:
    print(f"Error: {response.status_code}")
