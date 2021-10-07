import tkinter as tk
from tkinter import *
import random
import string
import clipboard


class Tela:
    def __init__(self, master):
        self.telaPrincipal = master
        self.telaPrincipal.title("Gerador de Senha")

        self.quantidade_car = tk.StringVar()

        self.telaPrincipal.geometry("500x300")

        self.texto_tela1 = tk.Label(self.telaPrincipal, text="Escolha as opções da senha: ")
        self.texto_tela1.place(x=140, y=10)

        self.cb_numero = tk.BooleanVar()
        self.cb_letra = tk.BooleanVar()
        self.cb_simbolo = tk.BooleanVar()

        self.cb1 = tk.Checkbutton(self.telaPrincipal, text="Números", variable=self.cb_numero)
        self.cb1.place(x=180, y=30)

        self.cb2 = tk.Checkbutton(self.telaPrincipal, text="Letras", variable=self.cb_letra)
        self.cb2.place(x=180, y=55)

        self.cb3 = tk.Checkbutton(self.telaPrincipal, text="Símbolos", variable=self.cb_simbolo)
        self.cb3.place(x=180, y=80)

        self.texto_tela2 = tk.Label(self.telaPrincipal, text="Selecione a quantidade de Caracteres:")
        self.texto_tela2.place(x=140, y=105)

        self.numero_slide = Scale(master, from_=6, to=25, orient=HORIZONTAL)
        self.numero_slide.place(x=180, y=125)

        self.senha_mostrada = StringVar()

        self.texto_tela3 = tk.Label(self.telaPrincipal, textvariable=self.senha_mostrada, font=("Verdana", "18"))
        self.texto_tela3.place(x=100, y=165)

        self.btn = tk.Button(self.telaPrincipal, text="Gerar senha", font=("Verdana", "14"), command=self.clique)
        self.btn.place(x=80, y=230)

        self.btn = tk.Button(self.telaPrincipal, text="Copiar Senha", font=("Verdana", "14"), command=self.copiar)
        self.btn.place(x=260, y=230)

    def clique(self):
        senha_final = GeradorSenha(self.cb_numero.get(), self.cb_letra.get(),
                                   self.cb_simbolo.get(), self.numero_slide.get())

        self.senha_mostrada.set(senha_final)

    def copiar(self):
        clipboard.copy(self.senha_mostrada.get())


class GeradorSenha:
    def __init__(self, cb_numero, cb_letra, cb_simbolo, quantidade_caracteres):
        self.senha_nao_tratada = self.selecao_de_tipo(cb_numero, cb_letra, cb_simbolo, quantidade_caracteres)

        self.senha_final = self.transformar_lista_em_string(self.senha_nao_tratada)

    def __str__(self):
        return self.senha_final

    def selecao_de_tipo(self, numero_selecionado, letra_selecionada, simbolo_selecionado, quanti_caracteres):
        if letra_selecionada:
            if numero_selecionado:
                if simbolo_selecionado:
                    lista_gerada = self.todos_os_caracteres(quanti_caracteres)
                else:
                    lista_gerada = self.somente_letra_e_numeros(quanti_caracteres)
            elif simbolo_selecionado:
                lista_gerada = self.somente_letra_e_simbolo(quanti_caracteres)
            else:
                lista_gerada = self.somente_letras(quanti_caracteres)
        elif numero_selecionado:
            if simbolo_selecionado:
                lista_gerada = self.somente_numero_e_simbolo(quanti_caracteres)
            else:
                lista_gerada = self.somente_numeros(quanti_caracteres)
        elif simbolo_selecionado:
            lista_gerada = self.somente_simbolos(quanti_caracteres)
        else:
            lista_gerada = 'Selecione alguma das opções'

        return lista_gerada

    def somente_numeros(self, quant_caracteres):
        lista1 = []
        for quantidade in range(quant_caracteres):
            lista1.append(self.numero_aleatorio())
        return lista1

    def somente_simbolos(self, quant_caracteres):
        lista1 = []
        quantidade_caracteres = int(quant_caracteres)
        for quantidade in range(quantidade_caracteres):
            lista1.append(self.simbolo_aleatorio())
        return lista1

    def somente_letras(self, quant_caracteres):
        lista1 = []
        quantidade_caracteres = int(quant_caracteres)
        for quantidade in range(quantidade_caracteres):
            lista1.append(self.letra_aleatoria())
        return lista1

    def somente_letra_e_numeros(self, quant_caracteres):
        lista1 = []
        quantidade_caracteres = int(quant_caracteres)
        for quantidade in range(quantidade_caracteres):
            seletor = self.escolha_tipo_2()
            if seletor == '0':
                lista1.append(self.letra_aleatoria())
            elif seletor == '1':
                lista1.append(self.numero_aleatorio())
        return lista1

    def somente_numero_e_simbolo(self, quant_caracteres):
        lista1 = []
        quantidade_caracteres = int(quant_caracteres)
        for quantidade in range(quantidade_caracteres):
            seletor = self.escolha_tipo_2()
            if seletor == '0':
                lista1.append(self.numero_aleatorio())
            elif seletor == '1':
                lista1.append(self.simbolo_aleatorio())
        return lista1

    def somente_letra_e_simbolo(self, quant_caracteres):
        lista1 = []
        quantidade_caracteres = int(quant_caracteres)
        for quantidade in range(quantidade_caracteres):
            seletor = self.escolha_tipo_2()
            if seletor == '0':
                lista1.append(self.letra_aleatoria())
            elif seletor == '1':
                lista1.append(self.simbolo_aleatorio())
        return lista1

    def todos_os_caracteres(self, quant_caracteres):
        lista1 = []
        quantidade_caracteres = int(quant_caracteres)
        for quantidade in range(quantidade_caracteres):
            seletor = self.escolha_tipo()
            if seletor == '0':
                lista1.append(self.letra_aleatoria())
            elif seletor == '1':
                lista1.append(self.simbolo_aleatorio())
            elif seletor == '2':
                lista1.append(self.numero_aleatorio())
        return lista1

    def escolha_tipo(self):
        return str(random.randrange(3))

    def escolha_tipo_2(self):
        return str(random.randrange(2))

    def numero_aleatorio(self):
        return str(random.randrange(10))

    def letra_aleatoria(self):
        return random.choice(string.ascii_letters)

    def simbolo_aleatorio(self):
        return random.choice(string.punctuation)

    def transformar_lista_em_string(self, lista_gerada):
        senhagerada = ''.join(lista_gerada)
        return senhagerada


janelaRaiz = tk.Tk()

Tela(janelaRaiz)

janelaRaiz.mainloop()
