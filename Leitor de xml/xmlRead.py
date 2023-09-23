import xmltodict
import os
import json

list_xml = os.listdir("NFE")
def get_xml(file_name):
    arquivo = f"NFE\{file_name}"
    with open(arquivo,"rb") as xml:
        dict_xml = xmltodict.parse(xml)
    try: 
        info = dict_xml["nfeProc"]["NFe"]["infNFe"]
        emitente = info["emit"]["xNome"]
        
    except Exception:
        info = dict_xml["NFe"]["infNFe"]
        emitente = (dict_xml["NFe"]["infNFe"]["emit"])
    
    if True: #"BRF S.A" in emitente:
        for i in info["total"]["ICMSTot"]: print(i,info["total"]["ICMSTot"][i])
        print("\n")
        #print(json.dumps(dict_xml,indent=4))
        return
        if "venda" in info["ide"]["natOp"].lower():
            try: print(emitente, info["cobr"].keys())
            except Exception as error:
                print(json.dumps(dict_xml,indent=4))
                #print(info["total"].keys())
                print(error,"#"*10)
        else:print( emitente, info["ide"]["natOp"])
        #itens = info["det"]
        #item1 = itens[0]["prod"]
        #for item in itens:
        #    item = item["prod"]
        #    for i in item:
        #        print(i,"   ",item[i])
        #    print("\n")
        #print(dict_xml["nfeProc"]["NFe"]["infNFe"][])
    
        
    
for index,file_name in enumerate(list_xml):
    get_xml(file_name)
    if index == 1: break
    