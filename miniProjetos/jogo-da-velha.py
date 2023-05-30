import random
tabela = [[1,2,3], [4,5,6], [7,8,9]]
players = [['Jogador 1', 'X'], ['Jogador 2','O']]
jogador1 = 0 
jogador2 = 1
playerStart = random.randint(0,1);#Sorteia quem começa o jogo;


def condicaoDeGanho():
    tamanhoTabela= len(tabela); # pega quantidade de [] dentro do array
    count_vertical_player1 = 0
    count_horizontal_player1 = 0
    count_vertical_player2 = 0
    count_horizontal_player2 = 0

    for i in range(tamanhoTabela):
        for j in range(tamanhoTabela):        
            if (tabela[i][j] == 'X'):
                count_horizontal_player1+=1
            if (tabela[j][i]) == 'X':
                count_vertical_player1+=1
            if (tabela[i][j] == 'O'):
                count_horizontal_player2+=1
            if (tabela[j][i]) == 'O':
                count_vertical_player2+=1
            
            if (j == 2):#cada loop do j
                if ((count_horizontal_player1 == 3) or (count_vertical_player1 == 3)):
                    print('X GANHOU')                
                if ((count_vertical_player2 == 3) or (count_horizontal_player2 == 3)):
                    print('Y GANHOU')                                    
                count_horizontal_player1 = 0
                count_vertical_player1 = 0  
                count_horizontal_player2 = 0
                count_vertical_player2 = 0            

def playerInput():
    print(f'Vez do jogador {players[playerStart][0]}')
    position = int(input('Insira o número correspondente à posição desejada:'));
    return position;    

def gerarTabuleiro():
    print(tabela[0])
    print(tabela[1])
    print(tabela[2])
    
def escolherPosicaoTabuleiro(posicaoEscolhida: int):
    tabela_pos = 1;
    for linha in range(0,3):
        for coluna in range (0,3):
            if (tabela_pos == posicaoEscolhida):
                tabela[linha][coluna] = players[playerStart][1]
                return True
            tabela_pos = tabela_pos + 1;
        
while True:
    playerStart = jogador2 if ( playerStart == jogador1 ) else jogador1 #Alterna o player na próxima jogada
    gerarTabuleiro()
    escolherPosicaoTabuleiro(playerInput());
    condicaoDeGanho()

    
