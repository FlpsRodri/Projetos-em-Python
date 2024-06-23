from tkinter import *
from tkinter import ttk, messagebox
import keyboard
import sqlite3
import os

class FilterEntrance(object):
    numeros: str

    def __init__(self):
        self.numeros = "0123456789"
        self.alfabeto = "abcçdefghijklmnopqrstuv"
        self.acentos = "âãáàäéèêëíìîïóòõôöúùûü"
        self.carcEspeciais = "!@#$%¨&*()_-=+§{[ªº]}~/\\°?;:.>,<|"

        """
        uso:
        instanciando a classe
        Filter = FilterEntrance()
        atribuindo a uma variavel
        value = "abc1234def"
        var_only_num = Filter.onlyNum(value)
        var_only_alfa = Filter.onlyAlfa(value=value, acentos=True, caractEspec=True) # caso queira apenas caracters especiais especificos, passar em formato string: caractEspec = "#@+-/"
        """

    def onlyNun(self, value, maxWidth: int = None, crctEspec: str = None):
        listValues = self.numeros
        if crctEspec:
            listValues += crctEspec
        value = list(filter(lambda x: x in listValues, value))
        if maxWidth:
            value = value[:maxWidth]
        del listValues
        return "".join(value)

    def onlyAlfa(self, value: str, acentos: bool = False, caractEspec=None, maxWidth: int = None):
        listValues = self.alfabeto
        if acentos:
            listValues += self.acentos
        if caractEspec:
            if type(caractEspec) == bool:
                listValues += self.carcEspeciais
            else:
                listValues += caractEspec
        value = list(filter(lambda x: x in listValues, value))
        if maxWidth:
            value = value[:maxWidth]
        del listValues
        return "".join(value)


class sale_screen(object):
    def __init__(self, master):
        self.codePayVar = None
        self.valueVar = None
        self.itemVar = None
        self.qntVar = None
        self.codVar = None
        self.filter = FilterEntrance()
        self.tv = None
        master = Toplevel(master=master)
        master.focus_force()
        master.grab_set()
        master.geometry("800x600+10+20")
        master.resizable(False, False)
        top_frame = LabelFrame(master=master)
        top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.6)
        bottom_frame = LabelFrame(master=master)
        bottom_frame.place(relx=0, rely=0.6, relwidth=1, relheight=1)

        self.treeview(top_frame)
        self.entry(bottom_frame)
        self.labels(bottom_frame)
        self.buttons(bottom_frame)

    def treeview(self, master):
        def select(*args):
            item = self.tv.selection()[0]
            print(item)

        colunas = ["CDG", "QTD", "ITEM", "VALOR"]
        columns_geo = {"CDG": 100, "QTD": 60, "ITEM": 500, "VALOR": 100}
        self.tv = ttk.Treeview(master=master, columns=colunas, show="headings")
        self.tv.place(relx=0.02, rely=0, relheight=1, relwidth=0.96)
        self.tv.bind("<Double-Button-1>", select)
        self.tv.bind("<Return>", select)
        vs = Scrollbar(master=master, orient="vertical", command=self.tv.yview, width=15)
        # vs.place(rely=0.5, x=705, relheight=0.48)
        self.tv.configure(yscrollcommand=vs.set)
        for column in colunas:
            self.tv.heading(column, text=column)
            width = columns_geo[column]
            self.tv.column(column, width=width, minwidth=width)

    def buttons(self, master):
        def enter(*args):
            keyboard.press("space")

        def erase():
            pass

        y = 180
        font = "arial 12"
        lmp = Button(master, text="LIMPAR", bg="#ccc", font=font, command=erase)
        lmp.place(x=315, y=y)
        lmp.bind("<Return>", enter)
        cancel = Button(master, text="CANCELAR TUDO", fg="#e00", bg="#ccc", font=font, state=DISABLED)
        cancel.place(x=400, y=y)
        cancel.bind("<Return>", enter)
        fin = Button(master, text="FINALIZAR VENDA (V)", fg="#183E0C", bg="#cfc", font=font, state=DISABLED)
        fin.place(x=560, y=y)
        fin.bind("<Return>", enter)

    def labels(self, master):
        y = 125
        Label(master, text="R$ 0,00", width=12, height=2, bg="white", bd=1, relief=GROOVE, anchor=E,
              font="times 26 bold").place(x=523, y=20)
        Label(master, text="COD", anchor=W).place(x=40, y=y)
        Label(master, text="QUANT", anchor=W).place(x=150, y=y)
        Label(master, text="ITEM", anchor=W).place(x=260, y=y)
        Label(master, text="VALOR", anchor=W).place(x=640, y=y)
        Label(master, text="CODIGO DE PAGAMENTO", anchor=W).place(x=40, y=68)

    def entry(self, master: "frame tkinter"):
        def ast(*args):
            if self.codVar.get():
                self.qntVar.set(self.codVar.get())
                self.codVar.set("")

        def validate():
            pass

        def enter(value=None, defautValue=None):
            if value:
                if value != defautValue:
                    validate()
                else:
                    keyboard.press("tab")
            else:
                keyboard.press("tab")

        self.codVar = StringVar(value="")
        self.codVar.trace("w", lambda *args: self.codVar.set(str(self.filter.onlyNun(self.codVar.get(), maxWidth=20))))
        self.qntVar = StringVar(value="1")
        self.qntVar.trace("w", lambda *args: self.qntVar.set(str(self.filter.onlyNun(self.qntVar.get(), maxWidth=10))))
        self.itemVar = StringVar()
        self.valueVar = StringVar(value="0,00")
        self.valueVar.trace("w", lambda *args: self.qntVar.set(str(self.filter.onlyNun(self.valueVar.get(), maxWidth=10))))
        self.codePayVar = StringVar(value="")
        y = 150
        entry_cod = Entry(master, textvariable=self.codVar, width=15)
        entry_cod.place(x=40, y=y)
        entry_cod.focus()
        entry_cod.bind("<KeyPress-*>", ast)
        entry_cod.bind("<Return>", lambda *args: enter(entry_cod.get()))
        entry_qnt = Entry(master, textvariable=self.qntVar, width=15)
        entry_qnt.place(x=150, y=y)
        entry_qnt.bind("<Return>", lambda *args: enter(entry_qnt.get(), defautValue="1"))
        entry_item = Entry(master, textvariable=self.itemVar, width=60)
        entry_item.place(x=260, y=y)
        entry_item.bind("<Return>", lambda *args: enter(entry_item.get()))
        entry_value = Entry(master, textvariable=self.valueVar, width=15, justify=RIGHT)
        entry_value.place(x=640, y=y)
        entry_value.bind("<Return>", lambda *args: enter(entry_value.get(), defautValue="0,00"))
        entry_code_payment = Entry(master, textvariable=self.codePayVar, width=30)
        entry_code_payment.place(x=40, y=90)
        entry_code_payment.bind("<Return>", lambda
            *args: entry_cod.focus() if not entry_code_payment.get() else validate())


class client_screen(object):
    def __init__(self, master):
        master = Toplevel(master=master)
        master.geometry("800x600")
        master.resizable(False, False)
        master.focus_force()
        self.main_font = "consolas 12"
        self.main_bg = "White"
        self.frame_client = None
        self.frame_contato = None
        self.frame_ficha = None
        self.abas = None
        self.entry_cod = None
        self.entry_name = None
        self.entry_cpf = None
        self.entry_rg = None
        self.entry_org = None
        self.entry_dtN = None
        self.entry_nac = None
        self.entry_nat = None
        self.entry_pai = None
        self.entry_mae = None
        self.entry_cell = None
        self.entry_end = None
        self.entry_setor = None
        self.entry_cdd = None
        self.entry_uf = None
        self.entry_ava = None
        self.num_ava = None
        self.entry_obs = None
        self.tv = None

        self.tool_bar(master)
        self.buttons(master)
        self.entrys()
        self.labels()
        self.treeview(master=self.frame_ficha)

    def treeview(self, master):
        def select(*args):
            item = self.tv.selection()[0]
            print(item)

        colunas = ["DATA", "CODIGO", "STATUS", "PARCELAS", "VALOR"]
        columns_geo = {"DATA": 100, "CODIGO": 100, "STATUS": 100, "PARCELAS": 50, "VALOR": 100}
        self.tv = ttk.Treeview(master=master, columns=colunas, show="headings")
        self.tv.place(relx=0.02, rely=0, relheight=1, relwidth=0.96)
        self.tv.bind("<Double-Button-1>", select)
        self.tv.bind("<Return>", select)
        vs = Scrollbar(master=master, orient="vertical", command=self.tv.yview, width=15)
        # vs.place(rely=0.5, x=705, relheight=0.48)
        self.tv.configure(yscrollcommand=vs.set)
        for column in colunas:
            self.tv.heading(column, text=column)
            width = columns_geo[column]
            self.tv.column(column, width=width, minwidth=width)

    def buttons(self, master):
        bg = "#ccc"
        Button(master, text="Cadastrar Cliente", state=DISABLED, width=30, bg=bg).place(x=40, y=500)
        Button(master, text="Alterar", state=DISABLED, width=30, bg=bg).place(x=280, y=500)
        Button(master, text="Remover Cliente", state=DISABLED, width=30, bg=bg).place(x=40, y=530)
        Button(master, text="Definir taxas personalizadas", width=30, state=DISABLED, bg=bg).place(x=280, y=530)

    def labels(self):
        def label(x: int, y: int, master, text: str):
            bg = "#efefef"
            font = "arial 9"
            Label(master, text=text, bg=bg, font=font).place(x=x, y=y)

        # frame_client
        label(40, 29, self.frame_client, "COD")
        label(100, 29, self.frame_client, "NOME")
        label(40, 119, self.frame_client, "CPF")
        label(200, 119, self.frame_client, "RG")
        label(360, 119, self.frame_client, "ORGÃO EXP.")
        label(40, 179, self.frame_client, "NASCIMENTO")
        label(200, 179, self.frame_client, "NACIONALIDADE")
        label(400, 179, self.frame_client, "NATURALIDADE")
        label(40, 279, self.frame_client, "PAI")
        label(40, 329, self.frame_client, "MÃE")

        # frame_contato
        label(40, 29, self.frame_contato, "CELULAR")
        label(40, 79, self.frame_contato, "ENDEREÇO")
        label(40, 129, self.frame_contato, "BAIRRO")
        label(250, 129, self.frame_contato, "CIDADE")
        label(450, 129, self.frame_contato, "UF")
        label(40, 179, self.frame_contato, "AVALISTA")
        label(40, 229, self.frame_contato, "CEL. AVALISTA")
        label(40, 279, self.frame_contato, "OBSERVAÇÃO")

        # ficha de registro
        # debito em aberto
        # historico de pagamento

        pass

    def entrys(self):
        # frame_client

        self.entry_cod = Entry(self.frame_client, width=5, font=self.main_font, bg=self.main_bg)
        self.entry_cod.focus()
        self.entry_name = Entry(self.frame_client, width=60, font=self.main_font, bg=self.main_bg)
        self.entry_cpf = Entry(self.frame_client, width=15, font=self.main_font, bg=self.main_bg)
        self.entry_rg = Entry(self.frame_client, width=15, font=self.main_font, bg=self.main_bg)
        self.entry_org = Entry(self.frame_client, width=10, font=self.main_font, bg=self.main_bg)
        self.entry_dtN = Entry(self.frame_client, width=15, font=self.main_font, bg=self.main_bg)
        self.entry_nac = Entry(self.frame_client, width=20, font=self.main_font, bg=self.main_bg)
        self.entry_nat = Entry(self.frame_client, width=20, font=self.main_font, bg=self.main_bg)
        self.entry_pai = Entry(self.frame_client, width=60, font=self.main_font, bg=self.main_bg)
        self.entry_mae = Entry(self.frame_client, width=60, font=self.main_font, bg=self.main_bg)

        self.entry_cod.place(x=40, y=50)
        self.entry_name.place(x=100, y=50)
        self.entry_cpf.place(x=40, y=140)
        self.entry_rg.place(x=200, y=140)
        self.entry_org.place(x=360, y=140)
        self.entry_dtN.place(x=40, y=200)
        self.entry_nac.place(x=200, y=200)
        self.entry_nat.place(x=400, y=200)
        self.entry_pai.place(x=40, y=300)
        self.entry_mae.place(x=40, y=350)

        # frame_contao
        self.entry_cell = Entry(self.frame_contato, width=20, font=self.main_font, bg=self.main_bg)
        self.entry_end = Entry(self.frame_contato, width=60, font=self.main_font, bg=self.main_bg)
        self.entry_setor = Entry(self.frame_contato, width=20, font=self.main_font, bg=self.main_bg)
        self.entry_cdd = Entry(self.frame_contato, width=20, font=self.main_font, bg=self.main_bg)
        self.entry_uf = Entry(self.frame_contato, width=5, font=self.main_font, bg=self.main_bg)
        self.entry_ava = Entry(self.frame_contato, width=60, font=self.main_font, bg=self.main_bg)
        self.num_ava = Entry(self.frame_contato, width=20, font=self.main_font, bg=self.main_bg)
        self.entry_obs = Text(self.frame_contato, width=70, height=7, font=self.main_font, bg=self.main_bg, )

        self.entry_cell.place(x=40, y=50)
        self.entry_end.place(x=40, y=100)
        self.entry_setor.place(x=40, y=150)
        self.entry_cdd.place(x=250, y=150)
        self.entry_uf.place(x=450, y=150)
        self.entry_ava.place(x=40, y=200)
        self.num_ava.place(x=40, y=250)
        self.entry_obs.place(x=40, y=300)

    def tool_bar(self, master):
        self.abas = ttk.Notebook(master)
        self.frame_client = Frame(self.abas)
        self.frame_contato = Frame(self.abas)
        self.frame_contato.focus_force()
        self.frame_ficha = Frame(self.abas)
        self.abas.add(self.frame_client, text="CLINTE")
        self.abas.add(self.frame_contato, text="CONTATO")
        self.abas.add(self.frame_ficha, text="FICHA")
        self.abas.place(relx=0, rely=0, relwidth=1, relheight=0.8)


class history_screen(object):
    def __init__(self, master):
        master = Toplevel(master=master)
        master.geometry("800x600")
        master.resizable(FALSE, FALSE)
        master.focus_force()
        self.tv = None
        self.main_font = "arial 10"
        self.main_entry_bg = "white"
        self.entry_date1 = None
        self.entry_date2 = None
        self.ckb_open = None
        self.var_open = IntVar(master, value=1)
        self.ckb_expired = None
        self.var_expired = IntVar(master, value=1)
        self.ckb_paid = None
        self.var_paid = IntVar(master, value=0)
        self.main_menu(master=master)
        self.treeview(master)

    def treeview(self, master):
        def select(*args):
            item = self.tv.selection()[0]
            print(item)

        columns_geo = {"CLIENTE": 300, "VENCIMENTO": 100, "STATUS": 100, "PARCELA": 50, "VALOR": 100}
        self.tv = ttk.Treeview(master=master, columns=list(columns_geo.keys()), show="headings")
        self.tv.place(relx=0.02, rely=0.3, relheight=0.65, relwidth=0.9)
        self.tv.bind("<Double-Button-1>", select)
        self.tv.bind("<Return>", select)
        vs = Scrollbar(master=master, orient="vertical", command=self.tv.yview, width=20)
        vs.place(rely=0.3, x=740, relheight=0.65)
        self.tv.configure(yscrollcommand=vs.set)
        for column in columns_geo:
            self.tv.heading(column, text=column)
            width = columns_geo[column]
            self.tv.column(column, width=width, minwidth=width)

    def main_menu(self, master):
        master = LabelFrame(master=master, text="OPÇOES DE VIZUALIZAÇÃO")
        master.place(relx=0.02, rely=0.05, relwidth=0.9, relheight=0.23)

        self.entry_date1 = Entry(master, justify=RIGHT, width=15, font=self.main_font, bg=self.main_entry_bg)
        self.entry_date1.place(x=40, y=30)
        self.entry_date2 = Entry(master, justify=RIGHT, width=15, font=self.main_font, bg=self.main_entry_bg)
        self.entry_date2.place(x=200, y=30)

        def a():
            print(self.var_open.get())

        self.ckb_open = ttk.Checkbutton(master, text="EM ABERTO", variable=self.var_open, command=a)
        self.ckb_open.place(x=40, y=60)
        self.ckb_expired = ttk.Checkbutton(master, text="VENCIDOS", variable=self.var_expired, command=a)
        self.ckb_expired.place(x=180, y=60)
        self.ckb_paid = ttk.Checkbutton(master, text="QUITADOS", variable=self.var_paid, command=a)
        self.ckb_paid.place(x=320, y=60)

        total_frame = LabelFrame(master, text="TOTAL")
        total_frame.place(relx=0.6, rely=0, relwidth=0.4, relheight=0.9)
        Label(total_frame, text="EM ABERTO", font="consolas 10").place(x=10, y=10)
        Label(total_frame, text="PAGO", font="consolas 10").place(x=10, y=30)
        Label(total_frame, text="VENCIDO", font="consolas 10").place(x=10, y=50)


class config_screen(object):
    def __init__(self, master):
        master = Toplevel(master=master)
        master.geometry("800x600")
        master.focus_force()
        master.resizable(FALSE, FALSE)
        self.entry_name_fant = None
        self.entry_rz_social = None
        self.entry_cnpj = None
        self.entry_cntt = None
        self.entry_adress = None
        self.entry_inc_estadual = None
        self.frame_enterprise = LabelFrame(master=master, text="EMPRESA")
        self.frame_enterprise.place(relx=0.02, rely=0, relheight=0.4, relwidth=0.96)
        self.frame_buttons = Frame(master=master, bg="#ddd")
        self.frame_buttons.place(relx=0.02, rely=0.41, relwidth=0.96, relheight=0.55)

        self.labels()
        self.listBox(self.frame_buttons)
        self.entry(self.frame_enterprise)
        self.buttons(self.frame_buttons)

    def labels(self):
        font = "consolas 12"
        Label(self.frame_enterprise, text="NOME FANTASIA", font=font).place(x=30, y=10)
        Label(self.frame_enterprise, text="INSCRIÇÃO ESTADUAL", font=font).place(x=500, y=10)
        Label(self.frame_enterprise, text="RAZAO SOCIAL", font=font).place(x=30, y=60)
        Label(self.frame_enterprise, text="CNPJ", font=font).place(x=30, y=110)
        Label(self.frame_enterprise, text="CONTATO", font=font).place(x=200, y=110)
        Label(self.frame_enterprise, text="ENDEREÇO", font=font).place(x=30, y=160)
        Label(self.frame_enterprise, text="CODIGO DE PAGAMENTO", font=font).place(x=500, y=60)
        Label(self.frame_enterprise, text="CODIGO UNICO", font=font).place(x=500, y=110)
        Label(self.frame_enterprise, text="TERMINAL", font=font).place(x=500, y=160)
        Label(self.frame_buttons, text="TERMINAIS", width=44, bd=4, relief=GROOVE, font="arial 10").place(x=12, y=10)

    def entry(self, master):
        font = "times 11"
        self.entry_name_fant = Entry(master, font=font, width=55)
        self.entry_rz_social = Entry(master, font=font, width=55)
        self.entry_cnpj = Entry(master, font=font, width=20)
        self.entry_cntt = Entry(master, font=font, width=20)
        self.entry_adress = Entry(master, font=font, width=55)
        self.entry_inc_estadual = Entry(master, font=font, width=25)

        self.entry_name_fant.place(x=30, y=30)
        self.entry_rz_social.place(x=30, y=80)
        self.entry_cnpj.place(x=30, y=130)
        self.entry_cntt.place(x=200, y=130)
        self.entry_adress.place(x=30, y=180)
        self.entry_inc_estadual.place(x=500, y=30)

    def listBox(self, master):
        def list_term():
            print("ass")

        font = "consolas 12"
        self.lb = Listbox(master, height=12, width=40, font=font)
        self.lb.place(x=10, y=30)
        list_term_btn = Button(master, text="DEFINIR TERMINAIS", height=2, width=40, command=list_term)
        list_term_btn.place(x=400, y=30)
        self.lb["state"] = DISABLED

    def buttons(self, master):
        Button(master, text="CADASTRO DE FUNCIONÁRIOS", height=2, width=40).place(x=400, y=80)
        Button(master, text="DEFINIR JUROS E MULTAS", height=2, width=40).place(x=400, y=130)
        Button(master, text="SALVAR", height=2, width=40).place(x=400, y=180)


class login(object):
    def __init__(self):
        self.entry_key = None
        self.entry_user = None
        self.permission = None
        self.permission = BooleanVar(value=False)
        self.process = BooleanVar()

    def loginScreen(self, master):
        self.permission.set(value=False)
        master = Toplevel(master)
        master.bind("<Escape>", lambda *args: master.destroy())
        master.geometry("300x150+500+300")
        master.resizable(FALSE, FALSE)
        master.title("LOGIN")
        master.focus_force()
        master.overrideredirect(True)
        master.grab_set()
        bg = "#ddd"
        master.config(bg=bg)
        font = "consolas 11 bold"
        Label(master, text="USUARIO", bg=bg, font=font).place(x=30, y=40)
        Label(master, text="SENHA", bg=bg, font=font).place(x=150, y=40)
        self.entry_user = Entry(master, font=font, width=10)
        self.entry_user.place(x=30, y=60)
        self.entry_user.focus_force()
        self.entry_user.bind("<Return>", lambda *args: keyboard.press("Tab"))
        self.entry_key = Entry(master, font=font, width=10, show="*")
        self.entry_key.place(x=150, y=60)
        self.entry_key.bind("<Return>", lambda *args: self.login(master=master, user=self.entry_user.get().upper(),
                                                                 key=self.entry_key.get()))
        btnClose = Button(master=master, text="X", font="times 12 bold", fg="red", border=None, relief=GROOVE, width=2,
                          justify=RIGHT, command=lambda: master.destroy())
        btnClose.place(x=274, y=0)
        master.mainloop()
        return self.permission.get()

    def login(self, master, user: str, key: str):
        if True:
            # if key == self.usersAlowed.get(self.user, False):
            self.permission.set(True)
            master.destroy()
            self.lock(state=NORMAL)

        else:
            print("nannanao")

    def users(self):
        pass


class DataBase(object):
    def __init__(self, dataBaseName : str):
        self.dataBase = dataBaseName

    def connect(self):
        if self.checkDb(dataBaseName=self.dataBase):
            messagebox.showinfo(message="Conected")
        else:
            return False

    def CREATE(self):
        pass

    def checkDb(self, dataBaseName : str):
        try:
            with open(dataBaseName, "r") as db:
                return True
        except Exception as Error :
            message = "Banco de dados não encontrado\nSolicite assistência especializada \nDev: felipesgs@proton.me\n"+str(Error)
            messagebox.showerror(title="DATABASE ERROR", message=message)
            restore = messagebox.askokcancel(title="Assitência", message="Continuar para Restauração do Banco de dados")
            if restore:
                self.restoreDb()
            return False

    def restoreDb(self):
        print("restaurar?")
        pass

class app(login):

    def __init__(self):

        self.master = Tk()
        super().__init__()

        self.main_frame = Frame(self.master, bg="#999")
        self.main_frame.place(relwidth=1, relx=0, rely=0)

        self.title = None
        self.main_font = None
        self.main_bg = None
        self.main_fg = None
        self.main_geometry = None
        self.screenSet = None
        self.icon = None
        self.btn_cn = None
        self.btn_v = None
        self.btn_c = None
        self.btn_m = None
        self.btn_user = None

        self.db = DataBase(dataBaseName="DBteste.sql")
        if self.db.connect():
            self.main_config()
            self.hotkeys()
            self.buttons()
            self.loginScreen(self.master)
            self.master.mainloop()

        else: self.master.destroy()
    def buttons(self):
        def enter(*args):
            keyboard.press("space")

        self.master.bind("<Return>", enter)

        self.btn_user = Button(self.main_frame, text="USUÁRIO", height=5, width=20,
                               command=lambda: self.lock(state=DISABLED))
        self.btn_user.pack(side=LEFT, anchor=N)
        self.btn_v = Button(self.main_frame, text="NOVA VENDA", height=5, width=20, state=DISABLED,
                            command=lambda: sale_screen(master=self.master))
        self.btn_v.pack(side=LEFT, anchor=N)
        self.btn_c = Button(self.main_frame, text="CLIENTES", height=5, width=20, state=DISABLED,
                            command=lambda: client_screen(self.master))
        self.btn_c.pack(side=LEFT, anchor=N)
        self.btn_m = Button(self.main_frame, text="MOVIMENTO", height=5, width=20, state=DISABLED,
                            command=lambda: history_screen(self.master))
        self.btn_m.pack(side=LEFT, anchor=N)
        self.btn_cn = Button(self.main_frame, text="CONFIGURAÇÃO", height=5, width=20, state=DISABLED,
                             command=lambda: config_screen(self.master))
        self.btn_cn.pack(side=LEFT, anchor=N)

    def lock(self, state):
        self.btn_v["state"] = state
        self.btn_c["state"] = state
        self.btn_m["state"] = state
        self.btn_cn["state"] = state

        if state == DISABLED:
            self.loginScreen(self.master)

    def main_config(self):
        self.title = "Controle de vendas - LPprog"
        self.main_font = "consolas 12"
        self.main_bg = "#777"
        self.main_fg = "black"
        self.main_geometry = "800x600"
        self.screenSet = False
        self.icon = "Images\Comercio.ico"

        self.master.state("zoomed")
        self.master.title(self.title)
        self.master.geometry(self.main_geometry)
        self.master.config(bg=self.main_bg)
        self.master.wm_iconbitmap(self.icon)

    def hotkeys(self):
        def full_screen(*args):
            self.screenSet = False if self.screenSet is True else True
            self.master.attributes("-fullscreen", self.screenSet)

        self.master.bind("<KeyPress-F2>", lambda *args: sale_screen(self.master))
        self.master.bind("<KeyPress-F11>", full_screen)


if __name__ == '__main__':
    app()
