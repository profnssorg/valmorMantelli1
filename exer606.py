###Titulo: Organizador de fila
###Função: Este programa organiza entradas e saídas de duas filas 
###Autor: Valmor Mantelli Jr.
###Data: 31/12/2018
###Versão: 0.0.2

### Declaração de variáve 

último = 0

fila1 = [] 

fila2 = []

x = 0

operação = []

### Atribuição de valor

while True:
	print ("\nExistem %d clientes na fila a e %d clientes na fila 2"  % (len (fila1), len (fila2)))
	print ("Fila 1 atual: ", fila1)
	print ("Fila 2 atual: ", fila2)
	print ("Digite F para adicionar um cliente ao final da fila 1 ou G a fila 2,")
	print ("para realizar o atendimento na fila 1 digite A ou para B fila 2.")
	print ("Pressione S para sair")
	operação = input ("Operação (F ou G, A ou B, ou S): ")
	x = 0
	sair = False
### Processamento e saída
	while x < len (operação): 
		if operação [x] == "A" or operação [x] == "F":
			fila = fila1
		else:
			fila = fila2
		if operação [x] == "A" or operação [x] == "B":
			if (len(fila)) > 0:
                        	atendido = fila.pop(0)
                        	print ("Cliente %d atendido" % atendido)
			else:
                        	print ("Fila vazia! Ninguém para atender")
		elif operação [x] == "F" or operação [x] == "G":
			último += 1 #Adicionado o ticket do novo cliente
			fila.append(último)
		elif operação [x] == "S" or operação [x] == "s":
			sair = True
			break
		else:
			print ("Operação ínválida! %s na posição %d! Digite Apenas F, A ou S!" % (operação [x], x))
		x += 1
	if (sair):
		break	 
