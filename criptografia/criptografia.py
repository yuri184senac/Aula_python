lista = [
    ["z" , "p"],
    ["e" , "o"],
    ["n" , "l"],
    ["i" , "a"],
    ["t" , "r"],
    
    ["p" , "z"],
    ["o" , "e"],
    ["l" , "n"],
    ["a" , "i"],
    ["r" , "t"]
]

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
    try:
        for char in enumerate(frase):
            for letraAntiga, letraNova in lista.items():
                print(letraNova)
                if char[1] == letraAntiga :
                    # print(char[1], '<-->', letraNova)           
                    frase = frase.replace(char[1], letraNova)
        print(frase)
    except:
        print('Ocorreu um erro no código durante a execução do programa2')


parseToZeus('todo mundo age nao apenas por compulsao externa, mas tambem por necessidade intima') 

