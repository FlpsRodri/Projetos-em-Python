import xmltodict
import os
import pandas as pd

import json

def get_info(arquivo,valores):
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
            #produtos
            prod = infos["det"]
            if type(prod) == list:
                for prod in prod:
                    prod = prod["prod"]
                    prod = {"cEAN":prod["cEAN"],"xProd":prod["xProd"],"vUnCom":prod["vUnCom"],"uCom":prod["uCom"],"emitente":emitente["nome"]}
                    produtos.append(prod)
            
            elif type(prod) == dict:
                prod = infos["det"]["prod"]
                prod = {"cEAN":prod["cEAN"],"xProd":prod["xProd"],"vUnCom":prod["vUnCom"],"uCom":prod["uCom"],"emitente":emitente["nome"]}
                produtos.append(prod)
            
            endereco = infos["dest"]["enderDest"]
            if "vol" in infos["transp"]:
                pesoBruto = infos["transp"]["vol"]["pesoB"]
            else:
                pesoBruto = "0.00"
            #print(json.dumps(dict_xml,indent=4))


        except Exception as ERROR:
            print(ERROR)
            #print(dict_xml)
            print(json.dumps(dict_xml,indent=4))
        #valores.append([nNFe,cNFe,emitente["nome"],cliente["nome"],endereco["xLgr"]+" CEP:"+endereco["CEP"],pesoBruto])   
        return {"nNFe":nNFe,"cNFe":cNFe,"emitente":emitente,"cliente":cliente,"endereco":endereco,"pesoBruto":pesoBruto}
        
pegar = """det": {
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
                        
arquivos = os.listdir("NFE")
arquivos = list(filter(lambda x : x[-3:] == "xml",arquivos ))
colunas = ["Numero_Nota","Codigo_Nota","Emissor","Destinatario","Endereco_Dest","Peso Bruto"]
valores = []
produtos = []
temp = []
for index,xml in enumerate(arquivos):
    if index <= 2:
        get_info(xml,valores)
        
        for i in produtos: 
            print(i["xProd"],">> EAN:",i["cEAN"],"\t",(round(float(i["vUnCom"]),2)))
            
    else: 
        break
#tabela = pd.DataFrame(columns=colunas,data=valores)
#tabela.to_excel("Notas_Fiscais.xlsx",index=False)

#for i in valores: print(i,"\n")
    

