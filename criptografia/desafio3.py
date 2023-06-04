numeros = []

#FUNÇÕES
def parseToZeus(frase, opcao, chave):
    if (opcao == 1) :
        rn = chave 
    elif (opcao == 2):
        rn = -chave
    for char in enumerate(frase):
        decimal = ord(char[1])
        if (decimal != 32):
            numeros.append(decimal+rn)
        elif (decimal == 32):
            numeros.append(decimal)

def imprimirFrase():
    string = ''
    for num in numeros:
        string += chr(num) #monta uma string apartir dos elementos do vetor.
    print('Resultado do processamento: ',string)

#---EXECUTANDO O ALGORITMO---

#ENTRADA DE DADOS
print('Desafio 3 – criar uma criptografia assimétrica com chave privada')
print('--------MENU------')
print('1. CRIPTOGRAFAR')
print('2. DESCRIPTOGRAFAR')

print('')
opcao = int(input('OPÇÃO: '));
print('Você escolheu a opção', opcao);
frase = input('Insira a frase :  ');
chave = int(input('Insira a sua chave privada: '));

#PROCESSO DE DADOS
parseToZeus(frase, opcao, chave)
#SAÍDA DE DADOS
imprimirFrase()


    

  
  

