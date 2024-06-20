import xmltodict
import os
from tkinter import *
import sqlite3
from tkinter import ttk,messagebox
from datetime import datetime
import pyperclip
import keyboard

class Db(object):
    def __init__(self):
        pass
    
    def checkDb(self,db):
        try:
            with open(db,'r'):
                return True
        except Exception : return False

    def start(self,db,tabela):
        if self.checkDb(db):
            self.db=db
            self.tabela = tabela
            self.connect_db(db)
        else: return False
        
    def connect_db(self):
        try:
            self.bank = sqlite3.connect(self.db)
            self.cursor = self.bank.cursor()
        except Exception as ERROR: 
            return ERROR
        
    def createBank(self, bank_name, table,columns):
        try:
            self.bank = sqlite3.connect(bank_name)
            self.cursor = self.bank.cursor()
            columnsName = columns
            temp =""
            for i in columns:
                temp += i +" text,"
            columns = temp[:-1]
            temp=""
            columns ="id integer primary key autoincrement, " + columns
            self.cursor.execute(f"create table if not exists {table} ({columns}) ")
            self.bank.commit()
            for index,i in enumerate(columnsName):
                if (index+1) != len(columnsName):
                    temp += i + ", "
                else:
                    temp += i 
            columnsName = temp
            if len(self.consultDB(self.table)) == 0:
                values = ("Null, " * len(columnsName.split(",")))[:-2]
                self.cursor.execute(f"INSERT INTO {table} ({columnsName}) VALUES ({values})")
                self.bank.commit()
            self.closeDB()
                
        except Exception as ERROR: return ERROR    

    def consultDB(self):
        try:
            self.cursor.execute(f"SELECT * FROM {self.table}")
            return self.cursor.fetchall()
        except Exception as ERROR: return ERROR
        
    def Insert(self,columns,values):
        try:
            _list = []
            for index,column in enumerate(columns):
                if len(columns) != (index + 1):
                    _list.append( column + ",")
                else:
                    _list.append( column)
            columns = ""
            for i in _list: columns+=i
            print(columns)
            self.cursor.execute(f"INSERT INTO {self.table} ({columns}) VALUES ({values})")
            self.bank.commit()
        except Exception as ERROR: return ERROR
                
    def Update(self,columns, values, whereID):
        try:
            _list = []
            for index,column in enumerate(columns):
                if len(columns) != (index + 1):
                    _list.append( column + "=" + (f"'{values[index]}'") + ",")
                else:
                    _list.append( column + "=" + (f"'{values[index]}'"))
            columns = ""
            for i in _list: 
                columns +=i
            
            self.cursor.execute(f"UPDATE {self.table} SET {columns} WHERE id = {whereID}")
            self.bank.commit()
        except Exception as ERROR: return ERROR
            
    def Delete(self,where):
        if not "=" in str(where): return False  
        self.cursor.execute(f"DELETE FROM {self.table} WHERE {where}")
        self.bank.commit()
    
    def closeDB(self):
        self.bank.close()
