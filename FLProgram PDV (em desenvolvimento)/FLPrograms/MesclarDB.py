import sqlite3

def check_db(db):
    try:
        with open(db):
            return True
    except: return False
def Open(db,Table):
    if check_db(db) == False: print ("Banco de dados invalido")
    else:
        bnk = sqlite3.connect(db)
        cursor = bnk.cursor()
        cursor.execute(f"SELECT * FROM {Table}")
        values = cursor.fetchall()
        for value in values : 
            return print(value)

while True:
    Input = input(">>> ")
    if Input.lower() == "exit" or Input.lower() == "stop" or Input.lower() == "break": break
    elif Input.lower() == "self" : 
        table = input("Tabela: ")
        Open("c:\FLPrograms\DBSupermercado Hely.sql",str(table))
        continue
    command = Input.lower().split(" to ")
    controle = len(command)
    
    if controle != 2 or command[1] == '':
        print ("Sintaxe do commando incorreta! \n")
        print("USO: origem to destino \n     origem  camino completo\Arquivo do Banco de dados inicial \n     destino  caminho completo\Arquivo que receberá as informacoes. \n")
        continue
    
    Intable = input("Tabela: ")
    if Intable == '' or Intable == None:
        print("Tabela Invalida. ")
        continue
    elif command[1].lower() == "self" : 
        print("indo to self")
        Open(command[0],Intable)
        continue
    
    
    print(command[0])
    print(command[1])
    
    try:
        if check_db(command[0]):
            banco1 = sqlite3.connect(command[0])
        else: print("Banco de dados origen inválido")
    except:
        print("Erro ao carregar banco de dados origem")
        continue
        
    try:
        if check_db(command[1]) : 
            banco2 = sqlite3.connect(command[1])
        else: print("Banco de dados destino inválido")
    except:
        print("Erro ao carregar banco de dados destino")
        continue
    cursor1 = banco1.cursor()
    cursor2 = banco2.cursor()
    
    cursor1.execute(f"SELECT * FROM {Intable}")
    DB1 = cursor1.fetchall()
    cursor2.execute(f"SELECT * FROM {Intable}")
    DB2 = cursor2.fetchall()
    
    for row in DB1:
        print(row)
        if DB2.count(row) > 0 :
            pass
        else:
            cursor2.execute(f"INSERT INTO {Intable}(dia, caixa, dinheiro, cartao, aprazo, pix) VALUES ('{row[1]}', '{row[2]}', {row[3]}, {row[4]}, {row[5]}, {row[6]})")
            banco2.commit()
    