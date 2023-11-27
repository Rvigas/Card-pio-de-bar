import tkinter as tk
from tkinter import ttk, messagebox

# Dicionário para armazenar as escolhas do cliente
escolhas_cliente = {}

# Variável para rastrear se o cliente já fez um pedido
fez_primeiro_pedido = False

def exibir_boas_vindas(nome):
    global fez_primeiro_pedido
    mensagem = f"Seja bem-vindo, {nome}!"
    messagebox.showinfo("Boas-vindas", mensagem)

    resposta_idade = messagebox.askyesno("Verificação de Idade", "Você é maior de idade?")

    if resposta_idade:
        criar_janela_menu("Menu Alcoólico", {"Cervejas": ["Skol", "Brahma", "Antarctica", "Schin", "Itaipava", "Bohemia"],
                                             "Roscas": ["Morango", "Kiwi", "Abacaxi"],
                                             "Whiskys": ["Johnnie Walker Red Label", "Chivas Regal 12 Anos", "Jack Daniel's Old No. 7"],
                                             "Drinkys": []})
    else:
        criar_janela_menu("Menu sem Álcool", {"Drinks sem Álcool": ["Mojito", "Virgin Mary", "Smoothie"],
                                               "Roscas sem Álcool": ["Morango", "Kiwi", "Abacaxi"],
                                               "Sucos": [],
                                               "Refrigerantes": []})

def criar_janela_menu(titulo, opcoes):
    janela_menu = tk.Tk()
    janela_menu.title(titulo)
    janela_menu.geometry("600x400")  # Ajuste o tamanho conforme necessário

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10)

    for categoria, variedades in opcoes.items():
        botao_categoria = ttk.Button(janela_menu, text=categoria, command=lambda c=categoria, v=variedades: exibir_variedades(c, v))
        botao_categoria.pack(pady=10)

    janela_menu.mainloop()

def exibir_variedades(categoria, variedades):
    janela_variedades = tk.Tk()
    janela_variedades.title(categoria)
    janela_variedades.geometry("600x400")  # Ajuste o tamanho conforme necessário

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10)

    for variedade in variedades:
        botao_variedade = ttk.Button(janela_variedades, text=variedade, command=lambda v=variedade: exibir_quantidade(v))
        botao_variedade.pack(pady=10)

    janela_variedades.mainloop()

def exibir_quantidade(variedade):
    janela_quantidade = tk.Tk()
    janela_quantidade.title("Quantidade")
    janela_quantidade.geometry("400x200")  # Ajuste o tamanho conforme necessário

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10)

    quantidade_label = tk.Label(janela_quantidade, text=f"Quantidade de {variedade}:", font=("Helvetica", 14))
    quantidade_label.pack(pady=10)

    quantidade_entry = tk.Entry(janela_quantidade, font=("Helvetica", 14))
    quantidade_entry.pack(pady=10)
    quantidade_entry.bind("<Return>", lambda event, v=variedade, q=quantidade_entry: adicionar_item(v, q))

    confirmar_button = ttk.Button(janela_quantidade, text="Confirmar", command=lambda v=variedade, q=quantidade_entry: adicionar_item(v, q))
    confirmar_button.pack(pady=10)

    global fez_primeiro_pedido
    if fez_primeiro_pedido:
        boas_vindas_button.config(text="Novo Pedido", command=lambda: exibir_boas_vindas(nome_entry.get().upper()))
    fez_primeiro_pedido = True

    janela_quantidade.mainloop()

def adicionar_item(variedade, quantidade_entry):
    quantidade = int(quantidade_entry.get())

    if variedade not in escolhas_cliente:
        escolhas_cliente[variedade] = {"Quantidade": quantidade, "Preço Unitário": obter_preco(variedade)}
    else:
        escolhas_cliente[variedade]["Quantidade"] += quantidade

    messagebox.showinfo("Adicionado ao Pedido", f"{quantidade} {variedade}(s) adicionado(s) ao pedido!")

def obter_preco(variedade):
    # Adicione a lógica para obter os preços reais aqui
    # Por enquanto, estou usando preços fictícios
    precos = {"Skol": 8.00, "Brahma": 8.00, "Antarctica": 8.00, "Schin": 5.00, "Itaipava": 6.00, "Bohemia": 9.00,
              "Morango": 5.00, "Kiwi": 6.00, "Abacaxi": 7.00, "Johnnie Walker Red Label": 40.00,
              "Chivas Regal 12 Anos": 50.00, "Jack Daniel's Old No. 7": 45.00, "Mojito": 10.00, "Virgin Mary": 8.00,
              "Smoothie": 12.00}

    return precos.get(variedade, 0.00)  # Retorna 0.00 se o preço não estiver definido

def calcular_valor_total():
    total = sum(item["Quantidade"] * item["Preço Unitário"] for item in escolhas_cliente.values())
    mensagem = f"O valor total da sua conta é R${total:.2f}."
    messagebox.showinfo("Valor Total da Conta", mensagem)

def criar_janela():
    janela = tk.Tk()
    janela.title("Sistema de Pedidos")
    janela.geometry("800x600")  # Ajuste o tamanho conforme necessário

    nome_label = tk.Label(janela, text="Qual o seu nome meu chapa?", font=("Helvetica", 16))
    nome_label.pack(pady=10)

    nome_entry = tk.Entry(janela, font=("Helvetica", 14))
    nome_entry.pack(pady=10)
    nome_entry.bind("<Return>", lambda event: exibir_boas_vindas(nome_entry.get().upper()))

    global boas_vindas_button
    boas_vindas_button = ttk.Button(janela, text="Boas-vindas", command=lambda: exibir_boas_vindas(nome_entry.get().upper()))
    boas_vindas_button.pack(pady=20)

    finalizar_button = ttk.Button(janela, text="Finalizar Pedido", command=calcular_valor_total)
    finalizar_button.pack(pady=10)

    janela.mainloop()

# Chama a função para criar a janela principal
criar_janela()
