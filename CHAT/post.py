import requests

url = 'http://localhost:5000/add_message'
data = {
    "content": "Olá, esta é uma mensagem de teste.",
    "token": "123456789",
    "user": "Felipe",
    "cpf": "000.000.000-00",
    "recipient": "Felipe"
}

response = requests.post(url, json=data)
print(response.json())
