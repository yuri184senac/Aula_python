print('Bem vindo a calculadora de hipotenusa');
input('Pressione enter para continuar...');

#ENTRADA
print('Insira a medida em centímetros de dois lados de um triângulo retângulo:');
a = float(input('Lado a: '));
b = float(input('Lado b: '));
#TRATAMENTO DE DADOS
while (a < 0 or b < 0):
    print('Por favor, insira um valor positivo');
    a = float(input('Cateto a: '));
    b = float(input('Cateto b: '));
#PROCESSO
hipotenusa = (a ** 2 + b ** 2) ** (1/2);
#SAÍDA
print(f'O valor da hipotenusa é igual a: {hipotenusa: .2f} cm');
print('------------------CRÉDITOS AO DESENVOLVEDOR----------------')
print('Programa realizado por Yuri Conder Roliz Sabbagh');