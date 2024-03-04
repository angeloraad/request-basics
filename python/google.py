import requests

session = requests.Session()

response = session.get("https://www.google.com/")

header = response.headers

file = "google-data.txt"

with open(file,"a") as file_object:
    file_object.write(str(header) + " \n" )




# cookies = response.headers.get('Set-Cookie')
# print(cookies)

