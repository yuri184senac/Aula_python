from turtle import *

def screenConfig():
  title('Jogo da Velha')
  setup (width=600, height=600, startx=None, starty=None)
  screenTableDraw()
  

def screenTableDraw():
  tracer(False)
  #start position
  

  # COLUNA 1
 
  goto(45,0)  #total 90
  goto(-45,0)
  goto(-22.5,0)
  goto(-22.5,100)
  goto(-22.5,-100)
  goto(-22.5,0)

  #COLUNA 2
  goto(22.5,0)
  goto(22.5,100)
  goto(22.5,-100)
 
  
  # # Completa a linha da esquerda
  # goto(-300,0)
  
  tracer(True)
  

  
def main():
  screenConfig()
  done()

if __name__ == "__main__":
  main()