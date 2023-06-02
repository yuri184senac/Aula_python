from turtle import *

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
  print(x,y)

def tabela_mouse_click(x,y):
  goto(x,y)
  


def player_1_mark():
    #DESENHA UM X
    # speed(1)
    # goto(15,15)
    # goto(-15,-15)
    # goto(0,0)
    # goto(-15,15)
    # goto(15,-15)
    penup()
    position_x = 125
    position_y = 125
    goto(position_x,position_y)
    pendown()
    goto(100,150)
    goto(150,100)
    
    goto(125,125)
    goto(100,100)
    goto(150,150)

def player_2_mark():
  #DESENHA UM Círculo
  circle(25)

def main():
  #screenConfig()
  player_1_mark()
  done()

if __name__ == "__main__":
  main()