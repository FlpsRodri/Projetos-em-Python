import pyautogui as pt
import pyperclip
import time
import pandas as pd
import twilio
import openpyxl
from twilio.rest import Client

#programa para analizar 6 arquivos excel e caso um dos funcionarios cumprir a meta de 50.000 vendas 
#enviar um sms informando que ele ganhou uma bonificação

#1 abrir os arquivos em excel
#enviar os arquivos excel para a mesma pasta do arquivo python

lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['vendas'] > 55000,'Vendedor'].values[0]
        venddas = tabela_vendas.loc[tabela_vendas['vendas'] > 55000,'Vendas'].values[0]
        print (f'no mes {mes} encontrou alguem com mais de 55000')
        
# para criar uma conta no twilio acesse https://www.twilio.com/docs/libraries/python 
#your acount SID from twilio.com/console
account_sid = ""
#your auth token from twilio.com/console
auth_token = "your_auth_token"

client = Cliente(account_sid, auth_token)

message = client.messages.creat(
    to = "+55979999999"
    from_="+15017250604"
    body="Hello from python!")

print(message.sid)


#2 para cada arquivo:
# verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

#3 se for maior que 55.000 -> envia um sms com o nome , o mes, e as vendas do vendedor
