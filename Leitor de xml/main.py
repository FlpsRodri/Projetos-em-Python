import xmltodict
import os
from tkinter import *
#import sqlite3
from tkinter import ttk,messagebox
from datetime import datetime
import pyperclip
import keyboard

class relogio(object):
    def __init__(self):
        pass
    def run_clock(self,master,time=(False,0,0), date=(False,0,0), font=None, bg="white", fg="black"):
        time,timex,timey = time[0], time[1], time[2]
        date,datex,datey = date[0], date[1], date[2]
        if time:
            self.time = Label(master, text="", font=font, bg=bg, fg=fg)
            self.time.place(relx=timex, rely=timey)
        if date:
            self.date = Label(master,  font=font, bg=bg, fg=fg)
            self.date.place(relx=datex,rely=datey)    
        self.relogio(time=time,date=date)
    def relogio(self,time=False,date=False):
        self.tempo = datetime.now()
        if time:
            hora = self.tempo.strftime("%H:%M:%S")
            self.time.config(text=hora)
            self.time.after(500, lambda:self.relogio(time=True))
            
        if date:
            self.get_time()
    def get_time(self):
        dia_semana = self.tempo.strftime("%A")
        dia = self.tempo.day
        mes = (f"0{str(self.tempo.month)}" if self.tempo.month < 10 else str(self.tempo.month))
        ano = self.tempo.strftime("%Y")
        self.date.config(text=f"{dia_semana}   {str(dia)}/{str(mes)}/{ano}")
        if not self.time:
            self.date.after(500, lambda:self.relogio(date=True))
            
class Table(object):
    def __init__(self):
        pass
        
    def filter_num(self,key):
        kargs = "1234567890"
        return "".join(i for i in key if i in kargs)
    
    def window(self, master):
        Style = ttk.Style()
        Style.configure("Treeview",font=("Times",11))
        self.cb_descriptionVar = IntVar(master=master,value=0)
        self.cb_description = Checkbutton(master=master, text="Descrição exata", variable=self.cb_descriptionVar, bg=self.main_bg,fg=self.main_fg, command=lambda:print(self.cb_descriptionVar.get()))
        self.cb_description.place(relx=0.06,rely=0.08)
        
        def labels():
            Label(master, text="GTIN / Descrição do produto",font=self.main_font,bg=self.main_bg,fg=self.main_fg).place(relx=0.05,rely=0.02)
            Label(master, text="N° NF-e", font=self.main_font,bg=self.main_bg,fg=self.main_fg).place(relx=0.4,rely=0.11)
            Label(master, text="Chave de Acesso (44 digitos)", font=self.main_font,bg=self.main_bg,fg=self.main_fg).place(relx=0.05,rely=0.11)
            Label(master, text="Items: ", font=self.main_font,bg=self.main_bg,fg=self.main_fg).place(relx=0.63,rely=0.05)
            Label(master, text="Maior Valor: ", font=self.main_font,bg=self.main_bg,fg=self.main_fg).place(relx=0.63,rely=0.08)
            Label(master, text="Menor Valor: ", font=self.main_font,bg=self.main_bg,fg=self.main_fg).place(relx=0.63,rely=0.11)
            Label(master,text="Exibir", font=self.main_font,bg=self.main_bg,fg=self.main_fg).place(relx=0.63,rely=0.14)
            self.value_items = Label(master, text="0", font=self.main_font,bg=self.main_bg,fg=self.main_fg)
            self.value_items.place(relx=0.73,rely=0.05)
            self.value_MaxValue = Label(master, text="0,00", font=self.main_font,bg=self.main_bg,fg=self.main_fg) 
            self.value_MaxValue.place(relx=0.73,rely=0.08)
            self.value_MinValue = Label(master, text="0,00", font=self.main_font,bg=self.main_bg,fg=self.main_fg) 
            self.value_MinValue.place(relx=0.73,rely=0.11)
        def entrys():
            
            def filter_nnfe(*args):
                key = self.variable_nnfe.get()
                self.variable_nnfe.set(self.filter_num(key))
            def filter_keynfe(*arg):
                key = self.variable_keynfe.get()
                if len(key) < 44: self.variable_keynfe.set(self.filter_num(key=key))
                else:self.variable_keynfe.set(self.filter_num(key=key)[:44])
                
            self.variable_nnfe = StringVar(master=master)
            self.variable_nnfe.trace("w",filter_nnfe)
            self.variable_keynfe = StringVar(master=master)
            self.variable_keynfe.trace("w",filter_keynfe)
            
            self.prodDescription = Entry(master, bg="#F3FCA1", width=100)
            self.entry_keynfe = Entry(master, bg="#F3FCA1", textvariable=self.variable_keynfe, width=50, font="times 12 bold")
            self.entry_nnfe = Entry(master, bg="#F3FCA1", textvariable=self.variable_nnfe)
            
            self.prodDescription.focus()
            #self.codEan.place(relx=0.1, rely=0.08)
            #self.prodDescription.place(relx=0.25, rely=0.08)
            self.prodDescription.place(relx=0.05, rely=0.055)
            self.entry_keynfe.place(relx=0.05,rely=0.14)
            self.entry_nnfe.place(relx=0.4, rely=0.14)
            
        def table():
            colunas = ["EAN", "PRODUTO","CD", "V. UNIT", "V.DESC","QTD", "U TRIB", "V. TRIB", "QTN. TRIB", "V. TOTAL", "ICMS", "FORNECEDOR", "DATA", "NCM", "N° NFE", "C. NFE"]
            columns_geo = {"EAN":[100], "PRODUTO":[360],"CD":[30], "V. UNIT":[60], "V.DESC":[60],"QTD":[40] , "U TRIB":[35], "V. TRIB":[60], "QTN. TRIB":[40],"V. TOTAL":[90], "ICMS":[60], "FORNECEDOR":[200], "DATA":[100], "NCM":[100], "N° NFE":[100], "C. NFE":[100]}
            self.tabela = ttk.Treeview(master, columns=colunas, show="headings", style="Treeview")
            self.tabela.place(relx=0.01, rely=0.2, relwidth=0.97, relheight=0.6)
            
            vs = Scrollbar(master=master, orient="vertical", command=self.tabela.yview, width=15)
            self.tabela.configure(yscrollcommand=vs.set)
            vs.place(rely=0.2, relx=0.97, relheight=0.6)
            hs = Scrollbar(master=master, orient="horizontal", command=self.tabela.xview)
            self.tabela.configure(xscrollcommand=hs.set)
            hs.place(rely=0.8, relx=0.01, relwidth=0.97)
            
            for coluna in colunas:
                self.tabela.heading(coluna, text=coluna)
                tamanho = columns_geo[coluna][0]
                
                self.tabela.column(coluna, width=tamanho, minwidth=tamanho)
            
        labels(), entrys(), table()
        
        #self.codEan.bind("<Return>",self.get_key)
        self.prodDescription.bind("<Return>",self.get_key)
        self.entry_nnfe.bind("<Return>",self.get_key)
        self.entry_keynfe.bind("<Return>",self.get_key)

    def table2(self,master):
        #["file_name","emitente","CNPJ|CPF","@Id","Cliente", "dhEmi","nNFe","cNFe","nNF","vTotProd", "vNF","fat",{"fat","dup"},"vTotDesc"]
        def select(*args):
            
            item = self.tabela2.selection()[0]
            nfe = self.nfeInTable[(self.tabela2.get_children()).index(item)]
            self.viewResultTable2(nfe)
            
        colunas = ["FORNECEDOR","DT. EMISSAO","N° NFE","V. TOTAL"]
        columns_geo = {"FORNECEDOR":[320],"DT. EMISSAO":[90],"N° NFE":[90],"V. TOTAL":[120]}
        self.tabela2 = ttk.Treeview(master, columns=colunas, show="headings")
        self.tabela2.place(relx=0.1, rely=0.5, relheight=0.48)
        self.tabela2.bind("<Double-Button-1>",select)
        self.tabela2.bind("<Return>",select)
        vs = Scrollbar(master=master, orient="vertical", command=self.tabela2.yview, width=15)
        self.tabela2.configure(yscrollcommand=vs.set)
        vs.place(rely=0.5, relx=0.8 ,relheight=0.48)
        
        for coluna in colunas:
            self.tabela2.heading(coluna, text=coluna)
            tamanho = columns_geo[coluna][0]
            self.tabela2.column(coluna, width=tamanho, minwidth=tamanho)
    
    def InsertOnTable2(self,keyAgr,key):
        
        #columns : "FORNECEDOR","DT. EMISSAO","N° NFE","V. TOTAL"
        try: self.tabela2.delete(*self.tabela2.get_children())
        except Exception: pass
        
        amount = 0
        self.nfeInTable = []
        for nfe in self.list_nfe:
            if keyAgr == nfe[key]:
                amount += 1
                self.nfeInTable.append(nfe)
                dicNfe = nfe
                values = [nfe["emitente"],nfe["dhEmi"],nfe["nNFe"],nfe["vNF"]]
                self.tabela2.insert("",END,values=values)
        if amount == 1:
            self.viewResultTable2(dicNfe)
        else: dicNfe = None
        
    def viewResultTable2(self,nfe):
        #nfe = {"emitente":emitente["nome"],"CNPJ|CPF":emitente["CNPJ|CPF"],"Cliente":cliente["nome"], 
        # "dhEmi":dtEmissao,"nNFe":nNFE,"cNFe":cNFe,"nNF":nNFe,"vTotProd":vTotProd, "vNF":vTotNf,
        # "fat":{"fat":fat,"dup":dup},"vTotDesc":vTotDesc}
        pyperclip.copy(nfe["nNF"])
        self.lblFornecedor["text"] = nfe["emitente"]
        self.lblDest["text"] = nfe["Cliente"]
        self.lblNatOp["text"] = nfe["natOp"]
        
        self.lblNNf["text"] = nfe["nNFe"]
        self.lblCdNf["text"] = nfe["cNFe"]
        self.lblDtEmi["text"] = nfe["dhEmi"]
        
        self.lblKeyAcess["text"] = nfe["nNF"]
        self.lblVlProd["text"] = nfe["vTotProd"]
        self.VlNf["text"] = nfe["vNF"]
        
        #fatFrame = LabelFrame(nfe_master, text="Fatura ",width=260, height=80, bg=self.main_bg, bd=1)
        #fatFrame.place(rely=0.17,relx=0.1, width=640, height=122)
    
    def Frmt(self, num):
        num = float(num)
        return format(num,".2f")
        
class app(Table,relogio):
    
    def __init__(self):
        
        arquivos = os.listdir("NFE")
        arquivos = list(filter(lambda x : x[-3:] == "xml",arquivos ))
        self.produtos = []
        self.list_nfe = []
        
        for xml in arquivos:
            self.get_info(xml)
            
        
        self.root = Tk()
        self.config(self.root)
        
        nb = ttk.Notebook(self.root)
        #nb.place(x=0 , y=0 , width=self.main_geometry["width"] , height=self.main_geometry["height"])
        nb.place(relx=0, rely=0, relheight=1, relwidth=1)
        aba1 = Frame(nb, bg=self.main_bg)
        aba2 = Frame(nb, bg=self.main_bg)
        
        nb.add(aba1, text="Buscar Produtos" )
        nb.add(aba2, text="Buscar Nota Fiscal Eletrônica")
        
        self.window(aba1)
        self.window_search_nfe(master=aba2)
        self.run_clock(master=aba1,time=(True,0.8,0.96),date=(True,0.85,0.96), bg=self.main_bg, font="times 12 bold")
        self.hotkeys()
        
        self.root.mainloop()
    
    def hotkeys(self):
        def st():
            keyboard.press("shift+tab")
        shitReturnt = keyboard.add_hotkey("shift+return",st)
    
    def config(self, master):
        self.main_bg = "#ddd"
        self.main_fg = "#000000"
        self.main_geometry = {"height":"720","width":"1300"}
        self.main_title = "Tabela Produtos"
        self.main_icon = "icon.ico"
        self.main_dataBase = "Banco_de_dados.sql"
        self.main_title_font = "times 18 bold"
        self.main_font = "consolas 12"

        master.state("zoomed")
        master["bg"] = self.main_bg
        master.title(self.main_title)
        master.geometry(f"{self.main_geometry['width']}x{self.main_geometry['height']}")
        master.resizable(False,False)
        
    def window_search_nfe(self, master):
        master = LabelFrame(master, width=900)
        master.pack(anchor=CENTER,fill=Y,expand=Y)
        master_widgets = Frame(master, bg=self.main_bg)
        master_widgets.place(relx=0, rely=0, relwidth=1, relheight=0.55)
        def labels():
            Label(master_widgets, text="N° Nota Fiscal",  font=self.main_font, bg=self.main_bg, fg=self.main_fg).place(relx=0.1, rely=0.05)
            Label(master_widgets, text="Cd Nota Fiscal",  font=self.main_font, bg=self.main_bg, fg=self.main_fg).place(relx=0.5, rely=0.05)
            Label(master_widgets, text="Fornecedor",      font=self.main_font, bg=self.main_bg, fg=self.main_fg).place(relx=0.1, rely=0.18)
            Label(master_widgets, text="Chave de acesso", font=self.main_font, bg=self.main_bg, fg=self.main_fg).place(relx=0.1, rely=0.32)
             
        def entrys():
            
            font = "times 12 bold"
            self.entry_Nnf = Entry(master_widgets, bg="#F3FCA1", width=25, font=font)
            self.entry_Cnf = Entry(master_widgets, bg="#F3FCA1", width=25, font=font)
            values = list(map(lambda x: x["emitente"], self.list_nfe))
            values = sorted(set(values), key=str.upper)
            self.cbb_emitent = ttk.Combobox(master_widgets,values=values, width=68, font=font)
            self.keyAcessVar = StringVar()
            self.entry_KeyAcess = Entry(master_widgets,textvariable=self.keyAcessVar, bg="#F3FCA1", width=70, font=font)
            self.entry_Nnf.place(relx=0.1, rely=0.12)
            self.entry_Cnf.place(relx=0.5, rely=0.12)
            self.cbb_emitent.place(relx=0.1, rely=0.25)
            self.entry_KeyAcess.place(relx=0.1, rely=0.39)
            self.entry_Nnf.bind("<Return>",self.get_key)
            self.entry_Cnf.bind("<Return>",self.get_key)
            self.cbb_emitent.bind("<Return>",self.get_key)
            self.entry_KeyAcess.bind("<Return>",self.get_key)
        
        def nfe():
            def filter(*args):
                pass
            
            font = "consolas 10 bold"
            nfe_master = Frame(master, bg=self.main_bg)
            nfe_master.place(relx=0, rely=0.55, relwidth=1, relheight=1)
            titleFrame = LabelFrame(nfe_master, width=290, height=80, bg=self.main_bg, bd=1)
            titleFrame.place(rely=0, relx=0.05, width=260, height=122)
            Label(titleFrame,text="Fornecedor", bg=self.main_bg, fg=self.main_fg, font=font,anchor=W).pack(anchor=W)
            self.lblFornecedor = Label(titleFrame,text="", bg=self.main_bg, fg=self.main_fg, font=font)
            self.lblFornecedor.pack(anchor=W)
            Label(titleFrame,text="Destinatario", bg=self.main_bg, fg=self.main_fg, font=font).pack(anchor=W)
            self.lblDest = Label(titleFrame,text="", bg=self.main_bg, fg=self.main_fg, font=font)
            self.lblDest.pack(anchor=W)
            Label(titleFrame,text="Nat. da Operação", bg=self.main_bg, fg=self.main_fg, font=font).pack(anchor=W)
            self.lblNatOp = Label(titleFrame,text="", bg=self.main_bg, fg=self.main_fg, font=font)
            self.lblNatOp.pack(anchor=W)
            
            infoFrame = LabelFrame(nfe_master, width=120, height=80, bg=self.main_bg, bd=1)
            infoFrame.place(rely=0,relx=0.34, width=120, height=122)
            Label(infoFrame,text="N° NF-e", bg=self.main_bg, fg=self.main_fg, font=font).pack(anchor=W)
            self.lblNNf = Label(infoFrame,text="", bg=self.main_bg, fg=self.main_fg, font=font)
            self.lblNNf.pack(anchor=W)
            Label(infoFrame,text="Cd. NF-e", bg=self.main_bg, fg=self.main_fg, font=font).pack(anchor=W)
            self.lblCdNf = Label(infoFrame,text="", bg=self.main_bg, fg=self.main_fg, font=font)
            self.lblCdNf.pack(anchor=W)
            Label(infoFrame,text="Dt. Emis.", bg=self.main_bg, fg=self.main_fg, font=font).pack(anchor=W)
            self.lblDtEmi = Label(infoFrame,text="", bg=self.main_bg, fg=self.main_fg, font=font)
            self.lblDtEmi.pack(anchor=W)
            
            indFrame = LabelFrame(nfe_master, width=260, height=80, bg=self.main_bg, bd=1)
            indFrame.place(rely=0,relx=0.475, width=340, height=122)
            Label(indFrame,text="Chave de Acesso", bg=self.main_bg, fg=self.main_fg, font=font).pack(anchor=W)
            self.lblKeyAcess = Label(indFrame,text="", bg=self.main_bg, fg=self.main_fg, font=font)
            self.lblKeyAcess.pack(anchor=W)
            Label(indFrame,text="Valor dos Produtos", bg=self.main_bg, fg=self.main_fg, font=font).pack(anchor=W)
            self.lblVlProd = Label(indFrame,text="", bg=self.main_bg, fg=self.main_fg, font=font)
            self.lblVlProd.pack(anchor=W)
            Label(indFrame,text="Valor da Nota", bg=self.main_bg, fg=self.main_fg, font=font).pack(anchor=W)
            self.VlNf = Label(indFrame,text="", bg=self.main_bg, fg=self.main_fg, font=font)
            self.VlNf.pack(anchor=W)
            
            fatFrame = LabelFrame(nfe_master, text="Fatura ",width=260, height=80, bg=self.main_bg, bd=1)
            fatFrame.place(relx=0.05, rely=0.17, width=722, height=122)
        
        self.table2(master=master_widgets)
        labels(), entrys(), nfe()
        
    def searchProd(self, prod, manage=None):
        
        self.value_items["text"] = "0"
        self.value_MaxValue["text"] = "0,00"
        self.value_MinValue ["text"] = "0,00"
        self.tabela.delete(*self.tabela.get_children())
        self.count,self.max,self.min = 0,0,0
        def calc_info(value):
            value = float(self.Frmt(value))
            self.count +=1
            self.max = value if value > self.max else self.max
            if self.min == 0: self.min = value
            elif value < self.min: self.min = value 
        if self.cb_descriptionVar.get():
            values = prod.split(" ")
            def check_and(keys,words):
                for key in keys:
                    if key.lower() not in words.lower():
                        return False
                return True
            for i in self.produtos:
                xProd = i["xProd"]
                if check_and(keys=values, words=xProd):
                    self.tabela.insert("",END,values=list(i.values()))
                    calc_info(i["vUnCom"])                    
        elif manage == "NNFe":
            for i in self.produtos:
                if prod == i["nNF"]:
                    self.tabela.insert("",END,values=list(i.values()))
                    calc_info(i["vUnCom"])
        
        else:
            for i in self.produtos:
                if (prod.lower() in str(i["xProd"]).lower()) or (prod in str(i["cEAN"])):
                    self.tabela.insert("",END,values=list(i.values()))
                    calc_info(i["vUnCom"])
        self.value_items["text"], self.value_MaxValue["text"], self.value_MinValue ["text"] = self.count, self.max, self.min
                    
    def sorcheNFe(self,key_nfe):
        try: self.tabela.delete(*self.tabela.get_children())
        except Exception: pass
        not_s = True
        for index,NFe in enumerate(self.list_nfe):
            
            if key_nfe in NFe["nNF"]:
                not_s = False
                self.searchProd(prod=NFe["nNFe"],manage="NNFe")
            elif ((index + 1) == len(self.list_nfe)) and not_s:
                messagebox.showinfo("Sem Registro", "Chave de acesso não encontrada no banco de dados")
    
    def get_key(self,event):
        if not event.widget.get():
            event.widget.tk_focusNext().focus()
        elif event.widget in (self.prodDescription, self.entry_nnfe, self.entry_keynfe):
            pyperclip.copy(event.widget.get())
            if event.widget == self.prodDescription :
                self.searchProd(event.widget.get())
                self.prodDescription.delete(0,END)
                
            elif self.entry_nnfe.get() and (event.widget == self.entry_nnfe):
                self.searchProd(prod=self.entry_nnfe.get(), manage="NNFe")
                self.entry_nnfe.delete(0,END)
            elif self.entry_keynfe.get() and (event.widget == self.entry_keynfe):
                if len(self.entry_keynfe.get()) == 44:
                    self.sorcheNFe(key_nfe=self.entry_keynfe.get())
                    self.entry_keynfe.delete(0,END)
                else: messagebox.showerror("Chave Inválida", "CHAVE INVÁLIDA\n Verifique o codigo e tente novamente.")
                self.entry_nnfe.delete(0,END)
           
                  # Mudar o foco para o segundo campo de entrada
        elif event.widget in (self.entry_Nnf, self.entry_Cnf, self.cbb_emitent, self.entry_KeyAcess):
            pyperclip.copy(event.widget.get())
            if event.widget.get():
                value = event.widget.get()
                if event.widget == self.entry_Nnf: 
                    self.entry_Nnf.delete(0,END)
                    key = "nNFe"
                elif event.widget == self.entry_Cnf: 
                    self.entry_Cnf.delete(0,END)
                    key = "cNFe"
                elif event.widget == self.cbb_emitent: key = "emitente"
                else: 
                    self.entry_KeyAcess.delete(0,END)
                    key = "nNF"
                self.InsertOnTable2(keyAgr=value,key=key)
    
    def get_info(self,file_name):
        arquivo = f"NFE\{file_name}"
        with open(arquivo,"rb") as xml:
            dict_xml = xmltodict.parse(xml)
        try:
            return self._extracted_from_get_info_6(dict_xml)
        except Exception as ERROR:
            print(ERROR)

    def _extracted_from_get_info_6(self, dict_xml):
        if "NFe" in dict_xml:
            infos = dict_xml["NFe"]["infNFe"]
        elif "nfeProc" in dict_xml:
            infos = dict_xml["nfeProc"]["NFe"]["infNFe"]
        
        nNFe = (infos["@Id"]).replace("NFe","") if "NFe" in infos["@Id"] else infos["@Id"]
        cNFe = infos["ide"]["cNF"]
        nNFE = infos["ide"]["nNF"]
        natOp = infos["ide"]["natOp"]
        try:emitente = {"CNPJ|CPF":infos["emit"]["CNPJ"],"nome":infos["emit"]["xNome"]}
        except: emitente = {"CNPJ|CPF":infos["emit"]["CPF"],"nome":infos["emit"]["xNome"]}
        try:cliente = {"CNPJ|CPF":infos["dest"]["CNPJ"],"nome":infos["dest"]["xNome"]}
        except: cliente = {"CNPJ|CPF":infos["dest"]["CPF"],"nome":infos["dest"]["xNome"]}
        try:
            cobr = infos["cobr"] if "venda" in natOp.lower() else False
            dup = (cobr["dup"] if "dup" in cobr else False) if cobr else False
            fat = cobr["fat"] if cobr else cobr
        except Exception as error: 
            fat = infos["pag"]
            dup = 0
            print(infos.keys(), "\t", error,emitente, nNFe)
        vTotProd = infos["total"]["ICMSTot"]["vProd"]
        vTotNf = infos["total"]["ICMSTot"]["vNF"]
        vTotDesc = infos["total"]["ICMSTot"]["vDesc"]
        
        if "dhEmi" in infos["ide"]:
            dtEmissao = infos["ide"]["dhEmi"]
            dtEmissao  = (dtEmissao.split("T"))[0]
        else : dtEmissao  = 0
        nfe = {"emitente":emitente["nome"],"CNPJ|CPF":emitente["CNPJ|CPF"],"Cliente":cliente["nome"],"natOp":natOp, "dhEmi":dtEmissao,"nNFe":nNFE,"cNFe":cNFe,"nNF":nNFe,"vTotProd":vTotProd, "vNF":vTotNf,"fat":{"fat":fat,"dup":dup},"vTotDesc":vTotDesc}
        self.list_nfe.append(nfe)
        
        def add_prod(prod,icmsInclude,imposto):
            if "vDesc" in prod:
                desc = float(prod["vUnCom"]) * float(prod["qCom"])
                desc = desc - float(prod["vDesc"])
                desc = (round(desc / float(prod["qCom"]),2))
            else: desc = 0
            if icmsInclude: valueIcms = imposto["vTotTrib"] if "vTotTrib" in imposto else 0
            else: valueIcms = 0 
            NCM = prod["NCM"] if "NCM" in prod else "0"
            peso = "0.00"
            
            prod = {"cEAN":str(prod["cEAN"]),"xProd":prod["xProd"],"uCom":prod["uCom"],"vUnCom":self.Frmt(prod["vUnCom"]),"vDesc": self.Frmt(desc),"qntd":self.Frmt(prod["qCom"]),"uTrib":prod["uTrib"], "vUnTrib":self.Frmt(prod["vUnTrib"]), "qTrib":self.Frmt(prod["qTrib"]), "vProd":self.Frmt(prod["vProd"]),"icms":self.Frmt(valueIcms),"emitente":emitente["nome"], "dtEmissao":dtEmissao,"NCM":NCM,"nNF":nNFE,"cNF":cNFe}
            self.produtos.append(prod)
        
        def icms():
            self.totalNfe = infos["total"]
            valueIcms = self.totalNfe["ICMSTot"]
            try:In = True if (float(valueIcms["vProd"])+float(valueIcms["vOutro"]) ) < float(valueIcms["vNf"]) else None
            except: return False
            
        ICMS_IN = icms()
        prod = infos["det"]
        if type(prod) == list:
            for prod in prod:
                prod,imposto  = prod["prod"],prod["imposto"]
                add_prod(prod,ICMS_IN,imposto)
                
        elif type(prod) == dict:
            prod,imposto = infos["det"]["prod"], prod["imposto"]
            add_prod(prod, ICMS_IN,imposto)

        endereco = infos["dest"]["enderDest"]
        pesoBruto = "0.00"
        return {"nNFe":nNFe,"cNFe":cNFe,"nNF":nNFE,"emitente":emitente,"dtEmissao":dtEmissao,"cliente":cliente,"endereco":endereco,"pesoBruto":pesoBruto}
            #print(dict_xml)
            #print(json.dumps(dict_xml,indent=4))
        #valores.append([nNFe,cNFe,emitente["nome"],cliente["nome"],endereco["xLgr"]+" CEP:"+endereco["CEP"],pesoBruto])
    
    def open_xml(self,key):
        # !! Adicionar função que armazena em uma variavel a descrição do item após encontrado o EAN para busca em produtos com a mesma descrição mas sem GTIN
        # !! Adicionar função para busca de nota fiscal pela chave d acesso
        
        os.system(f'NFE\{key}')
        
    def calc(self,value,amount,cod):
        # print(list(i for i,c in enumerate(a) if c == "x"))     #exemplo para uso de generator
        try:
            value=float(value)
            amount=float(amount)
            cod =cod.lower()
            pProd = {"cod":"Porcentagem","un":{"pc":0.3,"frete":5},"loc":{"pc":0.45,"frete":0},"bbom":{"pc":0.4,"frete":0},"calcado":{"pc":0.5,"frete":0},"refri":{"pc":0.3,"frete":5},"iog":{"pc":0.35,"frete":5},"fd":{"pc":0.3,"frete":5},"cx":{"pc":0.3,"frete":5},"cong":{"pc":0.3,"frete":5},"tecido":{"pc":0.7,"frete":0},"fr":{"pc":0.5,"frete":0},"toalha":{"pc":0.5,"frete":0}}
            if cod not in pProd: return 0
            elif cod == "un":
                price=((value*amount)+ pProd[cod]["frete"]) + (((value*amount)+ pProd[cod]["frete"])*pProd[cod]["pc"])
            else:
                price = (value + pProd[cod]["frete"]) +((value+pProd[cod]["frete"])*pProd[cod]["pc"])
                        #print("Valor de Compra: ",(format((value/amount),".2f")))
            return price / amount        
        except Exception: return 0

if __name__ == "__main__":
    run=app()
    exit()        
