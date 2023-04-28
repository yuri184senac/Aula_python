print('PROGRAMA QUE CALCULA E APRESENTA TODOS OS DIVISORES DO NÚMERO DA SUA ESCOLHA');

#ENTRADA
numero = int(input('Insira por favor o número desejado: '));
divisor = numero;
#PROCESSO E SAÍDA DE DADOS
print('Lista de todos os divisores do número', numero, ':')
while divisor > 0:
    if(numero % divisor == 0):
        print(f'{numero/divisor: .0f}');
    divisor = divisor - 1;
print('------------------CRÉDITOS AO DESENVOLVEDOR----------------')
print('Programa realizado por Yuri Conder Roliz Sabbagh');