from tkinter import *
from tkinter import messagebox
import sqlite3
from win32api import ShellExecute
import win32print
import datetime




def fechamento():
    window = Tk()
    window.title("Fechamento de Caixa")   
    window.state("zoomed")
    
    def grad1():
        grd = Label(window,text="",width=20)
        grd.grid(column=0,row=0)
        grd1 = Label(window,text="",width=12)
        grd1.grid(column=1,row=1)
        grd2 = Label(window,text="",width=20)
        grd2.grid(column=2,row=2)
        grd3 = Label(window,text="",width=20)
        grd3.grid(column=3,row=3)
        grd4 = Label(window,text="",width=20)
        grd4.grid(column=4,row=4)
        grd5 = Label(window,text="",width=20,height=1)
        grd5.grid(column=4,row=5)
        grd6 = Label(window,text="",width=20,height=1)
        grd6.grid(column=4,row=6)
        grd7 = Label(window,text="",width=20)
        grd7.grid(column=4,row=7)
        grd8 = Label(window,text="",width=20)
        grd8.grid(column=4,row=8)
        grd9 = Label(window,text="",width=20)
        grd9.grid(column=4,row=9)
        grd10 = Label(window,text="",width=20)
        grd10.grid(column=4,row=10)
        grd11 = Label(window,text="",width=20)
        grd11.grid(column=4,row=11)
        grd412 = Label(window,text="",width=20)
        grd412.grid(column=4,row=12)
        grd413 = Label(window,text="",width=20)
        grd413.grid(column=4,row=13)
        grd414 = Label(window,text="",width=20)
        grd414.grid(column=4,row=14)
        grd415 = Label(window,text="",width=5,height=2)
        grd415.grid(column=5,row=15)

    grad1()    
    def voltar():
        from App import inicio
        window.destroy()
        inicio()
        
    
    
    btnvoltar = Button(window,text="Voltar", font="arial 10",bg="#bbb" , command=voltar)
    btnvoltar.grid(column=1,row=14)
    
    logo = Label(window,text="SUPERMERCADO HELY",font="times 18 bold")
    logo.grid(column=2,row=2)
    logo1 = Label(window,text="Fechamento de Caixa",font="times 15")
    logo1.grid(column=2,row=3)
    
    fonte = "arial 12"
    
    lblcx = Label(window,text="CX              ",font=fonte,width=8)
    lblcx.grid(column=1,row=4)
    lbcx = Entry(window,width=2, font=fonte)
    lbcx.grid(column=1,row=4)
    
    nmcaixa = Entry(window,width=20, bg="#ffffaa" , font=fonte)
    nmcaixa.grid(column=2,row=4)
    
    ldia = Label(window,text="Dia", width=20,bd = 1, relief = "solid", font=fonte, bg="#ffff00")
    ldia.grid(column=1,row=5)
    txtdia = Entry(window,width=20)
    txtdia.grid(column=2,row=5)
    txtdia["font"] = fonte
    
    datual = datetime.datetime.now()
    mesatual = datual.month
    diaatual = datual.day
    if mesatual < 10 and diaatual < 10 :
        txtdia.insert(0,'0' + str(datual.day) + "/" + '0' + str(datual.month) + "/" + str(datual.year) )
    elif mesatual < 10:
        txtdia.insert(0, str(datual.day) + "/" + '0' + str(datual.month) + "/" + str(datual.year) )
    elif diaatual < 10:
        txtdia.insert(0,'0' + str(datual.day) + "/" + str(datual.month) + "/" + str(datual.year) )
    else:
        txtdia.insert(0, str(datual.day) + "/" + str(datual.month) + "/" + str(datual.year) )
        
    dmanha = Label(window,text="Dinheiro da manhã",width=20 ,font=fonte,bd = 1, relief = "solid", bg="#ffff00")
    dmanha.grid(column=1,row=6)
    txtmanha = Entry(window,width=20)
    txtmanha.grid(column=2,row=6)
    txtmanha["font"] = fonte

    dtarde = Label(window,text="Dinheiro da Tarde", font=fonte, bd = 1, relief = "solid",width=20,bg="#ffff00")
    dtarde.grid(column=1, row=7)
    with open(r"c:\FLPrograms\tarde.txt",'r') as arquivo:
        for row in arquivo:

            valortarde = float(row)
            
    with open(r"c:\FLPrograms\tarde.txt","w") as arq:
        arq.write(str("0"))
        arq.close()
    if valortarde > 0 :
        txtarde1 = Label(window,text=f"{valortarde}",bd=1,anchor=W ,width=20, font=fonte, bg="#ffffff")
        txtarde1.grid(column=2,row=7)
    else:
        txttarde = Entry(window,width=20)
        txttarde.grid(column=2,row=7)
        txttarde["font"] = fonte

        
    supri = Label(window,text="Suprimento",width=20, font=fonte,bd = 1, relief = "solid", bg="#ffff00")
    supri.grid(column=1,row=8)
    txtsupri = Entry(window,width=20)
    txtsupri.grid(column=2,row=8)
    txtsupri["font"] = fonte
    
    card = Label(window,text="Cartão",width=20, font=fonte,bd = 1, relief = "solid", bg="#ffff00")
    card.grid(column=1,row=9)
    txtcard = Entry(window,width=20)
    txtcard["font"] = fonte
    txtcard.grid(column=2,row=9)
    
    apra = Label(window,text="A Prazo",width=20, font=fonte,bd = 1, relief = "solid", bg="#ffff00")
    apra.grid(column=1,row=10)
    txtapra = Entry(window,width=20)
    txtapra["font"] = fonte
    txtapra.grid(column=2,row=10)
    
    lpix = Label(window,text="Pix/ticket",width=20, bd = 1, relief = "solid",font=fonte, bg="#ffff00")
    lpix.grid(column=1,row=11)
    txtpix = Entry(window,width=20)
    txtpix["font"] = fonte
    txtpix.grid(column=2,row=11)
    
    sistem = Label(window,text="Saldo Total",width=20, bd = 1, relief = "solid",font=fonte, bg="#ffff00")
    sistem.grid(column=1,row=12)
    txtsistem = Entry(window,width=20)
    txtsistem["font"] = fonte
    txtsistem.grid(column=2,row=12)
    
    
    
    def calculo():
        
        
            
        a = txtdia.get()
        
        if len(txtmanha.get()) > 0 :
            b = float(txtmanha.get().replace(",","."))
        else:
            b = 0
        if valortarde > 0:
            c = valortarde
        elif len(txttarde.get()) > 0:
            c = float(txttarde.get().replace(",","."))
        else:
            c = 0
        if len(txtsupri.get()) > 0 :
            su = float(txtsupri.get().replace(",","."))
        else:
            su = 0
        bc = ((b + c) - su)
        if len(txtcard.get()) > 0 :
            d = float(txtcard.get().replace(",","."))
        else:
            d = 0
        if len(txtapra.get()) > 0 :
            e = float(txtapra.get().replace(",","."))
        else:
            e = 0
        if len(txtpix.get()) > 0 :
            f = float(txtpix.get().replace(",","."))
        else:
            f = 0
        if len(txtsistem.get()) > 0 :
            g = float(txtsistem.get().replace(",","."))
        else:
            g = 0
        
        cx = lbcx.get()
        nmcx = nmcaixa.get()
        bcf = (bc + d + e + f)
        bgs = (bcf - g)
        bg = format(bgs , '.2f')
        
        with open(r'c:\FLPrograms\fechamento impresso.txt','w') as arquivo:
                arquivo.write(str(f"""

 Caixa {cx}                 {nmcx}

 Data                {a}
 ______________________________
 Manha                   {b}
 Tarde                   {c}
 ______________________________
 Total                   {b + c}
 Suprimento            - {su}
 ______________________________
 Total                   {bc}
 Cartão                  {d}
 A Prazo                 {e}
 Pix / Ticket            {f}
 ______________________________
 Total                   {bcf}
 Sistema                 {g}
 ______________________________
 Saldo                   {bg}

 """))
        
        
        def guardar():
            
            confirm = messagebox.askyesno(title="Confirmar Envio", message="Confirmar e fechar fechamento de caixa")
            
            if confirm:
                
                dia = a 
                caixa = cx 
                dinheiro = bc 
                cartao = d 
                aprazo = e
                pix = f 

                bnco = sqlite3.connect("DBSupermercado hely.db")
                crs = bnco.cursor()
                
                crs.execute(f"INSERT INTO fechamento (dia,caixa, dinheiro, cartao, aprazo, pix) VALUES ('{dia}','{caixa}',{dinheiro},{cartao},{aprazo},{pix} )")
                bnco.commit()
                crs.close()
                        
                window.destroy()
            
        def imprimir():
            enviar = Button(window,text="Enviar", font=fonte , bg="#4dc3ff", width=15 , command=guardar)
            enviar.grid(column=2,row=15)

        
            with open(r"c:\FLPrograms\Impressora padrao.txt","r") as impressora:
                for valor in impressora:
                    print(valor)
            win32print.SetDefaultPrinter(valor)
            caminho = r"c:\FLPrograms"
            ShellExecute(0, "print" , "fechamento impresso.txt" ,  None , caminho , 0  )

                
                
        btnimprimir = Button(window,text="Imprimir",background="#808080" ,font=fonte, width=15 , command=imprimir)
        btnimprimir.grid(column=2,row=14)
        
        lin1 = Label(window, text=f"CX{cx} {nmcx}")
        lin1.grid(column=3,row=4)
        lin1["font"] = fonte
        lin11 = Label(window,text=f"{a}")
        lin11["font"] = fonte
        lin11.grid(column=4,row=4)
        
        
        lin2 = Label(window,text="Dinheiro da Manhã",font=fonte,bg = "#ffff00", width=20, bd=1, relief='solid',anchor=W )
        lin2.grid(column=3,row=5)
        lin3 = Label(window,text="Dinheiro da Tarde",font=fonte, width=20,bg = "#ffff00", bd=1, relief='solid',anchor=W )
        lin3.grid(column=3,row=6)
        lin4 = Label(window,text="Suprimento",bg = "#ffff00",font=fonte, width=20, bd=1, relief='solid',anchor=W )
        lin4.grid(column=3,row=8)
        lin5 = Label(window,text="Cartão",font=fonte, width=20,bg = "#ffff00", bd=1, relief='solid',anchor=W )
        lin5.grid(column=3,row=10)
        lin6 = Label(window,text="A Prazo",font=fonte, width=20, bd=1,bg = "#ffff00", relief='solid',anchor=W )
        lin6.grid(column=3,row=11)
        lin7 = Label(window,text="Pix ou Ticket",font=fonte, width=20, bd=1,bg = "#ffff00", relief='solid',anchor=W )
        lin7.grid(column=3,row=12)
        lin8 = Label(window,text="Sistema",font=fonte, width=20, bd=1, relief='solid',bg = "#ffff00",anchor=W )
        lin8.grid(column=3,row=14)
        lin9 = Label(window,text="Saldo Total",font=fonte, width=20, bd=1,bg = "#ffff00", relief='solid',anchor=W )
        lin9.grid(column=3,row=15)
        
        lin22 = Label(window,text=f"{b}",font=fonte, width=20, bd=1, relief='solid',bg = "#ffff00",anchor=E )
        lin22.grid(column=4,row=5)
        
            
        lin33 = Label(window,text=f"+  {c}",font=fonte, width=20, bd=1, relief='solid',bg = "#ffff00",anchor=E )
        lin33.grid(column=4,row=6)
        
        lin44 = Label(window,text=f"{b + c}",font=fonte, width=20, bd=2, relief='solid',anchor=E )
        lin44.grid(column=4,row=7)
        lin55 = Label(window,text=f"-  {su}",font=fonte, width=20, bd=1, relief='solid',bg = "#ffff00",anchor=E )
        lin55.grid(column=4,row=8)
        lin66 = Label(window,text=f"{bc}",font=fonte, width=20, bd=2, relief='solid',anchor=E )
        lin66.grid(column=4,row=9)
        lin77 = Label(window,text=f"{d}",font=fonte, width=20,bg = "#ffff00", bd=1, relief='solid',anchor=E )
        lin77.grid(column=4,row=10)
        lin88 = Label(window,text=f"{e}",font=fonte, width=20, bd=1,bg = "#ffff00", relief='solid',anchor=E )
        lin88.grid(column=4,row=11)
        lin99 = Label(window,text=f"+  {f}",font=fonte, width=20, bd=1,bg = "#ffff00", relief='solid',anchor=E )
        lin99.grid(column=4,row=12)
        lin91 = Label(window,text=f"{bcf}",font=fonte, width=20, bd=2, relief='solid',anchor=E )
        lin91.grid(column=4,row=13)
        lin81 = Label(window,text=f"-  {g}",font=fonte, width=20, bd=1,bg = "#ffff00", relief='solid',anchor=E )
        lin81.grid(column=4,row=14)
        if bcf > g :
        
            lin71 = Label(window,text=f"{bg}",font=fonte, width=20, bd=2,bg = "#00ff00", relief='solid',anchor=E )
            lin71.grid(column=4,row=15)
            
        elif bcf == g:
            lin71 = Label(window,text=f"{bg}",font=fonte, width=20, bd=2, relief='solid',anchor=E )
            lin71.grid(column=4,row=15)
            
        else:
            lin71 = Label(window,text=f"{bg}",font=fonte, width=20, bd=2,bg = "#ff0000", relief='solid',anchor=E )
            lin71.grid(column=4,row=15)
        
        
        
        
    
    
    botao = Button(window,text="Confirmar", command=calculo , width=15 ,bg="#4dc3ff", font=fonte )
    botao.grid(column=1,row=13)
    
    

    window.mainloop()
    
