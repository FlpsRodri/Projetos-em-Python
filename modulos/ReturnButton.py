import tkinter as tk

# Função chamada quando o botão é clicado ou 'Enter' é pressionado
def handle_entry(event):
    if event.widget == entry1:  # Se o evento foi disparado pelo primeiro campo de entrada
        if not entry1.get():  # Se o primeiro campo de entrada estiver vazio
            entry2.focus()  # Mudar o foco para o segundo campo de entrada
        else:
            display_text(entry1.get())  # Exibir o texto do primeiro campo de entrada
    elif event.widget == entry2:  # Se o evento foi disparado pelo segundo campo de entrada
        if not entry2.get():  # Se o segundo campo de entrada estiver vazio
            entry1.focus()  # Mudar o foco para o primeiro campo de entrada
        else:
            display_text(entry2.get())  # Exibir o texto do segundo campo de entrada

def display_text(text):
    label_result.config(text="Texto inserido: " + text)

# Criar uma instância da classe Tk (janela principal)
root = tk.Tk()
root.title("Exemplo de Janela com Focus e Exibição")

# Criar rótulos e campos de entrada
label1 = tk.Label(root, text="Digite algo no campo 1 e pressione 'Enter':")
label1.pack(padx=20, pady=5)
entry1 = tk.Entry(root)
entry1.pack(padx=20, pady=5)

label2 = tk.Label(root, text="Digite algo no campo 2 e pressione 'Enter':")
label2.pack(padx=20, pady=5)
entry2 = tk.Entry(root)
entry2.pack(padx=20, pady=5)

# Criar um rótulo para exibir o resultado
label_result = tk.Label(root, text="")
label_result.pack()

# Vincular o evento de pressionar 'Enter' às duas entradas
entry1.bind("<Return>", handle_entry)
entry2.bind("<Return>", handle_entry)

# Iniciar o loop principal da interface gráfica
root.mainloop()
