import xmltodict
import os
from tkinter import *
#import sqlite3
from tkinter import ttk

class Table(object):
    def __init__(self):
        pass
        
    def window(self, master):
        
        def labels():
            Label(master, text="cod",font=self.main_font,bg=self.main_bg,fg=self.main_fg).place(relx=0.1,rely=0.1)
            Label(master, text="Descrição do produto",font=self.main_font,bg=self.main_bg,fg=self.main_fg).place(relx=0.25,rely=0.1)
            Label(master, text='Experimente utilizar o Filtro "AND"',font=self.main_font,bg=self.main_bg,fg="#ccf").place(relx=0.3,rely=0.17)
        
        
            
        def entrys():
            def filter(*args):
                value = self.variable_cod.get()
                kargs = "1234567890"
                temp = ""
                for i in value:
                    if i in kargs: temp += i
                self.variable_cod.set(temp)
            self.variable_cod = StringVar(master=master)
            self.variable_cod.trace("w",filter)
            self.codEan = Entry(master, bg="#F3FCA1", textvariable=self.variable_cod)
            self.prodDescription = Entry(master, bg="#F3FCA1", width=100)
            
            self.codEan.place(relx=0.1, rely=0.14)
            self.prodDescription.place(relx=0.25, rely=0.14)
            
            
        def table():
            colunas = ["EAN", "PRODUTO","CD", "V. UNIT", "V.DESC","QTD", "V. TOTAL", "ICMS", "FORNECEDOR", "DATA", "NCM", "N° NFE", "C. NFE"]
            columns_geo = {"EAN":[100], "PRODUTO":[300],"CD":[30], "V. UNIT":[60], "V.DESC":[60],"QTD":[40] ,"V. TOTAL":[90], "ICMS":[60], "FORNECEDOR":[200], "DATA":[100], "NCM":[100], "N° NFE":[100], "C. NFE":[100]}
            self.tabela = ttk.Treeview(master, columns=colunas, show="headings")
            
            for coluna in colunas:
                self.tabela.heading(coluna, text=coluna)
                tamanho = columns_geo[coluna][0]
                
                self.tabela.column(coluna, width=tamanho, minwidth=tamanho)
            
            self.tabela.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.6)
            
        labels()
        entrys()
        table()
        
    def config(self, master):
        self.main_bg = "#ffffff"
        self.main_fg = "#000000"
        self.main_geometry = {"height":"720","width":"1200"}
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
    
class app(Table):
    
    def __init__(self):
        
        arquivos = os.listdir("NFE")
        arquivos = list(filter(lambda x : x[-3:] == "xml",arquivos ))
        self.produtos = []
        
        for index,xml in enumerate(arquivos):
            if index >= 0:
                self.get_info(xml)
            else:
                break
        
        self.root = Tk()
        self.config(self.root)
        self.window(self.root)
        
        self.codEan.bind("<Return>",self.get_key)
        self.prodDescription.bind("<Return>",self.get_key)
        
        self.root.mainloop()
   
    def Frmt(self, num):
        num = float(num)
        return format(num,".2f")
    
    def sorcheProd(self, prod):
        try: self.tabela.delete(*self.tabela.get_children())
        except Exception as error: print(error)
        s = 0
        
        if "AND" in prod:
            values = prod.split(" AND ")
            def check_and(keys,words):
                for key in keys:
                    if key not in words.lower():
                        return False
                return True
            
            for index,i in enumerate(self.produtos):
                xProd = i["xProd"]
                if check_and(keys=values, words=xProd):
                    s += 1
                    self.tabela.insert("",END,values=list(i.values()))
        else:           
            for index,i in enumerate(self.produtos):
                if prod in i["cEAN"] or (prod.lower() in (str(i["xProd"]).lower())) :
                    s += 1
                    self.tabela.insert("",END,values=list(i.values()))
                
    def get_key(self,event):
        if event.widget:
            if self.codEan.get() and (event.widget == self.codEan):
                print(self.codEan.get())
                self.sorcheProd(self.codEan.get())
                self.codEan.delete(0,END)
            elif self.prodDescription.get() and (event.widget == self.prodDescription):
                print(self.prodDescription.get())
                self.sorcheProd(self.prodDescription.get())
                self.prodDescription.delete(0,END)
            else:
                event.widget.tk_focusNext().focus()  # Mudar o foco para o segundo campo de entrada
    
    def sorce_nfe(self,cd_type,cd_nfe):
        s = 0
        
        for index,i in enumerate(self.produtos):
                
            if cd_nfe == i[cd_type]:
                s += 1
                print(i["xProd"],">> EAN:",i["cEAN"],"\t",(round(float(i["vUnCom"]),2)),"  qntd",i["qntd"],"\n","Emitente",i["emitente"],"(cNFe",i["cNF"],"n.NFe",i["nNF"]+")","Data",i["dtEmissao"])
                print("Valor de venda:",format(self.calc(value=i["vUnCom"],amount=i["qntd"],cod=i["uCom"]),".2f"), f"V. Desconto {i['vDesc']}")
            
            elif ((index+1) == len(self.produtos)) and (s==0):
                print("Nota Fiscal nao encontrada")
            else:
                continue

    def get_info(self,arquivo):
        arquivo = f"NFE\{arquivo}"
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
        nNFe = infos["@Id"]
        cNFe = infos["ide"]["cNF"]
        nNFE = infos["ide"]["nNF"]
        try:emitente = {"CNPJ|CPF":infos["emit"]["CNPJ"],"nome":infos["emit"]["xNome"]}
        except: emitente = {"CNPJ|CPF":infos["emit"]["CPF"],"nome":infos["emit"]["xNome"]}
        try:cliente = {"CNPJ|CPF":infos["dest"]["CNPJ"],"nome":infos["dest"]["xNome"]}
        except: cliente = {"CNPJ|CPF":infos["dest"]["CPF"],"nome":infos["dest"]["xNome"]}
        if "dhEmi" in infos["ide"]:
            dtEmissao = infos["ide"]["dhEmi"]
            dtEmissao  = (dtEmissao.split("T"))[0]
        else : dtEmissao  = 0
        
        def fiter(self,value,type):
            temp = ""
            if type == "text":
                keyargs = "aàáâãbcçdeèéêfghiìíîjklmnoòóôõpqrstuùúûvwxyz"
                for i in value:
                    if i in keyargs: temp+=i
            elif type == "num":
                keyargs = "0123456789"
                for i in value:
                    if i in keyargs: temp+=i
            return temp
        
        def add_prod(prod,icmsInclude,imposto):
            if "vDesc" in prod:
                desc = float(prod["vUnCom"]) * float(prod["qCom"])
                desc = desc - float(prod["vDesc"])
                desc = (round(desc / float(prod["qCom"]),2))
            else: desc = 0
            if icmsInclude:
                valueIcms = imposto["vTotTrib"] if "vTotTrib" in imposto else 0
            else: valueIcms = 0 
            NCM = prod["NCM"] if "NCM" in prod else "0"
            #["EAN", "PRODUTO","CD", "V. UNIT", "V.DESC","QTD", "V. TOTAL", "ICMS", "FORNECEDOR", "DATA", "NCM", "N° NFE", "C. NFE"]
            prod = {"cEAN":str(prod["cEAN"]),"xProd":prod["xProd"],"uCom":prod["uCom"],"vUnCom":self.Frmt(prod["vUnCom"]),"vDesc": self.Frmt(desc),"qntd":prod["qCom"],"vProd":self.Frmt(prod["vProd"]),"icms":self.Frmt(valueIcms),"emitente":emitente["nome"], "dtEmissao":dtEmissao,"NCM":NCM,"nNF":nNFE,"cNF":cNFe}
            self.produtos.append(prod)
        
        def icms():
            self.totalNfe = infos["total"]
            valueIcms = self.totalNfe["ICMSTot"]
            try:
                if (float(valueIcms["vProd"])+float(valueIcms["vOutro"]) ) < float(valueIcms["vNf"]): return True
                else: return False
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
