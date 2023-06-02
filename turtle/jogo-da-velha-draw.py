from turtle import *
coordenada = [0,0]
def screenConfig():
  title('Jogo da Velha')
  setup (width=600, height=600, startx=None, starty=None)
  screenTableDraw()


def screenTableDraw():
  tracer(False)
  #start position
  alturaTabela= 45
  larguraTabela= 100
  compLinhaHorizontal = larguraTabela + (larguraTabela*50)/100 #porcentagem
  # COLUNA 1
  penup()
  goto(0,alturaTabela)
  pendown()
  
  goto(compLinhaHorizontal,alturaTabela) 
  goto(-compLinhaHorizontal,alturaTabela)
  goto(-larguraTabela/2,alturaTabela)
  goto(-larguraTabela/2,alturaTabela+50)
  goto(-larguraTabela/2,alturaTabela-50)
  goto(-larguraTabela/2,alturaTabela)

  #COLUNA 2
  goto(larguraTabela/2,alturaTabela)
  goto(larguraTabela/2,alturaTabela+50)
  goto(larguraTabela/2,alturaTabela-50)

  
 #parte-de-baixo-do-desenho
  segunda_barra_horizontal = alturaTabela-50
  goto(compLinhaHorizontal,segunda_barra_horizontal)
  goto(-compLinhaHorizontal,segunda_barra_horizontal)

  goto(-larguraTabela/2, segunda_barra_horizontal)
  goto(-larguraTabela/2, segunda_barra_horizontal-50)
  goto(-larguraTabela/2, segunda_barra_horizontal)

  goto(larguraTabela/2, segunda_barra_horizontal)
  goto(larguraTabela/2, segunda_barra_horizontal-50)
  
  tracer(True)
  

def get_mouse_click_coordenate(x,y):
    coordenada[0] = x
    coordenada[1] = y
    tabela_mouse_click()
    print(coordenada)


def tabela_mouse_click():
    if coordenada[0] > -150 and coordenada[0] < -52 and coordenada[1] > 48 and coordenada[1] < 94: 
      print("CLICK NO QUADRADO 1:", coordenada)
    elif coordenada[0] > -49 and coordenada[0] < 48 and coordenada[1] > 48 and coordenada[1] < 94:
      print('CLICK NO QUADRADO 2:', coordenada)
    elif coordenada[0] > 53 and coordenada[0] < 150 and coordenada[1] > 48 and coordenada[1] < 94:
      print('CLICK NO QUADRADO 3:', coordenada)
    elif coordenada[0] > -150 and coordenada[0] < -52 and coordenada[1] > -3 and coordenada[1] < 44:
      print('CLICK NO QUADRADO 4:',coordenada)
    elif coordenada[0] > -49 and coordenada[0] < 48 and coordenada[1] > -3 and coordenada[1] < 44:
      print('CLICK NO QUADRADO 5:', coordenada)
    elif coordenada[0] > -53 and coordenada[0] < 150 and coordenada[1] > -3 and coordenada[1] < 44:
      print('CLICK NO QUADRADO 6:', coordenada)  
    elif coordenada[0] > -150 and coordenada[0] < -52 and coordenada[1] > -53 and coordenada[1] < -6:
      print('CLICK NO QUADRADO 7:', coordenada)  
    elif coordenada[0] > -49 and coordenada[0] < 48 and coordenada[1] > -53 and coordenada[1] < -6:
      print('CLICK NO QUADRADO 8:', coordenada)    
    elif coordenada[0] > -53 and coordenada[0] < 150 and coordenada[1] > -53 and coordenada[1] < -6:
      print('CLICK NO QUADRADO 9:', coordenada)  
# def player_1_mark():
#     #DESENHA UM X
    
   

def player_2_mark(x,y):
  #DESENHA UM Círculo
  goto(x,y)
  circle(25)



def main():
  screenConfig()
  onscreenclick(get_mouse_click_coordenate)
  done()

if __name__ == "__main__":
  main()