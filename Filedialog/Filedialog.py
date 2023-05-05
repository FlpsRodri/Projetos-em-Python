import tkinter
from tkinter import CENTER, Button, messagebox, filedialog
import sqlite3

a = tkinter.Tk()
def searchdb():
    b = filedialog.askopenfilename 
    print(b)
Bb = Button(a, text="Buscar banco de dados", bg="#fff", font="times 13", command= searchdb)
Bb.pack(anchor=CENTER)
a.mainloop()
