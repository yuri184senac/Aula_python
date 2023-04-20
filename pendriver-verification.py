import os

iniciaScript = True;
inicializador = True
tocarMusica = False
while iniciaScript == True:
    inicializador = True;
    while inicializador==True:
        if (os.path.exists(('E:'))):
            inicializador = True;
            tocarMusica = True;
            print('PEN DRIVER CONECTADO');
        else:
            if(tocarMusica):
                os.system('start C:/Users/36129382023.1n\Documents/roleta-russa/sound1.mp3');
            tocarMusica = False;
            print('PEN DRIVER REMOVIDO');
            break;
