import time
inicio = time.time()
with open(r"\\192.168.0.1\Sansoft2020\Text.txt","w") as text:
    text.write("teste de criação de arquivo na rede")
meio = time.time()-inicio
with open(r"\\192.168.0.1\Sansoft2020\Text.txt","r") as txt:
    for row in txt: print(row)
fim = time.time() - inicio

print( meio, fim)
