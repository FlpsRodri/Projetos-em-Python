import xmltodict
import os
from tkinter import *
#import json
import sqlite3
class app():
    def __init__(self):
                 
        arquivos = os.listdir("NFE")
        arquivos = list(filter(lambda x : x[-3:] == "xml",arquivos ))
        colunas = ["Numero_Nota","Codigo_Nota","Emissor","Destinatario","Endereco_Dest","Peso Bruto"]
        valores = []
        self.produtos = []
        temp = []

        for index,xml in enumerate(arquivos):
            if index >= 0:
                self.get_info(xml,valores)
            else:
                break
            
        while True:
            prod = input(".:")
            if prod.lower() in [""," "] : continue
            elif prod.lower() == "exit":
                break
            elif prod.lower() == "clear all": 
                os.system("cls")
                continue
            s = 0
            os.system("cls")
            
            for index,i in enumerate(self.produtos):
                
                
                if prod in i["cEAN"] or (prod.lower() in (str(i["xProd"]).lower())) :
                    s += 1
                    print(i["xProd"],">> EAN:",i["cEAN"],"\t",(round(float(i["vUnCom"]),2)),"qntd",i["qntd"],"\n","Emitente",i["emitente"],"Data",i["dtEmissao"])
                    print("Valor de venda:",format(self.calc(value=i["vUnCom"],amount=i["qntd"],cod=i["uCom"]),".2f"))
                    #print(i)
                
                elif ((index+1) == len(self.produtos)) and (s==0):
                    print("Codigo EAN nao encontrado")
                else:
                    continue
    
    def main(self):
        self.root = Tk()
        self.root.config(bg="f543ac")
        self.root.title("Gerenciador de Produtos - FPrograms 1.0")
        self.root.mainloop()
        
    def get_info(self,arquivo,valores):  # sourcery skip: move-assign
        arquivo = f"NFE\{arquivo}"
        with open(arquivo,"rb") as xml:
            dict_xml = xmltodict.parse(xml)   
            try:
                if "NFe" in dict_xml:
                    infos = dict_xml["NFe"]["infNFe"]
                elif "nfeProc" in dict_xml:
                    infos = dict_xml["nfeProc"]["NFe"]["infNFe"]
                nNFe = infos["@Id"]
                cNFe = infos["ide"]["cNF"]
                #emitente = {"cnpj":infos["emit"]["CNPJ"],"nome":infos["emit"]["xNome"]}
                try:emitente = {"CNPJ|CPF":infos["emit"]["CNPJ"],"nome":infos["emit"]["xNome"]}
                except: emitente = {"CNPJ|CPF":infos["emit"]["CPF"],"nome":infos["emit"]["xNome"]}
                try:cliente = {"CNPJ|CPF":infos["dest"]["CNPJ"],"nome":infos["dest"]["xNome"]}
                except: cliente = {"CNPJ|CPF":infos["dest"]["CPF"],"nome":infos["dest"]["xNome"]}
                dtEmissao = infos["ide"]["dhEmi"]
                dtEmissao  = (dtEmissao.split(":"))[0]
                prod = infos["det"]
                if type(prod) == list:
                    for prod in prod:
                        
                        prod = prod["prod"]
                        prod = {"cEAN":prod["cEAN"],"dtEmissao":dtEmissao,"xProd":prod["xProd"],"vUnCom":prod["vUnCom"],"qntd":prod["qCom"],"uCom":prod["uCom"],"emitente":emitente["nome"]}
                        self.produtos.append(prod)
                
                elif type(prod) == dict:
                    prod = infos["det"]["prod"]
                    prod = {"cEAN":prod["cEAN"],"dtEmissao":dtEmissao,"xProd":prod["xProd"],"vUnCom":prod["vUnCom"],"qntd":prod["qCom"],"uCom":prod["uCom"],"emitente":emitente["nome"]}
                    self.produtos.append(prod)
                
                endereco = infos["dest"]["enderDest"]
                pesoBruto = "0.00"
            #print(json.dumps(dict_xml,indent=4))


            except Exception as ERROR:
                print(ERROR)
                #print(dict_xml)
                #print(json.dumps(dict_xml,indent=4))
            #valores.append([nNFe,cNFe,emitente["nome"],cliente["nome"],endereco["xLgr"]+" CEP:"+endereco["CEP"],pesoBruto])   
            return {"nNFe":nNFe,"cNFe":cNFe,"emitente":emitente,"dtEmissao":dtEmissao,"cliente":cliente,"endereco":endereco,"pesoBruto":pesoBruto}

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
    egar = """det": {
                        "@nItem": "1",
                        "prod": {
                            "cProd": "62",
                            "cEAN": "7898141930187",
                            "xProd": "OVO A  (360 OVOS)",
                            "NCM": "04072100",
                            "cBenef": null,
                            "CFOP": "5101",
                            "uCom": "CX",
                            "qCom": "25",
                            "vUnCom": "248",
                            "vProd": "6200.00",
                            "cEANTrib": "7898141930187",
                            "uTrib": "CX",
                            "qTrib": "25",
                            "vUnTrib": "248",
                            "indTot": "1",
                            "xPed": "324960",
                            "nItemPed": "1" """
                                            
if __name__ == "__main__":
    run=app()
    exit()        

