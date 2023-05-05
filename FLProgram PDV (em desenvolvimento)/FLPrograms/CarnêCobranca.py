from tkinter import *
import sqlite3
import keyboard

class app():
    def __init__(self):
        self.window()
    
    def window(self):
        self.root = Tk()
        self.root.wm_attributes('-toolwindow',0)
        self.root.title("Carnê de Cobrança")
        self.root.geometry("600x500")
        self.root.resizable(0,0)
        self.root_frameTop = LabelFrame(self.root,text="Dados", bg="#fff")
        self.root_frameTop.place(x=0, y=0, relheight=0.5, relwidth=1)
        self.root_frameBoot = LabelFrame(self.root, bg="#f00")
        self.root_frameBoot.place(rely=0.5,relheight=1, relwidth=1)
        self.topFrame()
        self.bootFrame()
        self.root.mainloop()
    
    def topFrame(self):
        Label(self.root_frameTop, text="Cod", bg="#fff", width=5).place(x=10, y=10)
        Label(self.root_frameTop, text="Cliente", bg="#fff", width=5).place(x=60, y=10)
        
        
        
        
    def bootFrame(self):
        
        pass

if __name__ == '__main__':
    
    run = app()
