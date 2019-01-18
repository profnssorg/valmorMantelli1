###Titulo: Soma e média
###Função: Este programa soma números e apresenta média aritmética
###Autor: Valmor Mantelli Jr.
###Data: 20/12/2018
###Versão: 0.0.8

# Declaração de variáve

s = 0

n = 0

v= 0

# Atribuição de valor a variavel e processamento

while True: 
	v = int(input("Digite um número inteiro ou 0 para sair: "))
	if v == 0:
		break
	s = s + v
	n = n + 1
	x = s / n 
# Saída

print ("A quantidade de números digitados é %d e sua soma e média aritmética são respectivamente %d e %d" % (n , s , x))

	
