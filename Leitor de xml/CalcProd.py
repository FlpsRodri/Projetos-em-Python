import os

class CalcP():
    def __init__(self):
        self.pProd = {"cod":"Porcentagem","und":{"pc":0.3,"frete":5},"loc":{"pc":0.45,"frete":0},"bbom":{"pc":0.4,"frete":0},"calcado":{"pc":0.5,"frete":0},"refri":{"pc":0.3,"frete":5},"iog":{"pc":0.35,"frete":5},"fd":{"pc":0.3,"frete":5},"cx":{"pc":0.3,"frete":5},"cong":{"pc":0.3,"frete":5},"tecido":{"pc":0.7,"frete":0},"fr":{"pc":0.5,"frete":0},"toalha":{"pc":0.5,"frete":0}}

        
    def calc(self,value,amount,cod):
        pProd = {"cod":"Porcentagem","und":{"pc":0.3,"frete":5},"loc":{"pc":0.45,"frete":0},"bbom":{"pc":0.4,"frete":0},"calcado":{"pc":0.5,"frete":0},"refri":{"pc":0.3,"frete":5},"iog":{"pc":0.35,"frete":5},"fd":{"pc":0.3,"frete":5},"cx":{"pc":0.3,"frete":5},"cong":{"pc":0.3,"frete":5},"tecido":{"pc":0.7,"frete":0},"fr":{"pc":0.5,"frete":0},"toalha":{"pc":0.5,"frete":0}}
        if cod == "und":
            price=((value*amount)+ self.pProd[cod]["frete"]) + (((value*amount)+ self.pProd[cod]["frete"])*self.pProd[cod]["pc"])
            price = price / amount
        else:
            price = (value + self.pProd[cod]["frete"]) +((value+self.pProd[cod]["frete"])*self.pProd[cod]["pc"])
            price = price / amount
            print("Valor de Compra: ",(format((value/amount),".2f")))
        return price
     

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
        
    

