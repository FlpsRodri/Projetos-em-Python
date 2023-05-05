import sqlite3
#from tkinter import *
#from tkinter import Tk,ttk,filedialog, Canvas
import time
#import keyboard
import os
#import docx
#from pathlib import Path



def a():
    with open(r"C:\FLPrograms\Read\Config\Texts\config.config","r") as red:
        lis = red.read().split("</>")
        a = lis[0].split("\n")
        a.remove("")
        b = lis[1].split("\n")
        b.remove("")

    for i in a: print(">>",i)
    print("="*70)
    for I in b: print(">>",I)
    print(len(a),len(b))

def b():
    try:
        with open("c:\FLPrograms\DBSupermercado Hely.sql","r") :
            return False
    except:
        return False

if b():
    B = Tk()
    B.geometry("300x300")
    vatualiza = DoubleVar()
    vatualiza.set(0)
    bp = ttk.Progressbar(B,variable=vatualiza, maximum=100)
    bp.place(x=0,y=100,width=300,height=40)
    
    bnk = sqlite3.connect("c:\FLPrograms\DBSupermercado hely.sql")
    c = bnk.cursor()
    c.execute("SELECT * FROM fechamento")
    tabela = c.fetchall()
    bkn = sqlite3.connect(r"c:\flprograms\read\dbsupermercado hely.sql")
    cu = bkn.cursor()
    cu.execute("SELECT * FROM fechamento")
    tabela2 = cu.fetchall()
    for i in tabela2:
        if i in tabela: continue
    else: 
        cu.execute(f"INSERT INTO fechamento VALUES {i}")        
        bkn.commit()
    B.mainloop()

def bank():
    bnk = sqlite3.connect("c:\FLPrograms\DBSupermercado Hely.sql")
    cr = bnk.cursor()
    cr.execute("CREATE TABLE IF NOT EXISTS fechamento(idcontrole integer primary key autoincrement ,dia text ,caixa text,  dinheiro float, cartao float, aprazo float , pix float) ")
    cr.execute("CREATE TABLE IF NOT EXISTS keys(idcontrole integer primary key autoincrement ,supervisor text,senha text) ")
    cr.execute("CREATE TABLE IF NOT EXISTS gastos(idcontrole integer primary key autoincrement ,dia text , gastosSemRetorno text ,valorSR float , gastosComRetorno text , valorCR float , funcionario text) ")
    bnk.commit()
    #user = ["helilton","511407"]
    #cr.execute("INSERT INTO gastos(dia, gastosSemRetorno, valorSR, gastosComRetorno, valorCR, funcionario)values('06/07/2022' , 'teste' , 0 , 'teste' , 0 , 'felipe')")
    bnk.commit()
    cr.execute("SELECT * FROM gastos")
    
def c():
    a = Tk()
    a.geometry("300x300")
    Bt = Button(a,text="",width=5,height=2,bg="#333",command=a.destroy)
    Bt.pack()
    a.mainloop()
#bank()

def janela():
    cd = Tk()
    cd.geometry("300x70")
    cd.title("CADASTRAR TERMINAIS")
    cd.resizable(0,0)
    inf = Label(cd,text="Informe a quantidades de teminais a serem cadastrados")
    inf.pack(side=TOP)
    eqt = Entry(cd,font="arial 12")
    eqt.pack(side=LEFT)
    bt = Button(cd,text="Buscar")
    bt.pack(side=LEFT)
    cd.mainloop()
def pgb():
    jnl = Tk()
    jnl.geometry("300x300")
    jnl.title("Atualizando Terminal 1")
    jnl.resizable(0,0)
    def d():
        c = [1,2,3,4,5,6,7,8,8]
        b = DoubleVar()
        b.set(0)
        e = 0
        a = ttk.Progressbar(jnl,variable=b, maximum=len(c))
        a.pack(fill=X)
        
        for i in c:
            e += 1
            time.sleep(0.5)
            b.set(e)
            jnl.update()
        a.destroy()
        b.set(0)
        jnl.update()
    bt = Button(jnl,command=d)
    bt.pack()
    jnl.mainloop()

#a = sqlite3.connect(r"c:\flprograms\dbsupermercado hely.sql")
#c = a.cursor()
#c.execute("SELECT idcontrole,dia, caixa, dinheiro, cartao, aprazo, pix FROM fechamento")
#bnk1 = c.fetchall()
#c.execute("SELECT * FROM fechamento")
#b = c.fetchall()
#print(bnk)

#print (1 if 1+2 > 2 else 2)
def g():
    x = 200
    a = 30  #2
    b = 70  #5
    c = 40  #10
    d = 500  #20
    e = 5600  #100/50
    s = 0
    #1
    if a + b + c == 200 : s = 201

    elif a + b == 100 and c > 0:
    #2
        if c > 100 :
            s = a + b + 102
    #3
        elif c < 100 and d > 0:
            if c + d > 100:
                g = int(d/20)
                d = 20
                for i in range(0,g):
                    if c + d == 100 :
                        s = a + b + c + d + 3
                        break
                    d +=20

    print(s)
    a = Tk()
    i = PhotoImage(file="image.gif")
    img = Label(text='', image=i)
    img.pack()
    print(i)
    a.mainloop()

#a = "felipe1"
#print(a.isalnum())


def movimento():
    
    a = Tk()
    a.geometry("500x500")
    x = 500
    y = 450
    while True:
        
        if x == -350 :
            x = 500
        
        lbl = Label(a,text="SUPERMERCADO HELY", font="arial 24 bold", fg="#000")
        lbl.place(x=x, y=y)
        a.update()
        time.sleep(0.05)
        lbl.destroy()
        x -= 5
    
    a.mainloop()

#os.startfile("c:\FLPrograms\Read\Config\Texts\Dbf.txt", "print")

def animation_window():
    a = Tk()
    
    def scan(event):
        time.sleep(0.01)
        a.destroy()
    a.geometry("400x400")
    canvas = LabelFrame(a, text="felipe", bd=2, font="arial 18")
    canvas.place(x=10, y=10)
    lb = Label(canvas,text="felipe")
    lb.pack()
    frame = Frame(a, width=100, height=100, bg="yellow")
    frame.pack()
    s = Button(frame, width=10, height=4, bg="red")
    s.place(x=0, y=0)
    a.update()
    a.wm_attributes('-toolwindow', 0)
    #a.wm_attributes('-disabled', True)
    
    a.wm_attributes('-alpha',1)
    #a.overrideredirect(True)
    #a.resizable(0,0)
    a.bind("<Key>", scan)
    x = 200
    try:
        while True:
            if x == -190:
                x = 400
            
            lbl = Label(a, text="Supermercado Hely", font="arial 12 bold")
            lbl.place(x=x, y=200)
            time.sleep(0.1)
            a.update()
            x -= 5
            lbl.destroy()
    except:pass
    a.mainloop()
#animation_window()

def tela_venda():
    main = Tk()
    main.geometry("800x600")
    #main.overrideredirect(True)
    main.state("zoomed")
    #self.main.wm_focusmodel(ACTIVE)
    bground = "#ff1510"
    main["bg"] = bground
    bg = "#ff5"
    #titulo
    base = Label(main, text="SUPERMERCADO HELY",bg=bground, fg="white", font="perpetua 50 bold")
    base.place(relx=0, rely=0.02, relwidth=1, relheight=0.1)
    #linha
    lin = Label(main, text="", bg="white", font="arial 2")
    lin.place(relx=0, rely=0.102, relwidth=1, relheight=0.01)
    #barra lateral
    frame_itm = Frame(main, bg=bg, bd=2, relief=RIDGE)
    frame_itm.place(relx=0, rely=0.15, relwidth=0.4, relheight=1)
    # barra horizontal inferior
    text = "SUPERMERCADO HELY"
    
    l = Label(frame_itm, text=text, font="times 13 bold",anchor=NW, justify=CENTER, height=20, width=55)
    l.grid(column=0, row=0)
    
    def produto():
        frame_prod = Frame(main, bg=bg, bd=2, relief=RIDGE)
        frame_prod.place(relx=0.4, rely=0.78, relwidth=1, relheight=1)
        frame_total = Frame(frame_prod, bg=bg, height=200)
        frame_total.pack(fill=X)
        frame_input = Frame(frame_prod,bg="gray20", height=900)
        frame_input.pack(fill=X)
        lbl_total = Label(frame_total, text="R$ 0,00",justify=RIGHT,bg=bg, font="times 40 bold")
        lbl_total.pack()
        
        Label(frame_input, text="", bg=bg, width=10).grid(column=0, row=0)
        lbl_cod = Label(frame_input, text="PRODUTO",width=10, font="arial 8 bold",bd=2, relief=SOLID, justify=LEFT)
        lbl_cod.grid(column=1, row=1)
        en_cod = Entry(frame_input,width=10, font="arial 10 bold", bd=2, relief=SOLID)
        en_cod.grid(column=1, row=2)
        lbl = Label(frame_input, text="", bg=bg, width=10)
        lbl.grid(column=3, row=0)
        lbl_qnt = Label(frame_input,width=10, text="QUANTIDADE", font="arial 8 bold", bd=2, relief=SOLID, justify=LEFT)
        lbl_qnt.grid(column=4, row=1)
        en_qnt = Entry(frame_input,width=10, font="arial 10 bold", bd=2, relief=SOLID)
        en_qnt.grid(column=4, row=2)
        main.mainloop()
    
#tela_venda()
def valida_entry():
    a = Tk()
    def scan(*args):
        d = b.get()
        if not d[-1] in ('1','2','3','4','5','6','7','8','9','0',','):
            b.set(d[:-1])
    b = StringVar()
    b.trace("w", scan)
    e = Frame(a, width=100, height=100)
    e.pack()
    f = Frame(e,width=100, height=100)
    f.pack()
    c = Entry(f, textvariable=b)
    c.grid(column=0, row=0)
    a.mainloop()

def check_db():
    bank = r"\\192.168.0.1\flprograms\DBSupermercado Hely.sql"
    with open(bank ,"r"):
        print("ok")

def corrigir_db():
    bnk = "\\\\192.168.0.1\FLPrograms\DBSupermercado Hely.sql"
    print(bnk)
    banco = sqlite3.connect(bnk)
    cursor = banco.cursor()
    cursor.execute("SELECT dia, caixa, dinheiro, cartao, aprazo, pix FROM fechamento")
    c = cursor.fetchall()
    a = []
    x = 0
    for row in c:
        if a.count(row) == 0:
            a.append(row)
        elif a.count(row) == 1:
            x += 1
            print(row, x)
            continue
    print(len(a))
#corrigir_db()

def type_entry():
    a = Tk()
    e = Entry(a, font="times 12")
    e.pack(anchor=CENTER)
    f = Entry(a, font="times 12")
    f.pack(anchor=CENTER)
    
    b = Button(a, text="somar", font="arial 12 bold", bg="#f34fd0", command= lambda:Label(a,text=format( float(e.get())  + float(f.get()), ".2f"), font="times 12").pack(anchor=CENTER))
    b.pack(anchor=CENTER)
    
    a.mainloop()

def pass_or_continue():
    for i in range(0,10):
        if i == 5:
            print("p ", i)
            pass
        else:
            print("c ", i)
            continue

def var():
    a, b, c, d = "felipe",2,3.5, 6
    print(d, c, b, a)
    
def Ping():
    a = time.time()
    b = os.system("ping 192.168.0.1 -n 1 >> teste.if")
    with open("teste.if","r") as teste:
        for row in teste:
            c = row[4:]
    if "Received = 0" or "Recebidos = 0" in c:
        print("perca total")
    print((time.time() - a) / 2)

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
def anagrama(key):
    a = key
    b = 1
    while a != 1:
        b = b * a
        a -= 1
    print(b, len(str(b)))

anagrama(86)