import requests

otsing = input("Sisesta märksõna: ")
url = "https://dummyjson.com/users"

response = requests.get(url)

if response.status_code == 200:
    datas = response.json()
    for data in datas:
        if otsing in  data['username']:
            print(f"Id: {data['id']}")
            print(f"Name: {data['firstName'and'lastName']}")
            print(f"Email: {data['email']}")
            print(f"Comment body: {data['body']}")
            break  
else:
    print(f"Error: {response.status_code}")
