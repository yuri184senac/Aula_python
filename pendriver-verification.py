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
            print('O arquivo existe');
        else:
            if(tocarMusica):
                os.system('start C:/Users/36129382023.1n\Documents/roleta-russa/sound1.mp3');
            tocarMusica = False;
            print('Não existe!');
            break;
