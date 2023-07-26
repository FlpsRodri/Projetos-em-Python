import os
import sqlite3
from tkinter import *

class chat():
    def __init__(self):
        pass
    
    def startChat(self,master):
        self.root = Toplevel(master)
        self.root.resizable(0,0)
        self.root.geometry("")
        self.root.title("Chat")
        self.root.attributes("-topmost",True)
        self.root.config(bg="#2dcc9f")

class Db(object):
    def __init__(self):
        pass
    
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
                
        except Exception as ERROR: return ERROR    


    def consultDB(self,table):
        try:
            self.cursor.execute(f"SELECT * FROM {table}")
            return self.cursor.fetchall()
        except Exception as ERROR: return ERROR
        
    def Insert(self,table,columns,values):
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
            self.cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({values})")
            self.bank.commit()
        except Exception as ERROR: return ERROR
                
    def Update(self,table,columns, values, whereID):
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
            
            self.cursor.execute(f"UPDATE {table} SET {columns} WHERE id = {whereID}")
            self.bank.commit()
        except Exception as ERROR: return ERROR
            
    def Delete(self,table,where):
        if not "=" in str(where): return False  
        self.cursor.execute(f"DELETE FROM {table} WHERE {where}")
        self.bank.commit()
    
    def closeDB(self):
        self.bank.close()
    
class app(chat,Db):
    def __init__(self):
        self.table="teste"
        self.columns = ["nome", "telefone", "usuario", "senha"]
        self.chat = Tk()
        self.createBank(bank_name="NewDB.sql", table=self.table, columns=self.columns)
        #values = ["Null","Null","Null","Null"]
        #self.Insert("teste",columns=self.columns,values=" 'nome', 'telefone', 'usuario', 'senha'" )
        #print(self.Update(table=self.table,columns=self.columns,values=values,whereID=2))
        #self.Delete("teste","id = 0")
        
        self.startChat(self.chat)
        self.chat.mainloop()
        self.closeDB()
        
if __name__ == "__main__":
    
    app()


