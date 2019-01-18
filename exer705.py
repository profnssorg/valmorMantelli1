###Titulo: Leitor de string
###Função: Este programa lê duas string e gera uma terceira com caracteres da primeira 
###Autor: Valmor Mantelli Jr.
###Data: 08/01/2019
###Versão: 0.0.1


# Declaração de variáveis

f = ""

s = ""

t = ""

x = 0

#Entrada de dados

f = input("Digite a primeira sequência de letras: ")

s = input("Digite a segunda sequencia de letras: ")


#Processamento dos dados e saída

for x in f:
        if x not in s:
                t += x
if len (t) != 0:
        print ("Retirando os caracteres %s de %s, restaram %s." % (s, f, t))
else:
        print("Não sobraram caracteres para serem retirados.")
