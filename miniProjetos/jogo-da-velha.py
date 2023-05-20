tabela = [[1,2,3], [4,5,6], [7,8,9]]
players = [['Jogador 1', 'X'], ['Jogador 2','O']]


def condicaoDeganho():
    if ()

def playerInput():
    position = int(input('Insira o número correspondente à posição desejada:'));
    return position;    

def gerarTabuleiro():
    print(tabela[0])
    print(tabela[1])
    print(tabela[2])
    
def inserirValor(posicao):
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



gerarTabuleiro()
inserirValor(playerInput())
gerarTabuleiro()
