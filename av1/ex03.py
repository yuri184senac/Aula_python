print('PROGRAMA QUE LÊ UM NÚMERO INTEIRO QUALQUER MENOR QUE 1000 E APRESENTE TODOS OS N ÍMPARES DE 1 ATÉ N');

#ENTRADA
numero = int(input('Insira um número qualquer menor do que 1000: '));

#VERIFICAÇÃO
while numero > 1000:
    numero = int(input('Insira um número qualquer menor do que 1000: '));

#SAÍDA
print('');
print('Listagem de todos os números ímpares menores que',numero);
print('----------------------------------------------------------')
for i in range(1, numero):
    if(i % 2):
        print(i);

print('------------------CRÉDITOS AO DESENVOLVEDOR----------------')
print('Programa realizado por Yuri Conder Roliz Sabbagh');