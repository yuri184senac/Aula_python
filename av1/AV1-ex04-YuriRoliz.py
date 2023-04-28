print('PROGRAMA QUE CALCULA A MÉDIA ARITIMÉTICA DE IDADES DO GRUPO');
print('1.Insira a quantaidade de idades que quiser');
print('2.Insira um valor negativo para calcular a média aritimética das idades');
print('OBS: Enquanto você não inserir um valor negativo, o programa continua pedindo para inserir idades de outras pessoas !');

idade = 0;
somaIdades = 0;
contador = 0;
while (idade >= 0):
    idade = int(input(f'Insira a idade da pessoa {contador} :'));
    if (idade > 0):
        somaIdades = idade + somaIdades;
        contador = contador + 1;
#SAÍDA
print(f'A média aritimética das idade é {somaIdades/contador: .2f}');
print('------------------CRÉDITOS AO DESENVOLVEDOR----------------')
print('Programa realizado por Yuri Conder Roliz Sabbagh');
