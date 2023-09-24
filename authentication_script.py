import requests

url = "http://localhost:8000/auth/"
credentials = {
    "username" : "username"
    ,"password" : "password"}

response = requests.post(url, data=credentials)

# Print the response content
print(response.text)