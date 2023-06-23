#Alunos: Yuri Roliz e Joao Gabriel
import random
tabela = [[1,2,3], [4,5,6], [7,8,9]]
players = [['Jogador 1', 'X'], ['Jogador 2','O']]
jogador1 = 0 
jogador2 = 1
playerStart = random.randint(0,1);#Sorteia quem começa o jogo;
rodadas = 0
tamanhoTabela= len(tabela); # pega quantidade de [] dentro do array

def playerInput():
    print(f'Vez do jogador {players[playerStart][0]}')
    position = int(input('Insira o número correspondente à posição desejada:'));                    
    return position;    

def gerarTabuleiro():
    print(tabela[0])
    print(tabela[1])
    print(tabela[2])
    
def escolherPosicaoTabuleiro(posicaoEscolhida: int):
    flag = False
    tabela_pos = 1;
    for linha in range(0,3):
        for coluna in range (0,3):
            if (tabela_pos == posicaoEscolhida) :   
               if tabela[linha][coluna] == 'O' or tabela[linha][coluna] == 'X':
                    print('Posição já está ocupada')
                    linha = 0;
                    coluna = 0;
                    tabela_pos = tabela_pos
               else:
                    tabela[linha][coluna] = players[playerStart][1]                      
                    return True    
            tabela_pos = tabela_pos + 1;
           
    
while True:
    playerStart = jogador2 if ( playerStart == jogador1 ) else jogador1 #Alterna o player na próxima jogada
    gerarTabuleiro()
    escolherPosicaoTabuleiro(playerInput());
    