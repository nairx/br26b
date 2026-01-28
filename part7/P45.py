import requests
from datetime import datetime
url = "https://jsonplaceholder.typicode.com/users"
res = requests.get(url).json()
for user in res:
    print(user["name"],user["email"],user["address"]["city"])

#Read the data from api
#Add the datetime,name,email,address to a text file

