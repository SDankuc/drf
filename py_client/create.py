import requests

headers = {
    "Authorization":"Bearer86396d4d30ca82619910b2f848b6fb6ee6362df8"
    }

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "this field is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())