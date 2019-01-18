###Titulo: Exibição de menu
###Função: Este programa exibe menu para escolha de operação
###Autor: Valmor Mantelli Jr.
###Data: 27/12/2018
###Versão: 0.0.2

# Declaração de variáve e atribuição de valor

while True:
	print ("""

 									    Menu
								=============================	
								=     1 - Adição	     =
								=     2 - Subtração	     =
								=     3 - Multiplicação	     =
								=     4 - Divisão	     =
								=     5 - Sair		     =
								==============================
""")

	operador = int(input("Escolha um operador do menu: "))
	if operador == 5:
		break
	elif  1 < operador > 5:
		print ("Você escolheu uma opção inválida. Tente novamente!!!")
	
	elif operador >= 1 and operador <5:
		n = int(input("Escolha um número. O programa fará 10 repetições com o operador escolhido: "))
		x = 1

###  Processamento e Saída

		while x <= 10:
			if operador == 1:
				print ("%d + %d = %d" % (n, x, n + x))
			if operador == 2:
				print ("%d - %d = %d" % (n, x, n - x))
			if operador == 3:
                                print ("%d X %d = %d" % (n, x, n * x))
			if operador == 4:
                                print ("%d / %d = %.4f" % (n, x, n / x))
			x = x + 1
	


