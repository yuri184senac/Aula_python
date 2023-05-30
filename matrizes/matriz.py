tabela = [['Y','Y','Y'], 
          ['Y','X','X'], 
          ['Y','Y','X']]


tamanhoTabela= len(tabela); # pega quantodade de [] dentro do array
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

      if (tabela[i][j] == 'Y'):
        count_horizontal_player2+=1
      if (tabela[j][i]) == 'Y':
        count_vertical_player2+=1
      
      

      if (j == 2):#cada loop do j
          if ((count_horizontal_player1 == 3) or (count_vertical_player1 == 3)):
            print('X GANHOU')
          if ((count_vertical_player2 or count_horizontal_player2) == 3):
            print('Y GANHOU')

          count_horizontal_player1 = 0
          count_vertical_player1 = 0  
          count_horizontal_player2 = 0
          count_vertical_player2 = 0
    

