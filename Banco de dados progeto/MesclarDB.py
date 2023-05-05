import sqlite3

while True:
    Input = input(">>> ")
    if Input.lower() == "exit" or Input.lower() == "stop" or Input.lower() == "break": break
    command = Input.lower().split(" to ")
    controle = len(command)
    
    if controle != 2 or command[1] == '':
        print ("Sintaxe do commando incorreta! \n")
        print("USO: origem to destino \n     origem  camino\Arquivo do Banco de dados inicial \n     destino  caminho\Arquivo que receberá as informacoes. \n")
        continue
    
    Intable = input("Tabela: ")
    if Intable == '' or Intable == None:
        print("Tabela Invalida. ")
        continue
    print(command[0])
    print(command[1])
    try:
        banco1 = sqlite3.connect(command[0])
    except:
        print("Erro ao carregar banco de dados origem")
        continue
    try:
        banco2 = sqlite3.connect(command[1])
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
    

