###Título: Programa imprime lista.py
###Descrição: Este programa imprime separadamente por linhas cada nível de listas dentro de listas
###Autor: Valmor Mantelli Jr.
###Data: 16/01/2018
###Versão 0.0.6

# Declaração de variáveis

L = [[[]]]

niveis = 0

nivel = 0

spc = 0

#Entrada de dados

L = [1, [2, 3, 4, [5, 6, 7]]]

niveis = 4


#Processamento dos dados e saída
def  comp (l, nivel = 0):
        spc = " " * niveis * nivel
        if type (l) == list:
                print (spc, "[")
                for i in l:
                        comp (i, nivel +1)
                print (spc, "]")
        else:
                print (spc, l)
comp (L)
