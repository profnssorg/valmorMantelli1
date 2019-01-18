###Titulo: Divisão
###Função: Este programa calcula a divisão entre dois números inteiros utilizando soma e subtração
###Autor: Valmor Mantelli Jr.
###Data: 27/12/2018
###Versão: 0.0.1

### Declaração de variáve 

dividendo = 0

divisor = 0

quociente = 0

resto = 0

### Atribuição de valor

dividendo = int(input ("Digite o número que deseja dividir: "))

divisor = int(input ("Digite o número pelo qual deseja dividir: "))

n = dividendo

### Processamento

while n >= divisor:
	n = n - divisor
	quociente = quociente + 1
resto = n
	
### Saída
print("%d divido por %d é igual a %d e resta %d" % (dividendo, divisor, quociente, resto))

