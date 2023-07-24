import xmltodict
import os
import pandas as pd

#import json

def get_info(arquivo,valores):
    arquivo = f"NFE\{arquivo}"
    with open(arquivo,"rb") as xml:
        dict_xml = xmltodict.parse(xml)
        try:
            if "NFe" in dict_xml:
                infos = dict_xml["NFe"]["infNFe"]
                cliente = {"CNPJ|CPF":infos["dest"]["CNPJ"],"nome":infos["dest"]["xNome"]}
            
            elif "nfeProc" in dict_xml:
                infos = dict_xml["nfeProc"]["NFe"]["infNFe"]
                cliente = {"CPNJ|CPF":infos["dest"]["CPF"],"nome":infos["dest"]["xNome"]}
            nNFe = infos["@Id"]
            cNFe = infos["ide"]["cNF"]
            emitente = {"cnpj":infos["emit"]["CNPJ"],"nome":infos["emit"]["xNome"]}
            endereco = infos["dest"]["enderDest"]
            if "vol" in infos["transp"]:
                pesoBruto = infos["transp"]["vol"]["pesoB"]
            else:
                pesoBruto = "0.00"
        except Exception as ERROR:
            print(ERROR)
            #print(json.dumps(dict_xml,indent=4))
        valores.append([nNFe,cNFe,emitente["nome"],cliente["nome"],endereco["xLgr"]+" CEP:"+endereco["CEP"],pesoBruto])   
        #return {"nNFe":nNFe,"cNFe":cNFe,"emitente":emitente,"cliente":cliente,"endereco":endereco,"pesoBruto":pesoBruto}
        
        
arquivos = os.listdir("NFE")
colunas = ["Numero_Nota","Codigo_Nota","Emissor","Destinatario","Endereco_Dest","Peso Bruto"]
valores = []
for xml in arquivos:
    get_info(xml,valores)
    #print(nfe,sep="\n")
    #print("\n")
    #if a == 1: break

tabela = pd.DataFrame(columns=colunas,data=valores)
tabela.to_excel("Notas_Fiscais.xlsx",index=False)

#for i in valores: print(i,"\n")
    
