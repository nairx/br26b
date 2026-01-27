import requests
url = "https://jsonplaceholder.typicode.com/users"
res = requests.get(url).json()
for user in res:
    print(user["name"])
