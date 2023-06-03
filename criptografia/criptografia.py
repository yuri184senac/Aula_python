lista = {
        "z" : "p", 
        "e" : "o" ,
        "n" : "l",
        "i" : "a" ,
        "t" : "r" ,
        
        "p" : "z" ,
        "o" : "e" ,
        "l" : "n" ,
        "a" : "i" ,
        "r" : "t"
}

letras = {
    'á':'a',
    'à':'a',
    'ã':'a',
    'é':'e',
    'í':'i',
    'ç':'c',
    'ó':'o',
}


#SANITIZAR DADOS NAO CONCLUIDO
def sanitizarEntradaDeDados(frase):
    for char in enumerate(frase):
        for letraEspecial, letraNormal in letras.items():
            if char[1] == letraEspecial:
              frase = frase.replace(letraEspecial, letraNormal)      

                  
def parseToZeus(frase):
    # try:
        listaFrase = list(frase);
        for char in enumerate(listaFrase):
           for charAntigo, charNovo in lista.items():
               if char[1] == charAntigo:
                listaFrase[char[0]] = charNovo;
                frase = ''.join(listaFrase)
        print(frase)
                            
       
    # except:
    #     print('Ocorreu um erro no código durante a execução do programa2')


parseToZeus('todo mundo age nao apenas por compulsao externa, mas tambem por necessidade intima') 

