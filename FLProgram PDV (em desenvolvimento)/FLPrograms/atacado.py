from tkinter import *
from tkinter import ttk,messagebox,filedialog
import time
import keyboard
class aplicativo():
    def __init__(self):
        self.main = Tk()
        self.e_qnt = StringVar()
        self.e_psq = StringVar()    
        self.e_produt = StringVar()
        self.window_on = True
        #self.main.overrideredirect(True)
        self.hotkeys("init")
        self.img_fundo("init")
        self.main.state("zoomed")
        self.main.resizable(1,1)
        self.H = self.main.winfo_screenheight()
        self.W = self.main.winfo_screenwidth()
        #self.main.geometry(str(self.W)+"x"+str(self.H))
        self.main.geometry("800x600")
        self.main.title("FLProrgrams - SUPERMERCADO HELY")
        self.main["bg"] = self.bground
        
        self.main.mainloop()
    
    def imput(self, window):
        #variaveis
        
        if window == "init":
            self.compras = []
            self.fonte_input = "times 12"
            self.e_produt.trace("w",self.produto)
            self.e_qnt.set(1)
            self.main.bind('<FocusIn>', self.scan)
            self.main.bind('<FocusOut>', self.scan_out)
            
            bg = "#ff5"
                
            self.l_produt = Label(self.main, text="PRODUTO", font="arial 9 bold", bg=bg, fg="#000", anchor=W)
            self.l_produt.place(relx=0.499, rely=0.81, relwidth=0.2, relheight=0.03)
            self.l_qnt = Label(self.main, text="QUANTIDADE", font="arial 9 bold", bg=bg, fg="#000", anchor=W)
            self.l_qnt.place(relx=0.648, rely=0.81, relwidth=0.2, relheight=0.03)
            self.l_pesquise = Label(self.main, text="PESQUISAR PRODUTOS GERAIS", font="arial 9 bold", bg=bg, fg="#000", anchor=W)
            self.l_pesquise.place(relx=0.499, rely=0.905, relwidth=0.25, relheight=0.03)
            
            self.produt = Entry(self.main, font=self.fonte_input,textvariable=self.e_produt, justify=RIGHT, bd=2, relief=RIDGE)
            self.produt.place(relx=0.5, rely=0.835, relwidth=0.1, relheight=0.04)
            self.qtn_prodt = Entry(self.main, font=self.fonte_input, textvariable=self.e_qnt, justify=RIGHT, bd=2, relief=RIDGE)
            self.qtn_prodt.place(relx=0.65, rely=0.835, relwidth=0.1, relheight=0.04)
            self.e_pesquise = Entry(self.main, font="arial 12 bold", textvariable=self.e_psq, justify=LEFT, bd=2, relief=RIDGE)
            self.e_pesquise.place(relx=0.5, rely=0.93, relwidth=0.25 ,relheight=0.04)
            self.produt.focus()
            if len(self.compras) == 0:
                self.lbl_aguard = Label(self.main, text="AGUARDANDO COMPRAS ...", anchor=W, bg=self.bground, font="arial 18 bold")
                self.lbl_aguard.place(relx=0.46, rely=0.3, relwidth=1, relheight=0.1)
                         
        self.last_event = StringVar()
    def scan_out(self,event):
        if str(event.widget) == ".":
            self.window_on = False
    def scan(self, event):
        print(str(event.widget))
        scan =  (str(event.widget)).replace(".!","")
        self.last_event = scan
        if str(event.widget) == ".":
            self.window_on = True
                
    def img_fundo(self, window):
        if window == "init":
            bg = "#ff5"
            self.bground = "#ff1510"
            #titulo
            self.base = Label(self.main, text="SUPERMERCADO HELY",bg= self.bground, fg="white", font="perpetua 50 bold")
            self.base.place(relx=0, rely=0.02, relwidth=1, relheight=0.1)
            #linha
            self.lin = Label(self.main, text="", bg="white", font="arial 2")
            self.lin.place(relx=0, rely=0.102, relwidth=1, relheight=0.01)
            #barra lateral
            self.lsl_itm = Label(self.main, text="", bg=bg, bd=2, relief=RIDGE)
            self.lsl_itm.place(relx=0, rely=0.15, relwidth=0.4, relheight=1)
            # barra horizontal inferior
            self.itm = Label(self.main, text="", bg=bg, bd=2, relief=RIDGE)
            self.itm.place(relx=0.4, rely=0.78, relwidth=1, relheight=1)

            self.imput("init")
            

        elif window == "venda":
            self.base["fg"] = "#ff7755"
            self.lsl_itm.destroy()
            self.itm.destroy()
            self.l_produt.destroy()
            self.l_qnt.destroy()
            self.l_pesquise.destroy()
            self.produt.destroy()
            self.qtn_prodt.destroy()
            self.e_pesquise.destroy()
            self.lbl_aguard.destroy()
            

    def hotkeys(self, window):
        self.s_enter = keyboard.add_hotkey("shift+enter", lambda:keyboard.press("shift+tab"))
        if window == "init":
            esc = keyboard.add_hotkey("esc", lambda:self.img_fundo("init"))
            #n pesquisar produtos por nome generico, abrir janela com as opcoes de produtos
            #* mudar de produto para qnts de produto
            self.ast =  keyboard.add_hotkey("*", lambda:self.qnt())
            self.enter = keyboard.add_hotkey("enter", lambda:self.f_enter())
            self.v = keyboard.add_hotkey("v", lambda:self.img_fundo("venda"))
            
            
    def qnt(self):
        s = self.e_produt.get()
        time.sleep(0.01)
        ss = self.e_produt.get()
        if s != ss:
            print(1)
            return
        else:
            if len(ss) > 0:
                self.e_qnt.set(ss)
                self.e_produt.set("")
            else:
                self.e_qnt.set(1)
                self.e_produt.set("")
    
    def conf_venda(self):
        pass
    
    def f_enter(self):
        print(self.last_event[:5])
        if self.window_on:
            if len(self.e_produt.get()) > 0 and len(self.e_qnt.get()) > 0:
                try:
                    self.atual_produto.destroy()
                except:
                    pass    
                produto = int(self.e_produt.get())
                qnt = int(self.e_qnt.get())
                compra = (self.e_produt.get(), self.e_qnt.get())
                self.compras.append(compra)
                self.lbl_aguard.destroy()
                self.atual_produto = Label(self.main, text=f"PRODUTO NAO CADASTRADO \n {produto} X {qnt}  = {produto * qnt}", bg=self.bground, font="times 24 bold", anchor=W)
                self.atual_produto.place(relx=0.46, rely=0.27, relwidth=1, relheight=0.1)
                
            elif self.last_event[:5] == "entry": 
                    keyboard.press("tab")
                
    def produto(self,*args):
        self.max_len = 14
        s = self.e_produt.get()
        if len(s) > 0:
            
            if not s[-1].isdigit():
                self.e_produt.set(s[:-1])
                
            else :
                self.e_produt.set(s[:self.max_len])
                if self.e_qnt.get() == "":
                    self.e_qnt.set(1)
     
    def rsl(self, num, r):
        self.screen_w = self.main.winfo_screenwidth()
        self.screen_h = self.main.winfo_screenheight()
        y = num * self.screen_h / 100 
        x = num * self.screen_w /100
        if r == "h":
            return y
        elif r == "w":
            return x 

start = aplicativo()