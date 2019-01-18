###Título: Programa jogo da velha.py
###Descrição: Esse programa executa um jogo da velha
###Autor: Valmor Mantelli Jr.
###Data: 11/01/2018
###Versão 0.0.5

# Declaração de variáveis


#Processamento dos dados e saída


print ("Jogo da velha. Utilize o quadro abaixo para orientar as posições onde irá fazer suas jogadas")





game ="""
   |   |      
---+---+---  
   |   |     
---+---+---  
   |   |     

 1 | 2 | 3
---+---+---  
 4 | 5 | 6
---+---+---  
 7 | 8 | 9




"""
pos = [None, (1, 1), (1, 5), (1, 9), (3, 1), (3, 5), (3, 9), (5, 1), (5, 5), (5, 9)]

win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 9], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

tab = []

for l in game.splitlines():
        tab.append(list(l))
pl = "X"
play = True
pld = 0
while True:
	for t in tab:  
		print("".join(t))
	if not play: 
		break
	if pld == 9:
		print("O jogo terminou empatado.")
		break
	move = int(input("Informe a posição entre 1 e 9 na qual deseja jogar (player %s): " % pl))
	if move < 1 or move > 9:
		print("Você escolheu uma posição inválida no tabuleiro")
		continue
	if tab[pos[move][0]][pos[move][1]] != " ":
		print("Você escolheu uma posição inválida no tabuleiro. Tente novamente");
		continue
	tab[pos[move][0]][pos[move][1]] = pl
	for w in win:
		for x in w:
			if tab[pos[x][0]][pos[x][1]] != pl:
				break
		else: 
			print("O jogador %s ganhou (%s): "%(pl, w))
			jogando = False
			break
	pl = "X" if pl == "O" else "O" 
	pld +=1 

