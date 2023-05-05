import tkinter
from tkinter import *
import sqlite3
import os
import keyboard
import time
class App():
    def __init__(self):
        self.tela_inicio()
    
    def tela_inicio(self):
        self.color_base = "#2EB9D9"
        self.empresa()
        self.root = Tk()
        self.root.title("FLPrograms 2022.2 - " +self.nome_fantasia_empresa.upper())
        self.root.geometry("800x600")
        self.root.resizable(0,0)
        self.root.bind('<FocusIn>', self.scan)
        self.root.bind('<FocusOut>', self.scan_out)
        self.root.state("zoomed")
        self.root["bg"] = self.color_base
        self.window = "init"
        self.window_state = True
        self.last_focus = ""
        self.tela_main()
        self.hotkeys()
        
        self.root.mainloop()
    
    def empresa(self):
        self.nome_fantasia_empresa = "SUPERMERCADO HELY"
        self.razao_social = ""
        self.cnpj_empresa = ""
        self.endereco_empresa = ""
        self.telefone_empresa = ""
        self.email_empresa = ""
        self.bground = "#ff1510"
        self.bg = "#ff5"
        
    def hotkeys(self):
        def f_enter():
            if self.window_state:
                
                if self.window == "init":
                    if self.last_focus[:6] == "button": 
                        keyboard.press("space")
                    elif self.last_focus[:5] == "entry": keyboard.press("tab")
                elif self.window == "venda":
                    self.last_focus = self.last_focus.replace("frame2frame2","")
                    if self.last_focus[:6] == "button": 
                        keyboard.press("space")
                    elif self.last_focus[:5] == "entry":
                        if len(self.variable_prod.get()) > 0:
                            if not len(self.variable_qnt.get()) > 0: self.variable_qnt.set(1)
                            value = float(self.variable_prod.get()) * float(self.variable_qnt.get())
                            self.lbl_total["text"] = self.formatar(value)
                        else:
                            if not len(self.variable_qnt.get()) > 0: self.variable_qnt.set(1)
                            keyboard.press("tab")
            else:
                pass
        def f_q():
            if self.window_state == True:
                if self.window == "venda":
                    #try:
                      self.main.destroy()
                #except:pass
        def f_v():
            if self.window_state == True:
                if self.window == "venda":
                    self.confirm_venda()    
                    pass
        def f_sEnter():
            if self.window_state == True:
                time.sleep(0.002)
                keyboard.press("shift+tab")
        def f_f2():
            if self.window_state == True and self.window == "init":
                self.venda_window()
        enter = keyboard.add_hotkey("enter", lambda:f_enter())
        v = keyboard.add_hotkey("v", f_v)
        q = keyboard.add_hotkey("q", f_q)
        f2 = keyboard.add_hotkey("f2", f_f2)
        #s_enter = keyboard.add_hotkey("shift+enter", f_sEnter)   
    def scan(self,event):
        if str(event.widget) == ".":self.window_state = True
        else: 
            self.last_focus = (str(event.widget)).replace(".!", "")
    def scan_out(self,event):
        if str(event.widget) == ".":self.window_state = False
        
    def tela_main(self):
        FONTE = "arial 9"
        self.btn_vender = Button(self.root, width=10, height=4, text="VENDA", justify=CENTER, anchor=S, font=FONTE, command=self.venda_window)
        btn_fechamento = Button(self.root, width=10, height=4, text="FECHAMENTO", justify=CENTER, anchor=S, font=FONTE)
        btn_clientes = Button(self.root, width=10, height=4, text="CLIENTES", justify=CENTER, anchor=S, font=FONTE)
        btn_backup = Button(self.root, width=10, height=4, text="BACKUP", justify=CENTER, anchor=S, font=FONTE)
        btn_cadastrar = Button(self.root, width=10, height=4, text="PRODUTOS", justify=CENTER, anchor=S, font=FONTE)
        btn_config = Button(self.root, width=10, height=4, text="CONFIGURAÇÕES", justify=CENTER, anchor=S, font=FONTE)
        btn_movimento = Button(self.root, width=10, height=4, text="MOVIMENTO", justify=CENTER, anchor=S, font=FONTE)
        btn_relatorio = Button(self.root, width=10, height=4, text="RELATORIO", justify=CENTER, anchor=S, font=FONTE)
        btn_administrativo = Button(self.root, width=10, height=4, text="ADMINISTRATIVO", justify=CENTER, anchor=S, font=FONTE)
        btn_fechar = Button(self.root, width=10, height=4, text="FECHAR", justify=CENTER, anchor=S, font=FONTE, command=lambda:self.root.destroy())
        lbl = Label(self.root, height=4, text="", font="arial 10")
        
        self.btn_vender.pack(anchor=N, side=LEFT)
        btn_fechamento.pack(anchor=N, side=LEFT)
        btn_clientes.pack(anchor=N, side=LEFT)
        btn_backup.pack(anchor=N, side=LEFT)
        btn_cadastrar.pack(anchor=N, side=LEFT)
        btn_config.pack(anchor=N, side=LEFT)
        btn_movimento.pack(anchor=N, side=LEFT)
        btn_relatorio.pack(anchor=N, side=LEFT)
        btn_administrativo.pack(anchor=N, side=LEFT)
        btn_fechar.pack(anchor=N, side=LEFT)
        lbl.pack(fill=X)
    
    def formatar(self,valor):
        var = ""
        if valor < 1000 :
            return "R$ "+str(format(valor,".2f").replace(".", ","))
        else:
            for i in str(format(valor,".2f").replace(".",","))[::-1]:
                if len(var) == 6: var += ("." + i)
                elif len(var) == 10: var += ("."+i)
                elif len(var) == 14: var += ("."+i)
                elif len(var) == 18: var += ("."+i)
                else: var += i
            return "R$ " + var[::-1]
    
    def venda_window(self):
        self.window = "venda"
        try:
            self.root.destroy()
            self.main.destroy()
        except:pass
        self.main = Tk()
        self.main.geometry("800x600")
        #self.main.overrideredirect(True)
        self.main.state("zoomed")
        self.main.resizable(0,0)
        self.main.bind("<FocusIn>", self.scan)
        self.main.bind("<FocusOut>", self.scan_out)
        #self.main.wm_focusmodel(ACTIVE)
        self.main["bg"] = self.bground
        #titulo
        base = Label(self.main, text=self.nome_fantasia_empresa.upper(),bg=self.bground, fg="white", font="perpetua 50 bold")
        base.place(relx=0, rely=0.02, relwidth=1, relheight=0.1)
        #linha
        lin = Label(self.main, text="", bg="white", font="arial 2")
        lin.place(relx=0, rely=0.102, relwidth=1, relheight=0.01)
        #barra lateral
        frame_itm = Frame(self.main, bg=self.bg, bd=2, relief=RIDGE)
        frame_itm.place(relx=0, rely=0.15, relwidth=0.4, relheight=1)
        # barra horizontal inferior
        
        #l = Label(frame_itm, text=text, font="times 13 bold",anchor=NW,bg="#F0ECB7", justify=CENTER, height=20, width=55)
        #l.grid(column=0, row=0)
        frame_prod = Frame(self.main, bg=self.bg, bd=2, relief=RIDGE)
        frame_prod.place(relx=0.4, rely=0.78, relwidth=1, relheight=1)
        frame_total = Frame(frame_prod, bg=self.bg, height=75)
        frame_total.pack(fill=X)
        frame_input = Frame(frame_prod,bg=self.bg, height=900)
        frame_input.pack(fill=X)
        
        self.valor_total = self.formatar(0)
        
        self.lbl_total = Label(frame_total, text=self.valor_total ,justify=RIGHT, anchor=E , bg="#eee",bd=2, relief=RIDGE, font="times 40 bold", width=20)
        self.lbl_total.place(relx=0.0001, rely=0, relwidth=0.6, relheight=1)
        numericos = "1234567890,"
        def prod(*args):
            if not len(self.variable_qnt.get()) > 0: self.variable_qnt.set(1)
            dg =self.variable_prod.get()
            if len(dg) > 0:
                if not dg[-1] in numericos:
                    self.variable_prod.set(dg[:-1])
                elif dg.count(",") > 1:
                    self.variable_prod.set(dg[:-1])
        def qnt(*args):
            dg = self.variable_qnt.get()
            if len(dg) > 0 : 
                if not dg[-1] in numericos:
                    self.variable_qnt.set(dg[:-1])
                elif dg.count(",") > 1:
                    self.variable_qnt.set(dg[:-1])
        
        self.variable_prod = StringVar(master=frame_input)
        self.variable_qnt = StringVar(master=frame_input)
        self.variable_prod.trace("w",prod)
        self.variable_qnt.trace("w", qnt)
        self.variable_qnt.set(1)
        Label(frame_input, text="", bg=self.bg, height=1, width=10).grid(column=0, row=0)
        lbl_prod = Label(frame_input, text="PRODUTO",width=15, font="arial 8 bold",bd=2, relief=SOLID, justify=LEFT)
        lbl_prod.grid(column=1, row=1)
        en_prod = Entry(frame_input,textvariable=self.variable_prod,width=15, font="arial 10 bold", bd=2, relief=SOLID)
        en_prod.grid(column=1, row=2)
        lbl = Label(frame_input, text="", bg=self.bg, width=6)
        lbl.grid(column=3, row=0)
        lbl_qnt = Label(frame_input,width=15, text="QUANTIDADE", font="arial 8 bold", bd=2, relief=SOLID, justify=LEFT)
        lbl_qnt.grid(column=4, row=1)
        en_qnt = Entry(frame_input,width=15, font="arial 10 bold", bd=2, relief=SOLID, textvariable=self.variable_qnt)
        en_qnt.grid(column=4, row=2)
        
        self.main.mainloop()
        pass
    
    def confirm_venda(self):
        try: self.main.destroy()
        except:pass
        pass
App()