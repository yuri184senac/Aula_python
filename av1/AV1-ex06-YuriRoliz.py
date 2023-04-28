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
            print('Você selecionou a opção gasolina');
        elif (validaEntrada == 2):
            alcoolCount= alcoolCount + 1;
            print('Você selecionou a opção álcool');
        elif (validaEntrada == 3):
            dieselCount= dieselCount + 1;
            print('Você selecionou a opção diesel');
        elif (validaEntrada == 4):
            iniciaPrograma = False;
            print('Você digitou a opção de sair');

print('');
print('----MUITO OBRIGADO !----');

primeiro = '';
primeiroCount = 0;
if (gasolinaCount > alcoolCount and gasolinaCount > dieselCount):
    primeiro = 'Gasolina';
    primeiroCount = gasolinaCount;
elif (alcoolCount > gasolinaCount and alcoolCount > dieselCount):
    primeiro =  'Álcool';
    primeiroCount = alcoolCount;
elif (dieselCount > gasolinaCount and dieselCount > alcoolCount):
    primeiro = 'Diesel';
    primeiroCount = dieselCount;

segundo='';
segundoCount = 0;
terceiro='';
terceiroCount = 0;

if (primeiro == 'Gasolina'):
    if (alcoolCount > dieselCount):
        segundo = 'Álcool';
        segundoCount = alcoolCount;
        terceiro = 'Diesel';
        terceiroCount = dieselCount;
    else:
        segundo = 'Diesel';
        segundoCount = dieselCount;
        terceiro = 'Álcool';
        terceiroCount = alcoolCount;
elif (primeiro == 'Álcool'):
    if (gasolinaCount > dieselCount):
        segundo = 'Gasolina';
        segundoCount = gasolinaCount;
        terceiro = 'Diesel';
        terceiroCount = dieselCount;
    else:
        segundo = 'Diesel';
        segundoCount = dieselCount;
        terceiro = 'Gasolina';
        terceiroCount = gasolinaCount;
elif (primeiro == 'Diesel'):
    if (gasolinaCount > alcoolCount):
        segundo = 'Gasolina';
        segundoCount = gasolinaCount;
        terceiro = 'Álcool';
        terceiroCount = alcoolCount;
    else:
        segundo = 'Ácool';
        segundoCount = alcoolCount;
        terceiro = 'Gasolina';
        terceiroCount = gasolinaCount;

print(primeiro,'=',primeiroCount);
print(segundo,'=',segundoCount);
print(terceiro,'=',terceiroCount);
print('------------------CRÉDITOS AO DESENVOLVEDOR----------------')
print('Programa realizado por Yuri Conder Roliz Sabbagh');
