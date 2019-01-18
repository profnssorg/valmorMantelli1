###Titulo: Organizador de fila
###Função: Este programa identifica entradas e saídas de uma fila
###Autor: Valmor Mantelli Jr.
###Data: 31/12/2018
###Versão: 0.0.2

### Declaração de variáve 

último = 10

fila  = list(range(1, último+1))

x = 0

### Atribuição de valor

while True:
	print ("\nExistem %d clientes na fila "  % len (fila))
	print ("Fila atual: " , fila)
	print ("Digite F para adicionar um cliente ao fim da fila, ")
	print ("ou A para realizar o atendimento. S para sair")
	operação = input ("Operação (F, A ou S): ")
	x = 0
	sair = False
### Processamento e saída
	while x < len (operação): 
		if operação [x] == "A":
                	if (len(fila)) > 0:
                        	atendido = fila.pop(0)
                        	print ("Cliente %d atendido" % atendido)
                	else:
                        	print ("Fila vazia! Ninguém para atender")
		elif operação [x] == "F":
			último += 1 #Adicionado o ticket do novo cliente
			fila.append(último)
		elif operação [x] == "S":
			sair = True
			break
		else:
			print ("Operação ínválida! %s na posição %d! Digite Apenas F, A ou S!" % (operação [x], x))
		x += 1
	if (sair):
		break	 
