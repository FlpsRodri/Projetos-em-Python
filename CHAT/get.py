import requests

url = 'http://127.0.0.1:5000/get_messages'
params = {
    "token": "123456789",
    "user": "Felipe",
    "cpf": "000.000.000-00",
    "recipient": "Felipe"
}

response = requests.get(url, params=params)
print(response.json())
