import pandas as pd 
import openpyxl
import pyautogui as pt
import twilio
from twilio.rest import Client


tabela = pd.read_excel("vendas.xlsx")
tabela = tabela.drop("0", axis=0)
print(tabela)
