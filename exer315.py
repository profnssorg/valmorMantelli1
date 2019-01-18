###Titulo: Redução do tempo de vida
###Função: Este programa calcula a redução do tempo de vida ocasionado por fumar
###Autor: Valmor Mantelli Jr.
###Data: 05/12/20148
###Versão: 0.0.1

# Declaração de variável

d = 0

f = 0

# Atribuição de valor a variavel

f = int(input("Diga o número de cigarros dumados por dia: "))

d = int(input("Diga a quantidade de anos que você fuma: "))


#Processamento

total = f * 10 * d * 365

redução = total / 60  / 24

# Saída

print("O seu tempo de vida foi reduzido em %0.2f dias." %redução) 

