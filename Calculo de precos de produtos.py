import os

class start():
    def __init__(self):
        self.pProd = {"cod":"Porcentagem","und":{"pc":0.3,"frete":5},"loc":{"pc":0.45,"frete":0},"bbom":{"pc":0.4,"frete":0},"calcado":{"pc":0.5,"frete":0},"refri":{"pc":0.3,"frete":5},"iog":{"pc":0.35,"frete":5},"fd":{"pc":0.3,"frete":5},"cx":{"pc":0.3,"frete":5},"cong":{"pc":0.3,"frete":5},"tecido":{"pc":0.7,"frete":0},"fr":{"pc":0.5,"frete":0},"toalha":{"pc":0.5,"frete":0}}

        Instruction = print("""
Bem vindo

Modo de uso: 
    ValorDeCompra Quantidade TipoDoProdruto
    Exemplo:
    12,00 5 und
    75.00 24 cx

exit  Fechar programa
list  Exibir codigos de tipo de produtos disponiveis
loop  Executar diversos calculos com a mesma porcentagem
calc  Executa calculos basicos
        exemplo: calc 5,54246575342468*365
    
""")

        self.helpLoop="""
loop TipoDoProduto  inicia LoopManeger atrinuindo 50% 
modo de uso:
    value amount

    value   valor de compra
    amount  quantidade de itens por caixa/fardo. Se nao informado sera calculado em unidade (1)

stop  Interromper LoopManager
exit  Interromper Programa
    
"""
        while True:
            prod = self.User().lower()
            if prod in ("sair","exit","close"): break
            elif prod == "list": self.List()
            elif prod == "clear": os.system("cls")
            elif prod[:7] == "command":os.system((prod.replace("command","")))
            elif prod[:4] == "calc": self.calculater((prod.replace("calc","")).replace(" ",""))
            elif prod[:4] == "loop":
                try:
                    if (prod.split(" "))[1] not in self.pProd:
                        print("Sintax incorreta ou codigo invalido\n")
                        print(self.helpLoop)
                    else:
                        self.loopManager((prod.split(" "))[1])
                except:
                    print("Sintax incorreta \n")
                    print(self.helpLoop)
            else:
                if len(prod.split(" ")) != 3: continue
                value,amount,cod = prod.split(" ")
                if not cod in self.pProd or cod == "cod":
                    print("Cod Not Found")
                    continue
                value,amount = value.replace(",","."),amount.replace(",",".")
                print(format(self.calc(value=(float(value)),amount=(float(amount)),cod=cod.lower()),".2f"))
                print("_"*50,"\n")
    def calc(self,value,amount,cod):
        if cod == "und":
            price=((value*amount)+ self.pProd[cod]["frete"]) + (((value*amount)+ self.pProd[cod]["frete"])*self.pProd[cod]["pc"])
            price = price / amount
        else:
            price = (value + self.pProd[cod]["frete"]) +((value+self.pProd[cod]["frete"])*self.pProd[cod]["pc"])
            price = price / amount
            print("Valor de Compra: ",(format((value/amount),".2f")))
        return price
        
    def loopManager(self,cod):
        cod=cod.lower()
        while True:
            value  = input("LoopManager\ >> ")
            if value.lower() == "stop": break
            elif value.lower() ==  "exit": exit()
            elif value.lower() == "help" : print(self.helpLoop)
            elif value.lower() == "clear": os.system("cls")
            else:
                value= value.replace(",",".")
                try :
                    value,amount=value.split(" ")
                    value = float(value)
                    amount=float(amount)
        
                except:
                    value=float(value)
                    amount=1
                if cod != "und":
                    vU = value/amount
                    print("Valor Unitario "+str(format(vU,".2f")))
                else:
                    value = value*amount
                    print("Valor Total "+str(format(value,".2f")))
                value += self.pProd[cod]["frete"]
                price = value + (value * self.pProd[cod]["pc"])
                price = price/amount
                print("Valor de venda "+str(format(price,".2f")))
                print("_"*50,"\n")

    def calculater(self,value):
        value=value.replace(",",".")
        operadores = ["/","*","-","+"]
        valueCalc = {}
        temp = ""
        for i in value:
            
            if (i not in operadores) and not (i.isalpha()):
                temp+=i
            elif i in operadores:
                valueCalc["value1"]=float(temp)
                valueCalc["operador"]=i
                temp=""
        valueCalc["value2"]=float(temp)
        if valueCalc["operador"]=="*": print(round((valueCalc["value1"]*valueCalc["value2"]),2))
        elif valueCalc["operador"]=="-": print(round((valueCalc["value1"]-valueCalc["value2"]),2))
        elif valueCalc["operador"]=="+": print(round((valueCalc["value1"]+valueCalc["value2"]),2))
        elif valueCalc["operador"]=="/": print(round((valueCalc["value1"]/valueCalc["value2"]),2))
        
                
    def User(self):
        return str(input(".: "))
    def List(self):
        for i in self.pProd :
            print(i,self.pProd[i])




if __name__ == "__main__":
    
    run = start()
    exit()
