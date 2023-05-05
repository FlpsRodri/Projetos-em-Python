import tkinter
from tkinter import *
from tkinter import ttk
from datetime import timedelta

import keyboard


class funcionario(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Administrativo Funcionários")
        self.bg = "white"
        self.root.config(bg=self.bg)
        self.root.iconphoto(True, tkinter.PhotoImage(file="icones\IconeMain.png"))

        self.table()
        self.btns()
        self.keys()
        self.root.mainloop()

    def keys(self):
        keyboard.add_hotkey("esc", lambda:self.root.destroy())

    def onlyNum(self, value, diferent=None):
        numbers = "1234567890"
        if diferent != None:
            numbers += diferent
        value = str(value)
        val = ""
        for i in value:
            if i in numbers:
                val += i
        return val

    def calcExtras(self):
        self.FuncionariosList = ["FELIPE DOS SANTOS RODRIGUES"]
        app = Toplevel(self.root)
        app.geometry("800x600")
        app.title("Horas Extras")
        app.config(bg="#ccc")
        app.resizable(0,0)
        metadados = ["data", "Entrada(AM)", "Saida(AM)", "Entrada(PM)", "Saida(PM)","total", "Total por Dia"]
        self.table = ttk.Treeview(app, columns=("data", "Entrada(AM)", "Saida(AM)", "Entrada(PM)", "Saida(PM)","total", "Total por Dia"), show="headings", height=20)
        self.table.place(relx=0.055, rely=0.06)

        for column in metadados:
            self.table.column(column, minwidth=0, width=100)
            self.table.heading(column, text=column.upper())

        self.dadosTable = []

        def inserir():
            def calcTate(time1, time2):
                time1 = self.onlyNum(time1)
                time2 = self.onlyNum(time2)

            data = self.dataE.get()
            entrm = self.entradaM.get()
            saidm = self.saidaM.get()
            entrt = self.entradaT.get()
            saidt = self.saidaT.get()
            totalPdia = calcDate(calcDate(),calcDate())
            total
            self.dadosTable.append({"data": data,
                                    "entrM": entrm,
                                    "saidM": saidm,
                                    "entrT": entrt,
                                    "saidT": saidt,
                                    "totalPdia": totalPdia,
                                    "total": total})

            "data", "Entrada(AM)", "Saida(AM)", "Entrada(PM)", "Saida(PM)", "total", "Total por Dia"
        def dell():
             for i in itens:
                 self.table.delete(i)
        Button(app, text="aperte", command=dell).place(relx=0.5,rely=0.9)

        fonte = "roboto 9"

        funcionario = ttk.Combobox(app, values=self.FuncionariosList, width=80)
        funcionario.place(relx=0.055, rely=0.01)
        funcionario.focus()

        def label(y,x,text="",width=None):
            if width != None : return Label(app, text=text,width=width, bd=1, relief=SUNKEN, bg=self.bg, font=fonte ).place(relx=x, rely=y)
            else: return Label(app, text=text, bd=1, relief=SUNKEN, bg=self.bg, font="roboto 9" ).place(relx=x, rely=y)

        def dataFilter(*args):
            value = self.onlyNum(self.dEmissaoVar.get())
            if len(value) > 8:
                val = self.dEmissaoVar.get()
                self.dEmissaoVar.set(val[:8])
                value = value[:8]
            ind = 0
            self.dEmissao.delete(0, END)
            for i in value:
                if ind == 2 or ind == 4:
                    self.dEmissao.insert(END, "/")
                    self.dEmissao.insert(END, i)
                else:
                    self.dEmissao.insert(END, i)
                ind += 1

        label(0.8, 0.05, "DATA", 15)
        label(0.8, 0.18, "ENTRADA", 15)
        label(0.8, 0.31, "SAIDA", 15)
        label(0.8, 0.44, "Entrada", 15)
        label(0.8,0.57, "SAIDA", 15)
        label(0.8, 0.7, "Total Dia", 15)
        label(0.8, 0.83, "TOTAL", 15)

        dataVar = StringVar()
        entradaMVar = StringVar()
        saidaMVar = StringVar()
        entradaTVar = StringVar()
        saidaTVar = StringVar()
        self.dataE = Entry(app, width=15, font=fonte)
        self.dataE.place(rely=0.833 , relx=0.05 )
        self.entradaM = Entry(app, width=15, font=fonte)
        self.entradaM.place(rely=0.833 , relx=0.18 )
        self.saidaM = Entry(app, width=15, font=fonte)
        self.saidaM.place(rely=0.833 , relx=0.31 )
        self.entradaT = Entry(app, width=15, font=fonte)
        self.entradaT.place(rely=0.833 , relx=0.44 )
        self.saidaT = Entry(app, width=15, font=fonte)
        self.saidaT.place(rely=0.833 , relx=0.57 )

        totalDia = Label(app, text="",width=15, bd=1, relief=SUNKEN, bg=self.bg, font=fonte)
        totalDia.place(relx=0.7, rely=0.833)
        totalValue = Label(app, text="",width=15, bd=1, relief=SUNKEN, bg=self.bg, font=fonte )
        totalValue.place(relx=0.83, rely=0.833)


    def btns(self):
        btn_extrasTime = Button(self.root, text="Horas Extras", command=self.calcExtras)
        btn_extrasTime.pack(side=RIGHT, anchor=N)
        btn_extrasTime.focus()





if __name__ == "__main__": funcionario()