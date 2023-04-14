import math
#Elaborar um programa que leia a medida de um raio de um círculo e efetue o cálculo da sua área

#Entrada de dados
raio = int(input('Informe a medida do raio do círculo: '));
area = math.pi * (raio **2);
print(f'A área do círculo é igual a {area: .2f}');
