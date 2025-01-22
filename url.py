import requests


url = "https://dummyjson.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    users = data("users")

user_id = int(input("Sisesta inimese id: "))

for user in users:
    if user('id') == user_id:
        print(f"User id: {user_id}")
