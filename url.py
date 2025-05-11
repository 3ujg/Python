import requests

otsing = input("Sisesta märksõna: ")
url = "https://dummyjson.com/users"

response = requests.get(url)

if response.status_code == 200:
<<<<<<< HEAD
    datas = response.json()
    for data in datas:
        if otsing in  data['username']:
            print(f"Id: {data['id']}")
            print(f"Name: {data['firstName'and'lastName']}")
            print(f"Email: {data['email']}")
            print(f"Comment body: {data['body']}")
            break  
=======
    users = response.json()
    for user in users['users']:
        if otsing in user['username']:
            print(f"Id: {user['id']}")
            print(f"Name: {user['firstName']} {['lastName']}")
            print(f"Username: {user['username']}")
            break 
        else:
            print("Midagi läks valesti proovi uuesti") 
>>>>>>> 0f64c66533e6c56bf8a0ac1836db7eb554a1521d
else:
    print(f"Error: {response.status_code}")
