import requests

otsing = input("Sisesta märksõna: ")
url = "https://dummy-json.mock.beeceptor.com/comments"

response = requests.get(url)

if response.status_code == 200:
    datas = response.json()
    for data in datas:
        if otsing in data['body'] or data['name']:
            print(f"Postituse ID: {data['postId']}")
            print(f"Id: {data['id']}")
            print(f"Name: {data['name']}")
            print(f"Email: {data['email']}")
            print(f"Comment body: {data['body']}")
            break  
else:
    print(f"Error: {response.status_code}")
