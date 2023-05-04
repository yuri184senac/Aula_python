print('ESTE PROGRAMA MOSTRARÁ A SEQUÊNCIA DE FIBONACCI:');
#ENTRADA
num = int(input('Insira um número inteiro maior do que zero'));
numAntes = 0;
numAtual = 1;
while (num < 0):
    num = int(input('Insira um número inteiro maior que zero'));

#PROCESSO
print(numAtual);
while (numAtual < num):
    soma = numAtual + numAntes;
    numAntes = numAtual;
    numAtual = soma;
    print(soma)

print('------------------CRÉDITOS AO DESENVOLVEDOR----------------')
print('Programa realizado por Yuri Conder Roliz Sabbagh !');



