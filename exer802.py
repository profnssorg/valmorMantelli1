###Título: Função
###Descrição: Este programa  é uma função que retorna o maior dos números
###Autor: Valmor Mantelli Jr.
###Data: 14/01/2018
###Versão 0.0.1

### Declaração de variáveis



### Entrada de dados

### Processamento de dados

def mult (a,b):
	if a % b == 0:
		return True
	else:
		return False

### Saída

print ("Resultado esperado: múltiplos(8,4) == True => Resultado obtido: são múltiplos?  %s" % (mult(8,4)))
print ("Resultado esperado: múltiplos(7,3) == False => Resultado obtido: são múltiplos?  %s" % (mult(7,3)))
print ("Resultado esperado: múltiplos(5,5) == True => Resultado obtido: são múltiplos?  %s" % (mult(5,5)))
