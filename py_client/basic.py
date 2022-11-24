import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# API (Aplication programming interface)-> Method
get_response = requests.post(endpoint, json = {"title":"123", "content": "Hello World"}) #HTTP Request
#print(get_response.headers)
#print(get_response.text) # print raw text response
# print(get_response.status_code)

#HTTP Request -> HTML
# REST API HTTP Request -> JSON (JavaScript Object Notation)

print(get_response.json())
# print(get_response.status_code)
