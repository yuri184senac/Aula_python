#Aluno: Yuri Conder Roliz Sabbagh
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


def sanitizarEntradaDeDados(frase):
    for char in enumerate(frase):
        for letraEspecial, letraNormal in letras.items():
            if char[1] == letraEspecial:
              frase = frase.replace(letraEspecial, letraNormal)      
    return frase.lower();
                  
def parseToZeus(frase):
        fraseSanitizada = sanitizarEntradaDeDados(frase)
        listaFraseSanitizada = list(fraseSanitizada);
        for char in enumerate(listaFraseSanitizada):
           for charAntigo, charNovo in lista.items():
               if char[1] == charAntigo:
                listaFraseSanitizada[char[0]] = charNovo;
                fraseSanitizada = ''.join(listaFraseSanitizada)
        return fraseSanitizada.capitalize()

#ENTRADA DE DADOS
print('Desafio 1 – criar uma criptografia simétrica')
print('--------MENU------')
print('1. CRIPTOGRAFAR')
print('2. DESCRIPTOGRADAR')
print('')
opcao = int(input('OPÇÃO: '));
print('Você escolheu a opção', opcao);

if (opcao == 1):
    frase:str = input('Insira a frase á ser criptografada: ');
    print('')
    print(f'A frase "{frase}" foi criptografada: ')
    print('')
    print('RESULTADO ---->', parseToZeus(frase))
elif (opcao == 2):
    frase:str = input('Insira a frase á ser descriptografada: ');
    print(f'A frase "{frase}" foi descriptografada: ')
    print('')
    print('RESULTADO ---->', parseToZeus(frase))
print('')

