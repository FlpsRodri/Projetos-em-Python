from tkinter import messagebox, ttk
import sqlite3

with open(r"c:\FLPrograms\read\config\texts\config.config", "r") as config:
    list_conect = config.read().split("\n")


def online(local):
    try:
        with open(local, "r"):
            return True
    except:
        return False


def other(local):
    bank = sqlite3.connect(local)
    cursor = bank.cursor()
    cursor.execute("SELECT * FROM fechamento")
    return cursor.fetchall()


bank1 = sqlite3.connect(r"C:\FLPrograms\DBSupermercado Hely.sql")
cursor1 = bank1.cursor()

for i in list_conect:
    terminal = list_conect.index(i) + 1
    try:
        if online(i):
            print("teminal " + str(terminal) + " online")
            cursor1.execute("SELECT  FROM fechamento")
            bnk1 = cursor1.fetchall()
            bnk2 = other(i)
			


        else:
            print("teminal " + str(terminal) + " offline")



    except:
        print("FAIL IN CHECK IF DB ONLINE")
confirm = messagebox.showinfo(title='', message="oi")
