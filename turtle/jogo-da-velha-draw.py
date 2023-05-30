from turtle import *

def screenConfig():
  title('Jogo da Velha')
  setup (width=600, height=600, startx=None, starty=None)
  screenTableDraw()
  

def screenTableDraw():
  tracer(False)

  forward(20)
  
  backward(20)
  tracer(True)
  

  
def main():
  screenConfig()
  done()

if __name__ == "__main__":
  main()