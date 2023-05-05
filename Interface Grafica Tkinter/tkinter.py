from tkinter import *

class application:
    def __init__(self,master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1,text="Primeiro Widget")
        self.msg.pack()
        self.msg["font"] = ("verdana","10","italic","bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique Aqui"
        self.sair["font"] = ("Calibri","10")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>",self.mudarTexto)
        self.sair["command"] = self.widget1.quit
        self.sair.pack(side=RIGHT)
        
        
    def mudarTexto(self,event):
        if self.msg["text"] == "Primeiro Widget":
            self.msg["text"] = "O botao recebeu um clique"
        else:
            self.msg["text"] = "Primeiro Widget"
root = Tk()
application(root)
root.mainloop()






#def comando():
#        print("felipe")
#    janela = Tk()
#    janela.title("FComerce")
#    botao = Button(janela, text="Buscar", command=comando)
#    janela.grid(column=0,row=1)
