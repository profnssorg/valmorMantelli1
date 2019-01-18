###Titulo: Números primos
###Função: Este programa exibe indica se determinado número é primo ou não
###Autor: Valmor Mantelli Jr.
###Data: 27/12/2018
###Versão: 0.0.4

### Declaração de variáve 

n = 0

x = 0

### Atribuição de valor, processamento e saída
while True:
	n = int(input("Escolha um número, maior que zero (ou 999 para sair): "))
	if n == 999:
		break
	if n < 0:
		print ("Eu disse um número maior que zero, sua besta")
	else:
		if n == 0 or n == 1:
 			print ("%d é um caso especial." % n)
		else: 
			if n == 2:
				print ("2 é um número primo")
			elif n % 2 == 0:
				print ("%d não é um número primo, pois o único número primo par é 2." % n)	
			else:
				x = 3
				while x < n:
					if n % x == 0:
						break
					x = x + 2
				if x == n:
					print (" %d é um número primo" % n)
				else:
					print (" %d não é um número primo, pois é divisível por %d" % (n, x))
					


