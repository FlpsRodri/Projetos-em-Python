import random
import sqlite3
from time import sleep

class Encript():
    def __init__(self):
        self.bank()
        self.check_db()
        self.listar()
        # caso a frase ou palavra sobreponha 18 caracteres, utilizar o modo multi
        text = input(".: ")
        #modo simple word
        if len(text) <=19: 
            cod = self.codificar(text)
            decod = self.decodificar(cod)
            print(cod)
            print(decod)
        # modo multi
        else:
            text = text.split(" ")
            a = ""
            b = ""
            for i in text:
                cod = self.codificar(i)
                a += cod
                decod = self.decodificar(cod)
                b += decod
            print(a)
            print(b)
            
    def codificar(self, key):
        try:
            key = key
            amount = len(key)
            if amount >=19:
                return "so long"
            var = ""
            for i in key:
                var += self.dict_cod[i]
            key = var[::len(key)] + str(amount)
            return key
        except: return False
    
    def decodificar(self, key):
        if key == False: return False
        try:
            if len(key) > 65 and len(key):
                amount = int(key[-2:])
                if amount >=19:
                    return "error, you cod are cracked"
            elif len(key) <= 65:
                amount = int(key[-1:])
        except:
            return "Fail, you cod are cracked "    
        key = key[:-1]
        all_key = ""
        lim = len(self.dict_cod["*"])
        all_amount = len(key) * int(amount)# + 1
        c = 0
        for i in range(0,all_amount):
            if (i % 64) == 0 and i > 0:
                all_key += "\n"
            if (i % amount) == 0:
                all_key += key[c]
                c += 1
            else:
                all_key += "*"
        all_key = all_key.split("\n")
        encripted = ""
        for i in all_key:
            a = []
            ind = 0
            for l in i:
                if l != "*": a.append((l,i.index(l)))
            for value in self.dict_cod.keys():
                key = self.dict_cod[value]
                e = True
                for l in a:
                    if l[0] == key[l[1]]:
                        pass
                    else: e = False
                if e == True:
                    encripted += value
                    #print(key, i, value)
        encripted = encripted[:amount]
        return encripted + " "
        
    def listar(self):
        self.cursor.execute("SELECT * FROM Codificacao")
        lista = self.cursor.fetchall()
        self.dict_cod = dict(lista)
          
    def check_db(self):
        self.bnk = sqlite3.connect("Hexadecimal.sql")
        self.cursor = self.bnk.cursor()
        #self.cursor.execute("SELECT * FROM Codificacao")
        #a = self.cursor.fetchall()
        #b = []
        #for i in a :
        #    print(i)
        #    if b.count(i) != 1: 
        #        b.append(i)
        #        print(">")
        #    else: print("serio mesmo? ")
        
    def bank(self):
        def check():
            try:
                with open("Hexadecimal.sql"):
                    return True
            except: return False
        if check(): return    
        self.bnk = sqlite3.connect("Hexadecimal.sql")
        self.cursor = self.bnk.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Codificacao(letra text, cod text)")
        self.bnk.commit()
        sleep(2)
        caracters = "0123456789abcdef" * 2
        caracters += caracters.upper() * 2
        caracters = list(caracters)
        num = "0123456789"
        vogais = "aáàãâäeéèêëiíìîïoóòôõöuúùûü"
        alfabet = "bcdfghjklmnpqrstvwxyz"
        specials = "!@#$%¨&*()_-+=§ª[]{}`º´^~:;?/°.,<>|\ "
        caracteres = num + vogais + alfabet + vogais.upper() + alfabet.upper() + specials
        lista_cod = []
        for i in caracteres :
            string = random.sample(caracters, k=64)
            cod = ""
            for it in string:
                cod += it
            lista_cod.append((i, cod))
        for i in lista_cod:
            self.cursor.execute("INSERT INTO Codificacao(letra, cod) VALUES('"+i[0]+"','"+i[1]+"')")
            self.bnk.commit()
        self.bnk.close()
        print("Concluido")
            
if __name__ == "__main__":
    start = Encript()    
