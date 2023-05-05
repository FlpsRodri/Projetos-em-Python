from tkinter import *
from tkinter import ttk
import sqlite3
import keyboard

quit()
#print(ProductSorce.produt("789"))
from datetime import datetime

class app:
    def __init__(self):
        #print(self.data("24112022"))
        
        self.win = Tk()
        self.win.title("Note Comerse")
        self.win.geometry("800x600")
        self.win.resizable(False, False)
        self.win.state("zoomed")
        self.win["background"] = "#bbb"
        self.functions()
        self.win.mainloop()

    def functions(self):
        self.img()
        self.variable()
        self.frames()
        self.menuBar()
        self.database()
        self.keys()
        self.logon()
        #self.ClientesWindow()

    def img(self):
        self.Photoimg = PhotoImage(file="LogoCEscritaP.png", height=600, width=600)

    def onlyNum(self,value, diferent=None):
        numbers = "1234567890"
        if diferent!= None:
            numbers += diferent
        value = str(value)
        val = ""
        for i in value:
            if i in numbers:
                val += i
        return val

    def onlyAlfa(self,value,width=None,simbol=0,diferent=None):
        value = str(value)
        permited =  ("abcdefghijklmnopqrstuvwxyzç ")
        if width != None and len(value) > width: value = value[:width]
        if simbol == 1 or simbol == True:
            permited += '+-=_?;:.,<>[]()*%°ºª!@#$&"/|\²£¢¬§'
        if diferent != None: permited+= diferent
        val = ""
        for i in value:
            if i.lower() in permited:
                val += i
        return val

    def variable(self):
        self.colorBase = "#fc240c"
        self.fontelbl = "arial 12 bold"
        self.bglbl = "#ccc"
        self.window = StringVar()
        self.bgbtn = "#ddd"
        self.heightbtn = 2
        self.bgFrame = "#fff"

    def keys(self):
        def esc_f():
            self.win.destroy()
        def enter_f():
            #keyboard.press("space")
            pass
        esc = keyboard.add_hotkey("esc", esc_f)
        enter = keyboard.add_hotkey("enter", enter_f)
        
    def ajuda(self, window):
        try: self.winA.destroy()
        except: pass
        self.winA = Toplevel()
        self.winA.geometry("300x200")
        self.winA.title(window)
        bg = "#66ffff"
        self.winA.configure(bg=bg)
        self.winA.resizable(False,False)

        if window == "Contato":
            text = "\n\nDesenvolvedor: Felipe Rodrigues \n\nEmail: felipesrodrigs@gmail.com \n\nNum: +5597984165908 \n"
            Label(self.winA, text=text,font=self.fontelbl, fg="black", bg=bg ).pack( expand=True)
        elif window == "Version":
            textV = "\n\nNote Comerce - FLPrograms \nVersion 1.0/1222"
            Label(self.winA, text=textV, font=self.fontelbl, fg="black", bg=bg, justify=CENTER).pack(fill=Y)
        self.winA.transient(self.win)
        self.winA.focus_force()
        self.winA.grab_set()
        self.winA.mainloop()
        self.winA.mainloop()

    def SetUser(self):
        self.logon()
    
    def menuBar(self):
        self.Bmenu = Menu(self.win)
        
        menuAjuda = Menu(self.Bmenu, tearoff=0)
        menuAjuda.add_command(label="Contato Desenvolvedor", command=lambda:self.ajuda("Contato"))
        menuAjuda.add_command(label="Informação de software", command=lambda: self.ajuda("Version"))
        menuAjuda.add_separator()
        menuAjuda.add_command(label="Sair", command=self.win.destroy)

        menuConfig = Menu(self.Bmenu, tearoff=0)
        menuConfig.add_command(label="Configurações")
        
        menuTrabalho = Menu(self.Bmenu,tearoff=0)
        menuTrabalho.add_command(label="Emitir Nota de Autorização")
        menuTrabalho.add_command(label="Confirir Validade de Nota")
        menuTrabalho.add_separator()
        menuTrabalho.add_command(label="Trocar Usuario", command=self.SetUser)
        
        self.Bmenu.add_cascade(label="Trabalho", menu=menuTrabalho)
        self.Bmenu.add_cascade(label="Configurações" ,menu=menuConfig)
        self.Bmenu.add_cascade(label="Ajuda", menu=menuAjuda)
        self.win.config(menu=self.Bmenu)
        
        self.Bmenu.entryconfig(1,state=DISABLED)
        self.Bmenu.entryconfig(2,state=DISABLED)

    def frames(self):
        self.logonFrame = LabelFrame(self.win, bg="#ddd", height=200, width=300)
        self.logonFrame.pack(anchor=CENTER, padx=10, pady=10, expand=1)
        self.mainFrame = LabelFrame(self.win, bg="#ddd")
        self.mainFrame.pack_forget()
        self.imgMainFrame = LabelFrame(self.win, bg=self.bgFrame)
        self.imgMainFrame.pack_forget()

    def hide(self, wid):
        wid.pack_forget()

    def logon(self):
        
        def confirm(userE,key):
            def permision(user):
                try:
                    return self.list[user]["key"]
                except: return False
            if permision(userE) == key :
                if self.permission == False:
                    self.permission = True
                    print("acess allow : "+self.list[userE]["user"])
                    self.logonFrame.pack_forget()
                    #self.imgMainFrame.pack(side=LEFT, fill=X)
                    #self.mainFrame.pack(side=RIGHT, fill=Y)
                    self.imgMainFrame.place(rely=0, relheight=1, relx=0, relwidth=0.8)
                    self.mainFrame.place(rely=0, relheight=1, relx=0.8, relwidth=1)
                    self.Bmenu.entryconfig(1, state=NORMAL)
                    self.Bmenu.entryconfig(2, state=NORMAL)
                    self.mainWindow()
            else:
                self.erroLogin["text"] = "Acesso Negado"
                self.erroLogin["bg"] = "#333"
                print("Acess danied : "+userE)
        def cancel():
            try:
                self.erroLogin["text"] = ""
                self.erroLogin["bg"] = "#ddd"
                self.userVar.set("")
                self.keyVar.set("")
                self.userE.focus()
            except:
                return
        def scanU(*args):
            try:
                var = self.userVar.get()
                self.userVar.set(var.upper())
                if len(var) > 13:
                    self.userVar.set(var[:-1])
            except: pass
        def scanK(*args):
            var = self.keyVar.get()
            var = self.onlyNum(var)
            self.keyVar.set(var if len(var) < 6 else var[:6])
             
        def windowLogon():
            self.permission = False
            self.window.set("login")
            self.userVar = StringVar()
            self.userVar.trace("w", scanU)
            self.keyVar = StringVar()
            self.keyVar.trace("w", scanK)
            self.erroLogin = Label(self.logonFrame, text="", fg="red", bg="#ddd",font=self.fontelbl)
            self.erroLogin.place(relx=0.3, rely=0.55)
            Label(self.logonFrame, text="LOGIN", font="Times 18 bold ", bg="#ddd").place(relx=0.39, rely=0.1)
            Label(self.logonFrame, text="Usuario", font=self.fontelbl, bg=self.bglbl, bd=1, relief=RIDGE, width=8).place(relx=0.1, rely=0.3)
            Label(self.logonFrame, text="Senha", font=self.fontelbl, bg=self.bglbl, bd=1, relief=RIDGE, width=8).place(relx=0.1, rely=0.42)
            self.userE = Entry(self.logonFrame, font=self.fontelbl, textvariable=self.userVar)
            self.userE.place(relx=0.4, rely=0.3, relwidth=0.5)
            keyE = Entry(self.logonFrame, font=self.fontelbl, show="#", textvariable=self.keyVar)
            keyE.place(relx=0.4, rely=0.42, relwidth=0.5)
            Button(self.logonFrame, text="Confirmar", width=8, command=lambda: confirm(self.userE.get().lower(), keyE.get())).place(relx=0.2, rely=0.7)
            Button(self.logonFrame, text="Cancelar", width=8, command=cancel).place(relx=0.45, rely=0.7)
            Button(self.logonFrame, text="sair", width=8, command=self.win.destroy).place(relx=0.7, rely=0.7)
            self.userE.focus()
        windowLogon()

    def database(self):
        def check(db):
            try:
                with open(db,"r"):
                    return True
            except: return False
        def createdb(name):
            bank = sqlite3.connect(name)
            cursor = bank.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS keysOfUsers(idcontrole integer primary key autoincrement, user text, key text)")
            cursor.execute("CREATE TABLE IF NOT EXISTS Clientes(idControle integer primary key autoincrement, cliente text")
            bank.commit()

        def users():
            self.cursor.execute("SELECT * FROM keysOfUsers")
            self.list = {}
            bnk = self.cursor.fetchall()
            for Id,user,key in bnk:
                self.list[user] = {
                    "id":Id,
                    "user": user,
                    "key": key
                    }
        db = "SBD.sql"
        if check(db):
            self.bank = sqlite3.connect(db)
            self.cursor = self.bank.cursor()

            users()
    
    def mainWindow(self):
        img = Label(self.imgMainFrame, text='', image=self.Photoimg, bg=self.bgFrame).pack()
        widthbtn = 25
        #btnNote = Button(self.mainFrame,text="Emitir Nota de Autorização", font=self.fontelbl, width=widthbtn, height=self.heightbtn, state=DISABLED).pack(pady=2, anchor=W)
        btnCheckNote = Button(self.mainFrame, text="Vender", font=self.fontelbl, width=widthbtn, height=self.heightbtn, state=DISABLED).pack(pady=2, anchor=W)
        btnrelatorio = Button(self.mainFrame, text="Movimento", font=self.fontelbl, width=widthbtn, height=self.heightbtn, state=DISABLED).pack(pady=2, anchor=W)
        btnclientes = Button(self.mainFrame, text="Clientes", font=self.fontelbl, width=widthbtn, height=self.heightbtn, command=self.ClientesWindow).pack(pady=2, anchor=W)
        bntFechar = Button(self.mainFrame, text="Sair", font=self.fontelbl, width=widthbtn, height=self.heightbtn, command=self.win.destroy).pack(pady=2, anchor=W)
    
    def ClientesWindow(self):
        try: self.CWindow.destroy()
        except: pass
        self.CWindow = Toplevel()
        self.CWindow.geometry("600x500")
        self.CWindow.title("Clientes")
        self.CWindow.focus_force()
        bg="#ccc"
        self.CWindow.configure(bg=bg)
        self.CWindow.resizable(False,False)
        def abas():
            aba = ttk.Notebook(self.CWindow)
            aba.place(x=0, y=0, width=600, height=500)
            dadosFrame = Frame(aba)
            empresaFrame = Frame(aba)
            enderecoFrame = Frame(aba)
            dadosFrame.config(bg=bg)
            empresaFrame.config(bg=bg)
            enderecoFrame.config(bg=bg)
            aba.add(dadosFrame, text="Dados Pessoais")
            aba.add(empresaFrame, text="Empresarial")
            aba.add(enderecoFrame, text="Endereço")
            
            
            def dados():
                self.fonte10b = "arial 10 bold"
                self.widthBtn = 20
                def label(x,y,text):
                    Label(dadosFrame, text=text, font=self.fonte10b, bg=bg).place(x=x, y=y)
                #Labels
                label(30,20,"COD")
                label(90,20,"NOME COMPLETO")
                label(30,80, "CPF")
                label(150,80,"RG")
                label(250,80,"DATA DE EMISSÂO")
                label(400,80, "DATA DE NASCIMENTO")
                label(30,120, "TELEFONE")
                label(150,120,"ESTADO CIVIL")
                label(250, 120, "CD. NASCIMENTO")
                label(400, 120, "UF")
                label(445, 120, "NACIONALIDADE")
                label(465, 170, "Data de Cadrasto")
                label(30,170,"NOME DA MÃE")
                label(30,213,"NOME DO PAI")
                label(30,263,"PESSOAS AUTORIZADAS ( , )")

                # orgao expedidor, renda, limite de compra, endereço: endereço, bairro, cidade, cep
                def codfilter(*args):
                    values = self.codVar.get()
                    value = self.onlyNum(values)
                    self.codVar.set(value)
                def nomefilter(*args):
                    value = self.onlyAlfa(self.nomeVar.get(),90)
                    self.nomeVar.set(value.upper())
                def cpffilter(*args):
                    value = self.onlyNum(self.cpfVar.get())
                    def formate(valueCpf):
                        val = ""
                        ind = 1
                        for i in valueCpf:
                            val +=i
                            if len(valueCpf) == 11:
                                if ind == 3 or ind == 6: 
                                    val +="."
                                elif ind == 9:
                                    val += "-"
                            ind +=1
                        return val
                    if len(value) > 11: value = value[:11]
                    value = formate(value)
                    self.cpfVar.set(value)
                def rgfilter(*args):
                    value = str(self.rgVar.get())
                    self.rgVar.set(self.onlyNum(value,"-"))
                def demissaofilter(*args):
                    value =self.onlyNum(self.dEmissaoVar.get())
                    if len(value) > 8 :
                        val = self.dEmissaoVar.get()
                        self.dEmissaoVar.set(val[:8])
                        value = value[:8]
                    ind = 0
                    self.dEmissao.delete(0,END)
                    for i in value:
                        if ind == 2 or ind == 4:
                            self.dEmissao.insert(END, "/")
                            self.dEmissao.insert(END, i)
                        else:
                            self.dEmissao.insert(END, i)
                        ind += 1
                def dNascimentoFilter(*args):
                    value =self.onlyNum(self.dNascimentoVar.get())
                    if len(value) > 8 :
                        val = self.dNascimentoVar.get()
                        self.dNascimentoVar.set(val[:8])
                        value = value[:8]
                    ind = 0
                    self.dNascimento.delete(0,END)
                    for i in value:
                        if ind == 2 or ind == 4:
                            self.dNascimento.insert(END, "/")
                            self.dNascimento.insert(END, i)
                        else:
                            self.dNascimento.insert(END, i)
                        ind += 1
                def tellfilter(*args):
                    value = self.onlyNum(self.tellVar.get())
                    if len(value) > 11 :value = value[:11]
                    ind = 0 
                    self.tell.delete(0,END)
                    for i in value:
                        if ind == 0:
                            self.tell.insert(END,"(")
                            self.tell.insert(END,i)
                        elif ind == 2:
                            self.tell.insert(END,") ")
                            self.tell.insert(END,i)
                        elif ind == 7:
                            self.tell.insert(END,"-")
                            self.tell.insert(END,i)
                        else: self.tell.insert(END,i)
                        ind += 1
                def cNascimentoFilter(*args):
                    value = self.onlyAlfa(self.cNascimentoVar.get(),17)
                    self.cNascimentoVar.set(value)
                def ufFilter(*args):
                    value = self.onlyAlfa(self.ufVar.get(),4)
                    self.ufVar.set(value.upper())
                def nacionalidadeFilter(*args): 
                    self.nacionalidadeVar.set(self.onlyAlfa(self.nacionalidadeVar.get(),30))
                def dtCadrastoFilter(*args):
                    value =self.onlyNum(self.dtCadrastoVar.get())
                    if len(value) > 8 :
                        val = self.dtCadrastoVar.get()
                        self.dtCadrastoVar.set(val[:8])
                        value = value[:8]
                    ind = 0
                    self.dtCadrasto.delete(0,END)
                    for i in value:
                        if ind == 2 or ind == 4:
                            self.dtCadrasto.insert(END, "/")
                            self.dtCadrasto.insert(END, i)
                        else:
                            self.dtCadrasto.insert(END, i)
                        ind += 1
                #mae pai pAuto
                def maeFilter(*args):
                    self.maeVar.set(self.onlyAlfa(self.maeVar.get(),90).upper())
                def paiFilter(*args):
                    self.paiVar.set(self.onlyAlfa(self.paiVar.get(),90).upper())
                def pAutoFilter(*args):
                    self.pAutorizaVar.set(self.onlyAlfa(self.pAutorizaVar.get(),90,diferent=",").upper())
                    
                self.codVar = StringVar()
                self.codVar.trace("w", codfilter)
                self.nomeVar = StringVar()
                self.nomeVar.trace("w", nomefilter)
                self.cpfVar = StringVar()
                self.cpfVar.trace("w", cpffilter)
                self.rgVar = StringVar()
                self.rgVar.trace("w", rgfilter)
                self.dEmissaoVar = StringVar()
                self.dEmissaoVar.trace("w",demissaofilter)
                self.tellVar = StringVar()
                self.tellVar.trace("w",tellfilter)
                self.cNascimentoVar = StringVar()
                self.cNascimentoVar.trace("w",cNascimentoFilter)
                self.dNascimentoVar = StringVar()
                self.dNascimentoVar.trace("w",dNascimentoFilter)
                self.ufVar = StringVar()
                self.ufVar.trace("w",ufFilter)
                self.nacionalidadeVar = StringVar()
                self.nacionalidadeVar.trace("w",nacionalidadeFilter)
                self.dtCadrastoVar = StringVar()
                self.dtCadrastoVar.trace("w",dtCadrastoFilter)
                self.maeVar = StringVar()
                self.maeVar.trace("w",maeFilter)
                self.paiVar = StringVar()
                self.paiVar.trace("w",paiFilter)
                self.pAutorizaVar = StringVar()
                self.pAutorizaVar.trace("w",pAutoFilter)
                
                self.cod = Entry(dadosFrame, font=self.fonte10b, width=7, textvariable=self.codVar)
                self.cod.place(x=30, y=39)
                self.nome = Entry(dadosFrame, font=self.fonte10b, width=60, textvariable=self.nomeVar)
                self.nome.place(x=90, y=39)
                self.cpf = Entry(dadosFrame, font=self.fonte10b, width=14, textvariable=self.cpfVar)
                self.cpf.place(x=30, y=99)
                self.rg = Entry(dadosFrame, font=self.fonte10b, width=11, textvariable=self.rgVar)
                self.rg.place(x=150, y=99)
                self.dEmissao = Entry(dadosFrame, font=self.fonte10b, width=13, textvariable=self.dEmissaoVar)
                self.dEmissao.place(x=250, y=99)
                self.dNascimento = Entry(dadosFrame, font=self.fonte10b, width=13, textvariable=self.dNascimentoVar)
                self.dNascimento.place(x=400, y=99)
                self.tell = Entry(dadosFrame, font=self.fonte10b, width=15, textvariable=self.tellVar)
                self.tell.place(x=30, y=139)
                estadoList = ["Solteiro(a)","Convivente","União Estavel" ,"casado(a)","Viúvo(a)","Disvorciado(a)"]
                self.eCivil = ttk.Combobox(dadosFrame, font=self.fonte10b, width=10,values=estadoList)
                self.eCivil.place(x=150, y=139)
                
                self.cNascimento = Entry(dadosFrame, font=self.fonte10b, width=17, textvariable=self.cNascimentoVar)
                self.cNascimento.place(x=250, y=139)
                self.uf = Entry(dadosFrame, font=self.fonte10b, width=5, textvariable=self.ufVar)
                self.uf.place(x=400, y=139)
                self.nascionalidade = Entry(dadosFrame, font=self.fonte10b, width=15, textvariable=self.nacionalidadeVar)
                self.nascionalidade.place(x=445, y=139)
                self.dtCadrasto = Entry(dadosFrame, font=self.fonte10b, width=15, textvariable=self.dtCadrastoVar)
                self.dtCadrasto.place(x=465, y=189)
                self.mae = Entry(dadosFrame, font=self.fonte10b, width=60, textvariable=self.maeVar)
                self.mae.place(x=30, y=189)
                self.pai = Entry(dadosFrame, font=self.fonte10b, width=60, textvariable=self.paiVar)
                self.pai.place(x=30, y=232)
                self.pAutorizadas = Entry(dadosFrame, font=self.fonte10b, width=60, textvariable=self.pAutorizaVar)
                self.pAutorizadas.place(x=30, y=282)
                self.cod.focus_force()

                def Add():
                    def save():
                        ClientePF = {
                        "cod":"Null",
                        "nome":"Null",
                        "cpf":"Null",
                        "rg":"Null",
                        "data de emissao" : "Null",
                        "data de nascimento" : "Null",
                        "telefone" : "Null",
                        "estado civil" : "Null",
                        "cd de nascimento" : "Null",
                        "uf":"Null",
                        "nacionalidade":"Null",
                        "data de cadrasto":"Null",
                        "mae":"Null",
                        "pai":"Null",
                        "pessoas autorizadas":"Null",
                        "endereco":"Null",
                        "cidade":"Null",
                        "bairro":"Null",
                        "vip":None,
                        "renda mensal":None,
                        "limite":None,
                        "referencia":"",
                        "avaliador":{"nome":"Null","telefone":"","email":"","endereco":""}
                        }
                        
                    
                def Remove():pass
                def Update():pass
                def Erase():
                    
                    self.cod.delete(0,END)
                    self.nome.delete(0,END)
                    self.cpf.delete(0,END)
                    self.rg.delete(0,END)
                    self.dEmissao.delete(0,END)
                    self.dNascimento.delete(0,END)
                    self.tell.delete(0,END)
                    self.eCivil.set("")
                    self.cNascimento.delete(0,END)
                    self.uf.delete(0,END)
                    self.nascionalidade.delete(0,END)
                    self.dtCadrasto.delete(0,END)
                    self.mae.delete(0,END)
                    self.pai.delete(0,END)
                    self.pAutorizadas.delete(0,END)
                    self.cod.focus()
                def History():pass
                def ListClients():
                    clienteWin = Toplevel(dadosFrame)
                
                self.adBtn = Button(dadosFrame, text='Cadastrar Novo Cliente', font=self.fonte10b, bg=self.bgbtn, width=22,command=Add, state=DISABLED).place(x=30, y=410)
                self.remBtn = Button(dadosFrame, text='Apagar Cliente', font=self.fonte10b, bg=self.bgbtn,width=self.widthBtn,command=Remove, state=DISABLED).place(x=220, y=410)
                self.upBtn = Button(dadosFrame, text='Atualizar Dados', font=self.fonte10b, bg=self.bgbtn,width=self.widthBtn,command=Update, state=DISABLED).place(x=400, y=410)
                self.eraseBtn = Button(dadosFrame, text='Limpar Para Nova Consulta', font=self.fonte10b, bg=self.bgbtn,width=22,command=Erase).place(x=30, y=440)
                self.histBtn = Button(dadosFrame, text='Consultar Historico', font=self.fonte10b, bg=self.bgbtn,width=self.widthBtn,command=History, state=DISABLED).place(x=220, y=440)
                self.lClientsBtn = Button(dadosFrame, text='Lista de Clientes', font=self.fonte10b,width=self.widthBtn,command=ListClients, bg=self.bgbtn).place(x=400, y=440)
            
            def PessoaJuridica():
                #master = empresaFrame
                def codFilter(*args):
                    self.codeVar.set(self.onlyNum(self.codeVar.get()))
                def nameFilter(*args):
                    self.nameFantasiVar.set(self.nameFantasiVar.get().upper())
                def rsocialFilter(*args):
                    self.rsocialeVar.set(self.onlyAlfa(self.rsocialeVar.get(), 80))
                def iestadualFilter(*args):
                    self.iestadualVar.set(self.onlyNum(self.iestadualVar.get()))
                def cnpjFilter(*args):
                    self.cnpjVar.set(self.onlyNum(self.cnpjVar.get()))
                def tellFilter(*args):
                    value = self.telleVar.get()
                def emailFilter(*args):
                    value = self.emaileVar.get().lower()
                    email = ""
                    for i in value:
                        if "@" in email and i == "@":
                            continue
                        email += i
                    self.emaileVar.set(email)
                def repFilter(*args):
                    self.repeVar.set(self.onlyAlfa(self.repeVar.get(), 80))
                def tellrepFilter(*args):
                    value =self.onlyNum( self.tellrepVar.get())
                def pAutoFilter(*args):
                    self.pAutoeVar.set(self.onlyAlfa(self.pAutoeVar.get(),diferent=","))
                def renMensalFilter(*args):
                    self.rendmeVar.set(self.onlyNum(self.rendmeVar.get()))
                def limiteFilter(*args):
                    self.limiteeVar.set(self.onlyNum(self.limiteeVar.get()))
                def dtCadFilter(*args):
                    self.dtcadeVar.set(self.onlyNum(self.dtcadeVar.get()))
                
                def label(x,y,text):
                    Label(empresaFrame, text=text, font=self.fonte10b, bg=bg).place(x=x, y=y)
                label(30,20,"COD")
                label(150,20,"NOME FANTASIA")
                label(30,60, "RAZÃO SOCIAL")
                label(30,100,"INSCRICAO ESTADUA")
                label(250,100,"CNPJ")
                label(393,100, "TELEFONE EMPRESA")
                label(30,140,"EMAIL")
                label(30,180, "REPRESENTANTE")
                label(393, 180, "TEL. REPRESENTANTE")
                label(30,220,"PESSOAS AUTORIZADAS ( , )")
                label(30, 269, "RENDA MENSAL")
                label(230,269, "LIMITE")
                label(393,269, "DATA CADRASTO")
                
                self.codeVar = StringVar()
                self.codeVar.trace("w",codFilter)
                self.nameFantasiVar = StringVar()
                self.nameFantasiVar.trace("w", nameFilter)
                self.rsocialeVar = StringVar()
                self.rsocialeVar.trace("w",rsocialFilter)
                self.iestadualVar = StringVar()
                self.iestadualVar.trace("w",iestadualFilter)
                self.cnpjVar = StringVar()
                self.cnpjVar.trace("w",cnpjFilter)
                self.telleeVar = StringVar()
                self.telleeVar.trace("w",tellFilter)
                self.emaileVar = StringVar()
                self.emaileVar.trace("w", emailFilter)
                self.repeVar = StringVar()
                self.repeVar.trace("w",repFilter)
                self.tellrepVar = StringVar()
                self.tellrepVar.trace("w",tellrepFilter)
                self.pAutoeVar = StringVar()
                self.pAutoeVar.trace("w",pAutoFilter)
                self.rendmeVar = StringVar()
                self.rendmeVar.trace("w",renMensalFilter)
                self.limiteeVar = StringVar()
                self.limiteeVar.trace("w",limiteFilter)
                self.dtcadeVar = StringVar()
                self.dtcadeVar.trace("w",dtCadFilter)
                
                self.codE = Entry(empresaFrame, font=self.fonte10b, width=7, textvariable=self.codeVar)
                self.codE.place(x=30,y=39)
                self.nFantasiaE = Entry(empresaFrame, font=self.fonte10b, width=55, textvariable=self.nameFantasiVar)
                self.nFantasiaE.place(x=150,y=39)
                self.rSocialE = Entry(empresaFrame, font=self.fonte10b, width=72, textvariable=self.rsocialeVar)
                self.rSocialE.place(x=30,y=79)
                self.iEstadualE = Entry(empresaFrame, font=self.fonte10b, width=30, textvariable=self.iestadualVar)
                self.iEstadualE.place(x=30,y=119)
                self.cnpjE = Entry(empresaFrame, font=self.fonte10b, width=18, textvariable=self.cnpjVar)
                self.cnpjE.place(x=250,y=119)
                self.tellEE = Entry(empresaFrame, font=self.fonte10b, width=20, textvariable=self.telleeVar)
                self.tellEE.place(x=393,y=119)
                self.emailE = Entry(empresaFrame, font=self.fonte10b, width=72, textvariable=self.emaileVar)
                self.emailE.place(x=30,y=159)
                self.repE = Entry(empresaFrame, font=self.fonte10b, width=50, textvariable=self.repeVar)
                self.repE.place(x=30,y=199)
                self.tellRE = Entry(empresaFrame, font=self.fonte10b, width=20, textvariable=self.tellrepVar)
                self.tellRE.place(x=393,y=199)
                self.pAutoE = Entry(empresaFrame, font=self.fonte10b, width=72, textvariable=self.pAutoeVar)
                self.pAutoE.place(x=30,y=239)
                self.rendMensalE = Entry(empresaFrame, font=self.fonte10b, width=20, textvariable=self.rendmeVar)
                self.rendMensalE.place(x=30, y=289)
                self.limiteE = Entry(empresaFrame, font=self.fonte10b, width=20, textvariable=self.limiteeVar)
                self.limiteE.place(x=230, y=289)
                self.dtCadE = Entry(empresaFrame, font=self.fonte10b, width=20, textvariable=self.dtcadeVar)
                self.dtCadE.place(x=393, y=289)
                
                def Add():
                    
                    ClientePessoaJuridica={
                        "cod":None,
                        "nomeFantasia":"",
                        "razaoSocial":"",
                        "inscriçãoEstadual":"",
                        "cnpj":None,
                        "telefone":"",
                        "endereco":"",
                        "email":"",
                        "representante":"",
                        "TelefoneRepresentante":"",
                        "pessoas autorizadas":None,
                        "rendaMensal":"",
                        "limite":"",
                        "dataCadrasto":""
                        }
                    
                def Remove():pass
                def Update():pass
                def Erase():
                    self.codE.delete(0,END)
                    self.nFantasiaE.delete(0,END)
                    self.rSocialE.delete(0,END)
                    self.iEstadualE.delete(0,END)
                    self.cnpjE.delete(0,END)
                    self.tellEE.delete(0,END)
                    self.emailE.delete(0,END)
                    self.repE.delete(0,END)
                    self.tellRE.delete(0,END)
                    self.pAutoE.delete(0,END)
                    self.codE.focus()
                def History(): pass
                #def ListClients():pass
                
                self.adBtnE = Button(empresaFrame, text='Cadastrar Nova Empresa', font=self.fonte10b, bg=self.bgbtn, width=22,command=Add, state=DISABLED).place(x=30, y=410)
                self.remBtnE = Button(empresaFrame, text='Apagar Empresa', font=self.fonte10b, bg=self.bgbtn,width=self.widthBtn,command=Remove, state=DISABLED).place(x=220, y=410)
                self.upBtnE = Button(empresaFrame, text='Atualizar Dados', font=self.fonte10b, bg=self.bgbtn,width=self.widthBtn,command=Update, state=DISABLED).place(x=400, y=410)
                self.eraseBtnE = Button(empresaFrame, text='Limpar Para Nova Consulta', font=self.fonte10b, bg=self.bgbtn,width=22,command=Erase).place(x=30, y=440)
                self.histBtnE = Button(empresaFrame, text='Consultar Historico', font=self.fonte10b, bg=self.bgbtn,width=self.widthBtn,command=History, state=DISABLED).place(x=220, y=440)
                #self.lClientsBtnE = Button(empresaFrame, text='Lista de Clientes', font=self.fonte10b,width=self.widthBtn,command=ListClients, bg=self.bgbtn).place(x=400, y=340)

                
                pass
            
            dados()
            PessoaJuridica()
            
        abas()
        self.CWindow.transient(self.win)
        self.CWindow.grab_set()
        self.CWindow.mainloop()

if __name__ == "__main__":
    app()
    quit()
