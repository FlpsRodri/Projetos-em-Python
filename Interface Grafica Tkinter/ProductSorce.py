import requests
from bs4 import BeautifulSoup
import pprint


# from bs4 import BeautifulSoup

def buscar(Cod):
    def cest(NCM):
        link = "https: //cosmos.bluesoft.com.br/ncms/"+NCM
        cestReq = requests.get(link)
        if cestReq.status_code == 200:
            html = cestReq.text()
            soup = BeautifulSoup(html,"parser")

    headers = {
        'X-Cosmos-Token': 'XvIebuLVw5rh2I75PeJljw',
        'Content-Type': 'application/json',
        'User-Agent': 'Cosmos-API-Request'
    }

    req = requests.get(f'https://api.cosmos.bluesoft.com.br/gtins/{Cod}.json', headers=headers)
    print(req.status_code)
    if int(req.status_code) == 200:
        dic = req.json()
        #pprint.pprint(dic)
        try:
            print(dic["description"])
            print("gtin(EAN): ", dic["gtin"])
        except:
            try: pprint.pprint(dic)
            except: print("falha de operação")
            return
        try :
            print(dic["brand"]["name"])
            print("\n ncm: " + dic["ncm"]["code"])
        except KeyError:
            print("Sem Codigo Ncm")
        return

    elif req.status_code == 403 or req.status_code == 500:
        print("Servidor Indisponivel")
    else:
        print("Falha na requisição")


if __name__ == "__main__":
    while True:
        cod = input("Cod: ")
        if cod.lower() in ("exit", "quit", "sair"):
            quit()
        if len(cod) != 13: #len("7898926784042")
            print("codigo incorreto")
            #continue

        buscar(cod)
