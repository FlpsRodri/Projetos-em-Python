from tkinter import *
import sqlite3


class functions(object):
    def __init__(self):
        self.Bank = sqlite3.connect("Deposito.sql")
        self.CursorBank = self.Bank.cursor()
        
    def InsertProdOnBd(self,descricao, valorUnit, valorVenda, DataEmissao, fornecedor, lastUpdate, unCom, amount, ):
        self.CursorBank.execute("INSERT INTO PRODUTOS () VALUES ()")
        self.Bank.commit()