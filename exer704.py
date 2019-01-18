###Titulo: Leitor de string
###Função: Este programa lê uma string e imprime o número de vezes que as letras aparecem
###Autor: Valmor Mantelli Jr.
###Data: 08/01/2019
###Versão: 0.0.1


# Declaração de variáveis

f = ""

c =  {}

p = 0

x = 0

#Entrada de dados

f = input("Digite a sequencia de letras: ")


#Processamento dos daodos

for p in f:
        if p in c:
                c[p] += 1
        else:
                c[p] = 1
for x in c:


#Saída dos dados
        print("%s: %dX"  %( x, c[x]))
