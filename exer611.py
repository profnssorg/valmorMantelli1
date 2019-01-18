###Titulo: Alterando listagem 6.15
###Função: Alterando a listagem 6.15, substituindo while por for quando possível
###Autor: Valmor Mantelli Jr.
###Data: 01/01/2019
###Versão: 0.0.2

### Declaração de variáve 

l = []

n = 0

x = 0

### Atribuição de valor e processamento

while True:	
	n = int(input("Digite o número que deseja inserir na lista( ou 0 para encerrar): "))
	if n == 0:
		break
	l.append(n)
for x in l:

### Saída

	print (x)

