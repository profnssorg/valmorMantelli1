###Titulo: Maquina registradora
###Função: Este programa simula uma máquina registradora
###Autor: Valmor Mantelli Jr.
###Data: 24/12/2018
###Versão: 0.0.6

# Declaração de variáve

p = 0

c = 0

q = 0

soma = 0


# Atribuição de valor a variavel e processamento

while True:
	c = int(input("Digite o código do produto ou 0 encerrar: "))
	if c == 1:
		p = 0.5
	elif c == 2:
		p = 1
	elif c == 3: 
		p = 4
	elif c == 5:
		p = 7
	elif c == 9:
		p = 8
	elif c == 0:
		break
	else:
		print ("Código inválido!")
	if p != 0:
		q = int(input("Insira a quantidade: "))
		soma = soma + (p * q) 
# Saída

print ("O valor de suas compras é de R$%.2f" % soma)

	
