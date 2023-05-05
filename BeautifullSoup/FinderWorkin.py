import requests
from bs4 import BeautifulSoup
user_agente = {'User-Agente':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
url = "https://wise.com/gb/currency-converter/brl-to-usd-rate?amount=10"
c = requests.get(url, headers=user_agente )
print(c.status_code)
print(c.headers)
#html = convert.text
#soup = BeautifulSoup(html,'html.parser')


#print(soup.get_text())
    

#for valor in value:
#    valor_convert = valor.find('input').get('value')
#    print(valor_convert)