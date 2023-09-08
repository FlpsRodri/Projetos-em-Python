import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

def proximo_entry(event):
    event.widget.tk_focusNext().focus()
    return "break"

def inserir_valor_inicial(event):
    if not entry_preco_venda.get():
        entry_preco_venda.insert(0, "0,00")

# Criar uma janela principal
janela = tk.Tk()
janela.title("Interface com Abas")
janela.geometry("800x600")  # Tamanho fixo

# Definir a fonte "Consolas"
fonte_consolas = Font(family="Consolas", size=12)

# Criar o widget Notebook (guias)
notebook = ttk.Notebook(janela)

# Criar a primeira aba (Produtos)
aba_produtos = ttk.Frame(notebook)
notebook.add(aba_produtos, text="Produtos")

# Criar LabelFrame para "Produto"
frame_produto = ttk.LabelFrame(aba_produtos, text="Produto")
frame_produto.place(x=10, y=10, width=780, height=220)  # Usando o método place

# Adicionar Label e Entry para "Cod"
label_cod = tk.Label(frame_produto, text="Cod:")
label_cod.grid(row=0, column=0, sticky="w")

entry_cod = tk.Entry(frame_produto, width=13, font=fonte_consolas)
entry_cod.grid(row=1, column=0, padx=5, sticky="w")
entry_cod.bind("<Return>", proximo_entry)

# Adicionar Label e Entry para "Produto"
label_produto = tk.Label(frame_produto, text="Produto:")
label_produto.grid(row=0, column=1, sticky="w")

entry_produto = tk.Entry(frame_produto, width=70, font=fonte_consolas)  # Definir o tamanho máximo para 70 caracteres
entry_produto.grid(row=1, column=1, padx=5, sticky="w")
entry_produto.bind("<Return>", proximo_entry)

# Adicionar Label e Entry para "Preço Venda"
label_preco_venda = tk.Label(frame_produto, text="Preço Venda:")
label_preco_venda.grid(row=0, column=2, sticky="w")

entry_preco_venda = tk.Entry(frame_produto, width=12, justify="right", font=fonte_consolas)  # Alinhar à direita
entry_preco_venda.grid(row=1, column=2, padx=5, sticky="e")  # Alinhar à direita
entry_preco_venda.bind("<Return>", proximo_entry)
entry_preco_venda.bind("<FocusIn>", inserir_valor_inicial)  # Chamar a função ao focar

# Adicionar Label e Entry para "NCM"
label_ncm = tk.Label(frame_produto, text="NCM:")
label_ncm.grid(row=2, column=0, sticky="w")

entry_ncm = tk.Entry(frame_produto, width=12, font=fonte_consolas)
entry_ncm.grid(row=3, column=0, padx=5, sticky="w")
entry_ncm.bind("<Return>", proximo_entry)

# Adicionar Label e Entry para "Fornecedor"
label_fornecedor = tk.Label(frame_produto, text="Fornecedor:")
label_fornecedor.grid(row=2, column=1, sticky="w")

entry_fornecedor = tk.Entry(frame_produto, width=40, font=fonte_consolas)
entry_fornecedor.grid(row=3, column=1, padx=5, sticky="w")
entry_fornecedor.bind("<Return>", proximo_entry)

# Adicionar Label e Entry para "N° NF-e"
label_nfe = tk.Label(frame_produto, text="N° NF-e:")
label_nfe.grid(row=2, column=2, sticky="w")

entry_nfe = tk.Entry(frame_produto, width=12, font=fonte_consolas)
entry_nfe.grid(row=3, column=2, padx=5, sticky="w")
entry_nfe.bind("<Return>", proximo_entry)

# Criar LabelFrame para "Preço"
frame_preco = ttk.LabelFrame(aba_produtos, text="Preço")
frame_preco.place(x=10, y=240, width=780, height=340)  # Usando o método place

# Adicionar o widget Notebook à janela
notebook.pack(padx=10, pady=10, fill="both", expand=True)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
