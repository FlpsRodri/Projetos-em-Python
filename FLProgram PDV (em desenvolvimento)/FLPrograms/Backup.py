import sqlite3
import time
def check_db(db):
    try:
        with open(db,"r"):
            return True
    except: return False

with open("Diretorios.config", "r") as directores:
    destinos = directores.read().split("\n")
destinos.remove("")
origem = input("IP origem >>")
destinos.remove(origem)
origem = "\\" + "\\" + origem + "\FLPrograms\DBSupermercado Hely.sql"
if check_db(origem):
    banco2 = sqlite3.connect(origem)
    cursor2 = banco2.cursor()
    cursor2.execute("SELECT dia, caixa, dinheiro, cartao, aprazo, pix FROM fechamento")
    DB2 = cursor2.fetchall()
else:
    print("Falha no banco de dados")
    quit()
for destiny in destinos:
    bank = "\\" + "\\" + destiny + "\FLPrograms\DBSupermercado Hely.sql"
    print(destiny)
    try:
        if check_db(bank):
            banco = sqlite3.connect(bank)
            cursor = banco.cursor()
        else: 
            print("Banco de dados > "+bank+" < offline")
            continue
    except:
        print("Erro ao carregar banco de dados origem")
        continue
    
    cursor.execute("SELECT dia, caixa, dinheiro, cartao, aprazo, pix FROM fechamento")
    DB1 = cursor.fetchall()
    for row in DB1:
        print(row)
        if row[0] == None and row[1] == None and row[2] == None:
            continue
        elif DB2.count(row) > 1:
            cursor2.execute(f"DELETE FROM fechamento WHERE dia == {row[0]} AND caixa = {row[1]} AND dinheiro = {row[2]} AND cartao = {row[3]} AND aprazo = {row[4]} AND pix = {row[5]}")
            banco2.commit()
            print("APAGADO......................")
        elif DB2.count(row) == 1:
            continue
        else:
            cursor2.execute(f"INSERT INTO fechamento(dia, caixa, dinheiro, cartao, aprazo, pix) VALUES ('{row[0]}', '{row[1]}', {row[2]}, {row[3]}, {row[4]}, {row[5]})")
            banco2.commit()
    print("*" * 100)
quit()