from tkinter import *
class aplication:
    def __init__(self,master=None):
        self.fontePadrao = ("Arial","10")
        self.pConteiner = Frame(master)
        self.pConteiner["pady"] = 10
        self.pConteiner.pack()
        
        self.sConteiner = Frame(master)
        self.sConteiner["padx"] = 20
        self.sConteiner.pack()
        
        self.tContainer = Frame(master)
        self.tContainer["padx"] = 20
        self.tContainer.pack()
        
        self.qContainer = Frame(master)
        self.qContainer["pady"] = 20
        self.qContainer.pack()
        
        self.titulo = Label(self.pConteiner,text="Dados do Usuario")
        self.titulo["font"] = ("Arial","10","bold")
        self.titulo.pack()
        
        self.nomeLabel = Label(self.sConteiner,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        
        self.nome = Entry(self.sConteiner)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        
        self.senhaLabel = Label(self.tContainer,text="senha",font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        
        self.senha = Entry(self.tContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "#"
        self.senha.pack(side=LEFT)
        
        self.autenticar = Button(self.qContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
        
        self.mensagem = Label(self.qContainer,text ="", font=self.fontePadrao)
        self.mensagem.pack()
        
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "Felipe" and senha == "bkrodri@1":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Usuario ou Senha errado"
        
        
        




root = Tk()
aplication(root)
root.mainloop()