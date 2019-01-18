###Título: Função
###Descrição: Este programa valida uma string
###Autor: Valmor Mantelli Jr.
###Data: 15/01/2018
###Versão 0.0.5

### Declaração de variáveis



### Entrada de dados

print ("Programa verifica se a palavra inserida esta dentro do intervalo determinado")

min = int(input("Diga o número minimo de letras que a palavra deve conter(maior ou igual a zero): "))

max = int(input("Diga o número máximo de letras que a palavra deve conter(maior que o mínimo): "))

p =  input("Diga a palavra que deseja verificar: ")

### Processamento de dados

def validador (p, min, max):
	s = len(p)
	return min <= s <= max


### Saída
print (validador(p, min, max))
	
