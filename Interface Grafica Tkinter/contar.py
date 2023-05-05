from tkinter import *
from tkinter import ttk
from fechamento import *
import openpyxl
import sqlite3
import datetime
def contarDinheiro():
    
    window = Tk()
    window.title("Contar Dinheiro")

    def grad():
        aie = 2
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
        grd5 = Label(window,text="",width=20)
        grd5.grid(column=4,row=5)
        grd6 = Label(window,text="",width=20)
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
        
    grad()
    
    fonte = "arial 12"
    
    lbl = Label(window,text="Contagem de Dinheiro",font="times 18 bold", width=20)
    lbl.grid(column=2,row=2)
    
    lbl1 = Label(window,text="Obs: Preencher com os valores  \ntotais somados de cada nota",font="arial 12", anchor=W, width=25,bd=1,relief="solid")
    lbl1.grid(column=1,row=4)
    lbl2 = Label(window,text="Notas de 200 / 100 / 50",font="arial 12", width=25,bg= "#ffff00",bd=1,anchor=W,relief="solid")
    lbl2.grid(column=1,row=5)
    lbl3 = Label(window,text="Notas de 20",bg= "#ffff00",font="arial 12", width=25,bd=1,anchor=W,relief="solid")
    lbl3.grid(column=1,row=6)
    lbl4 = Label(window,text="Notas de 10",font="arial 12",bg= "#ffff00", width=25,bd=1,anchor=W,relief="solid")
    lbl4.grid(column=1,row=7)
    lbl5 = Label(window,text="notas de 5",font="arial 12", width=25,bd=1,bg= "#ffff00",anchor=W,relief="solid")
    lbl5.grid(column=1,row=8)
    lbl6 = Label(window,text="Notas de 2",bg= "#ffff00",font="arial 12", width=25,bd=1,anchor=W,relief="solid")
    lbl6.grid(column=1,row=9)
    lbl7 = Label(window,text="Moedas",font="arial 12",bg= "#ffff00", width=25,bd=1,anchor=W,relief="solid")
    lbl7.grid(column=1,row=10)
    lbl8 = Label(window,text="total",font="arial 12", width=25,bd=1,bg= "#ffff00",anchor=W,relief="solid")
    lbl8.grid(column=1,row=11)
    
    
    tlbl2 = Entry(window,width=10,font=fonte)
    tlbl3 = Entry(window,width=10,font=fonte)
    tlbl4 = Entry(window,width=10,font=fonte)
    tlbl5 = Entry(window,width=10,font=fonte)
    tlbl6 = Entry(window,width=10,font=fonte)
    tlbl7 = Entry(window,width=10,font=fonte)
    
    tlbl2.grid(column=2,row=5)
    tlbl3.grid(column=2,row=6)
    tlbl4.grid(column=2,row=7)
    tlbl5.grid(column=2,row=8)
    tlbl6.grid(column=2,row=9)
    tlbl7.grid(column=2,row=10)

        
        
    
    
    def somar():
        
        
        if len(tlbl2.get()) > 0:
            v2 = float(tlbl2.get().replace(",","."))
        else:
            v2 = 0
        if len(tlbl3.get()) > 0:
            v3 = float(tlbl3.get().replace(",","."))
        else:
            v3 = 0
        if len(tlbl4.get()) > 0:
            v4 = float(tlbl4.get().replace(",","."))
        else:
            v4 = 0
        if len(tlbl5.get()) > 0:
            v5 = float(tlbl5.get().replace(",","."))
        else:
            v5 = 0
        if len(tlbl6.get()) > 0:
            v6 = float(tlbl6.get().replace(",","."))
        else:
            v6 = 0
        if len(tlbl7.get()) > 0:
            v7 = float(tlbl7.get().replace(",","."))
        else :
            v7 = 0
        
            
        vt = (v2+v3+v4+v5+v6+v7)
        tlbl8 = Label(window,text=f"{vt}",width=10,bg="#ffffff", background="#ffff00",font=fonte)
        tlbl8.grid(column=2,row=11)
    
    
        def importar():
            with open(r"c:\FLPrograms\tarde.txt","w") as vtarde:
                vtarde.write(str(vt))
            window.destroy()
            fechamento()
            

        btn1 = Button(window, text="Importar para Fechamento", width=20, bg="#4dc3ff", command=importar)
        btn1.grid(column=3,row=13)

        
    btn = Button(window,text="Confirmar",width=10 , bg="#4dc3ff" , command=somar)
    btn.grid(column=2,row=13)
    
  
    
    window.mainloop()


def relatorio():
    
    jnl = Tk()
    jnl.title("Relatorio")
    jnl.geometry("1200x600")
    jnl.state("zoomed")
    nb = ttk.Notebook(jnl)
    nb.place(x=0 , y=0 , width=1200 , height=600)
    
    tb1 = Frame(nb)
    tb2 = Frame(nb)
    tb3 = Frame(nb)
    
    nb.add(tb1, text="Inicio" )
    nb.add(tb2, text="Relatorio Mensal")
    nb.add(tb3, text="Relatorio Anual")
    
    with open (r"c:\FLPrograms\config.txt" , "r") as config:
        for linha in config:
            BancoDados = linha
    
    banco = sqlite3.connect(f"{BancoDados}")
    cursor = banco.cursor()
    
    
    #janela de relatorio inicio
    lbltitulo1 = Label(tb1,text="RELATORIO", font="times 18 bold")
    lbltitulo1.place(x=300 , y= 30)
    '''  
    diatual = datetime.datetime.now().day
    mesatual = datetime.datetime.now().month
    anoatual = datetime.datetime.now().year
        
    c.execute("SELECT dia FROM fechamento")
    datas = c.fetchall()
    d_mes_atual = 0
    for row4 in datas:
        if row4[0] != None:
            
            dia1 = row4[0][-10:2]
            dia  = int(dia1)
            mes1 = row4[0][-7:5]
            mes = int(mes1)
            anos = row4[0][-4:10]
            ano = int(anos)
            
           
            dt = datas.index(row4)
            
            
            
            if  mes == mesatual and ano == anoatual:
                
                c.execute("SELECT dinheiro FROM fechamento")
                l_dinheiro = c.fetchall()
                d_mes_atual += l_dinheiro[dt][0]
                
                c.execute("SELECT cartao FROM fechamento")
                l_card = c.fetchall()
                d_mes_atual += l_card[dt][0]
                
                c.execute("SELECT pix FROM fechamento")
                l_pix = c.fetchall()
                d_mes_atual += l_pix[dt][0]
    
     '''
    
    
    
    #janela 2, relatorio mensal
    lbltitulo2 = Label(tb2,text="RELATORIO MENSAL", font="times 18 bold")
    lbltitulo2.place(x=300 , y= 30)
    
    lista_meses = ["Janeiro" , "Fervereiro" , "Março" , "Abril" , "Maio" , "Junho" , "Julho" , "Agosto" , "Setembro" , "Outubro" , "Novembro" , "Dezembro"]
    datual = datetime.datetime.now()
    mesatual = datual.month
    diaatual = datual.day
    anoatual = datual.year
    indice_mes = mesatual - 1
    
    list_mes = ttk.Combobox(tb2, values=lista_meses)
    list_mes.set(lista_meses[indice_mes])
    list_mes.place(x=100 , y=67)
    
    
    
            
    
    
    
    cursor.execute("SELECT * FROM gastos")
    lista = cursor.fetchall()
    fonte = "arial 12"
    lista_anos = []
    for itens in lista:
        data = itens[1]
        ano = (data[-4:10])
        num = lista_anos.count(ano)
        if num == 0 :
            lista_anos.append(str(ano))
    
    lista_anos.sort()
    list_ano = ttk.Combobox(tb2, values=lista_anos , width=4)
    list_ano.set(anoatual)
    list_ano.place(x=245 , y=67)
    
    
    
    lblgSR = Label(tb2, text="GASTOS SEM RETORNO", font= "arial 12 bold")
    lblgSR.place(x=80 , y= 107)
    
    
    lstSR = Listbox(tb2)
    lstSR.place(x=50 , y= 130, width= 320)
    lstSR["font"] = fonte
    lstvSR = Listbox(tb2)
    lstvSR.place(x=350 , y= 130 , width=90)
    lstvSR["font"] = fonte
    
    
    
    lblgSR = Label(tb2, text="GASTOS COM RETORNO", font= "arial 12 bold")
    lblgSR.place(x=480 , y= 107)
    
    
    lstCR = Listbox(tb2)
    lstCR.place(x=450 , y= 130, width= 320)
    lstCR["font"] = fonte
    lstvCR = Listbox(tb2)
    lstvCR.place(x=750 , y= 130 , width=90)
    lstvCR["font"] = fonte
    
    
    totalsr = 0
    totalcr = 0
    
    for item in lista:
        
        
        if item[2] != None:
            data = item[1]
            dgastosSR = item[2]
            vgastosSR = item[3] 
            totalsr +=vgastosSR
            
            lstSR.insert(END, str(data) + " | " + str(dgastosSR) + "." * 50)
            lstvSR.insert(END, vgastosSR)
        
        
        if item[4] != None:
                
            dgastosCR = item[4]
            vgastosCR = item[5] 
            totalcr +=vgastosCR
            
            
            lstCR.insert(END, str(data) + " | " + str(dgastosCR) + "." * 50)
            lstvCR.insert(END, vgastosCR)
    
    lstSR.insert(END, "TOTAL" + "." * 80)
    lstvSR.insert(END, totalsr)
    lstCR.insert(END, "TOTAL" + "." * 80)
    lstvCR.insert(END, totalcr)
        
        
    def atualizar():
        
            
        lstSR.delete(0,END)
        lstCR.delete(0,END)
        lstvSR.delete(0,END)
        lstvCR.delete(0,END)
        
        cursor.execute("SELECT * FROM gastos")
        lista = cursor.fetchall()
        
        
        nmes = "0" + str(lista_meses.index(list_mes.get()) + 1) if lista_meses.index(list_mes.get()) < 9 else str(lista_meses.index(list_mes.get()) + 1)
        print(nmes)
        totalsr = 0
        totalcr = 0
        
        for item in lista:
            
            data = item[1]
            dia = (data[:2])
            mes = (data[-7:5])
            ano = (data[-4:10])
            
            list_mes.get()
            lista_meses
            
            if nmes == mes and list_ano.get() == ano:
            
                if item[2] != None:
                    
                    dgastosSR = item[2]
                    vgastosSR = item[3] 
                    totalsr +=vgastosSR
                    
                    lstSR.insert(END, str(data) + " | " + str(dgastosSR) + "." * 50)
                    lstvSR.insert(END, vgastosSR)
                
                
                if item[4] != None:
                        
                    dgastosCR = item[4]
                    vgastosCR = item[5] 
                    totalcr +=vgastosCR
                    
                    
                    lstCR.insert(END, str(data) + " | " + str(dgastosCR) + "." * 50)
                    lstvCR.insert(END, vgastosCR)
            
        lstSR.insert(END, "TOTAL" + "." * 80)
        lstvSR.insert(END, totalsr)
        lstCR.insert(END, "TOTAL" + "." * 80)
        lstvCR.insert(END, totalcr)

        btnimprimir = Button(tb2,text="IMPRIMIR" ,bg="#4dc3ff", font="arial 10")
        btnimprimir.place(x=100 , y=400)
    
    
    btnatualizar = Button(tb2, text="Atualizar", font="arial 8" ,bg="#4dc3ff", command=atualizar)
    btnatualizar.place(x=295 , y=65)
    
    
    
    
    #janela 3 relatorio anoal
    lbltitulo3 = Label(tb3,text="RELATORIO ANUAL", font="times 18 bold")
    lbltitulo3.place(x=300 , y= 30)
    
    
    
        
    
    
    jnl.mainloop()
    
relatorio()
