import sqlite3
from tkinter import Tk,ttk, DoubleVar, X
import os
def check_db(db,ip=None):
    try:
        b = os.system("ping "+ip+" -n 1 >> teste.if")
        with open("teste.if","r") as teste:
            for row in teste:
                c = row[4:]
        if "Received = 1" or "Recebidos = 1" in c:
            with open(db,"r"):
                return True
        else: return False
    except: return False
#
with open("C:\FLPrograms\Read\Config\Texts\Config.config", "r") as direct:
    terminais = direct.read().split("\n")
terminais.remove("")

def ip():
    ip = []
    with open("c:\FLPrograms\Read\Config\Texts\Config.config", "r") as config:
        a = config.read().split("\n")
    a.remove("")
    for i in a:
        b = i.split("\\")
        #b.remove("")
        b = b[2] if len(b) == 5 else False
        if b != False: ip.append(b)
    return ip

ips = ip()
def update_db():
    jnl = Tk()
    jnl.geometry("300x30")
    jnl.resizable(0,0)
    jnl.wm_attributes('-alpha',0.7)
    jnl.overrideredirect(True)
    
    if check_db(r"DBSupermercado Hely.sql"):
        jnl.title("Carregando Banco de Dados")
        bnk = sqlite3.connect(r"DBSupermercado Hely.sql")
        cursor = bnk.cursor()
        
        for terminal in terminais:
            cursor.execute("SELECT dia,caixa,dinheiro,cartao,aprazo,pix FROM fechamento")
            bank_l = cursor.fetchall()
            jnl.title("Atualizando Terminal "+ str(terminais.index(terminal) + 1))
            var = DoubleVar()
            var.set(0)
                
            if check_db(terminal):
                banco = sqlite3.connect(terminal)
                crsr = banco.cursor()
                crsr.execute("SELECT dia, caixa, dinheiro, cartao, aprazo, pix FROM fechamento")
                bank_t = crsr.fetchall()
                pb = ttk.Progressbar(jnl,variable=var, maximum=len(bank_t))
                pb.pack(fill=X)
            
                l = []
                for i in bank_t:
                    if i[0] == None:continue
                    var.set(bank_t.index(i)+1)
                    jnl.update()
                    if l.count(i) < 1:
                        l.append(i)
                        if i in bank_l:
                            pass
                        else:
                            dia, caixa, dinheiro, cartao, aprazo, pix = i[0],i[1],i[2],i[3],i[4],i[5]
                            cursor.execute(f"INSERT INTO fechamento(dia, caixa, dinheiro, cartao, aprazo, pix) VALUES('{dia}','{caixa}',{dinheiro},{cartao},{aprazo},{pix}) ")
                            bnk.commit()
                pb.destroy()
        jnl.title("Concluido")
        jnl.destroy()
        jnl.mainloop()

update_db()