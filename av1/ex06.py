import os
print('PESQUISA DE PREFERÊNCIA DE COMBUSTÍVEL AUTOMOTIVO');
print('Digite o número correspondente ao seu combustível preferido');
print('OPÇÕES:');
print('------------------------');
print('1.Gasolina');
print('2.Álcool');
print('3.Diesel');
print('4.Fim');
#ENTRADA DE DADOS
respostas = [];
iniciaPrograma = True;
dieselCount = 0;
gasolinaCount = 0;
alcoolCount = 0;
while iniciaPrograma:
    #VALIDA ENTRADA
    validaEntrada = input('Insira o número da opção: ');
    if (validaEntrada.isnumeric()):
        validaEntrada = int(validaEntrada);
    else:
        while validaEntrada.isalpha():
            validaEntrada = input('Insira um número e não um caractere : ');
    #PROCESSAMENTO
    if (validaEntrada > 0 and validaEntrada <= 4):
        if (validaEntrada == 1):
            gasolinaCount= gasolinaCount + 1;
        elif (validaEntrada == 2):
            alcoolCount= alcoolCount + 1;
        elif (validaEntrada == 3):
            dieselCount= dieselCount + 1;
        elif (validaEntrada == 4):
            iniciaPrograma = False;
            print('Você digitou a opção de sair');

print('----MUITO OBRIGADO !----');
print('GASOLINA = ', gasolinaCount);
print('Álcool = ', alcoolCount);
print('Diesel = ', dieselCount);



