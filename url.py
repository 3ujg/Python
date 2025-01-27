import requests

url = "https://dummy-json.mock.beeceptor.com/comments"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    comments = data("comments")

comment_id = int(input("Sisesta inimese id: "))

for comment in comments:
    if comment('id') == comment_id:
        print(f"User id: {comment_id}")
        break
    else:
        print("Something went wrong.")
