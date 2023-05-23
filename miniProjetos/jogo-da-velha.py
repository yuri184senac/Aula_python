import random

tabela = [[1,2,3], [4,5,6], [7,8,9]]
players = [['Jogador 1', 'X'], ['Jogador 2','O']]
player = random.randint(0,1);#Sorteia quem começa o jogo;


    
def condicaoDeGanho():
    #Coluna verifcando
    soma = 0
    for linha in range(len(tabela)):
        for coluna in range(len(tabela)):
            if (tabela[linha][coluna] == 'X'):
               
          
           
    
def playerInput():
    print(f'Vez do jogador {players[player][0]}')
    position = int(input('Insira o número correspondente à posição desejada:'));
    return position;    

def gerarTabuleiro():
    print(tabela[0])
    print(tabela[1])
    print(tabela[2])
    
def escolherPosicaoTabu(posicao):
    if (posicao == 1) :
        tabela[0][0] = players[player][1]
    elif (posicao == 2):
        tabela[0][1] = players[player][1]
    elif (posicao == 3):
        tabela[0][2] = players[player][1]
    elif (posicao == 4):
        tabela[1][0] = players[player][1]
    elif (posicao == 5):
        tabela[1][1] = players[player][1]
    elif (posicao == 6):
        tabela[1][2] = players[player][1]
    elif (posicao == 7):
        tabela[2][0] = players[player][1]
    elif(posicao == 8):
        tabela[2][1] = players[player][1]
    elif(posicao == 9):
        tabela[2][2] = players[player][1]


while True:
    player = 1 if (player==0) else 0 #Alterna o player na próxima jogada
    gerarTabuleiro()
    escolherPosicaoTabu(playerInput())
    condicaoDeGanho()
    
