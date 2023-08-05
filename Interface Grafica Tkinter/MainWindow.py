from tkinter import *
import keyboard
#menu bar
class app(object):
    def __init__(self,config):
        self.master = Tk()
        self.title,self.geometry,resizable,self.bg,self.fg = config["title"],config["geometry"],config["resizable"],config["bg"],config["fg"]
        self.master.title(self.title)
        self.master.geometry(self.geometry)
        if resizable==False:self.master.resizable(0,0)
        else: self.master.resizable(1,1)
        self.master["bg"]=self.bg
        self.fontTitle = "times 17 bold"
        self.fonte = "consolas 12"
        self.buttons()
        self.prodWindow()
        self.menuBar()
        
        self.master.mainloop()

    def prodWindow(self):
        self.prodFrame = LabelFrame(self.master,text="Indentificação do Produto",font="consolas 12 bold",width=795,height=150,bg=self.bg)
        self.prodFrame.place(relx=0,rely=0)
        labelsProd = {"Codigo(EAN)":(0.01,0),"Produto":(0.155,0.), "Fornecedor":(0,0.5), "Ultima Auteração":(0.4,0.5),"NCM":(0.7,0.5),"N° NF-e":(0.85,0.5)}
        self.labels(self.prodFrame,labelsProd)

        self.prodFrameCalc = LabelFrame(self.master,text="Preço do Produto",font="consolas 12 bold",width=795,height=300,bg=self.bg)
        self.prodFrameCalc.place(relx=0,rely=0.25)
        labelsProdCalc = { "quantidade":(0,0), "CD":(0,0), "vtotal":(0,0), "vunitario":(0,0),"v venda":(0,0), "porcentagem d lucro":(0,0) }
        self.labels(self.prodFrameCalc,labelsProdCalc)
        

    def buttons(self):
        # lista 
        pass
    def labels(self,master,dicLabel,bg=None):
        if bg == None: bg=self.bg
        for label in dicLabel:
            Label(master,text=label,bg=bg,fg=self.fg,font=self.fonte).place(relx=dicLabel[label][0],rely=dicLabel[label][1])

        

    def menuBar(self): pass
    
    

if __name__=="__main__":
    config={"title":"Main Window","geometry":"800x600","resizable":False,"bg":"#6495ed","fg":"#000"}
    start = app(config)
