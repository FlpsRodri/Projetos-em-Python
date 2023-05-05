#Combobox
from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Combo-Box)

listEsportes = ["Futebol","Volei","Basquete"]
lb_esportes = Label(app,text="Esportes").pack()

cb_esportes = ttk.Combobox(app,values=listEsportes).pack()
cb_esportes.set("Futebol")

#botao para imprimir selecionado

def imprimirEsporte():
	ve = cb_esporte.get()
	print("Esporte " + ve)

btn__esporte = Button(app,text="Esporte Selecionado", command=imprimirEsporte).pack()


app.mainloop()