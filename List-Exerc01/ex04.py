#Faça um programa que calcule o fatorial de um número positivo informado pelo usuário:
numero = 5
numeroDeEntrada = numero
fatorial = numero
while fatorial != 1:
    fatorial = fatorial -1
    numero = fatorial * numero

resultado = numero
print(f'A fatorial do número {numeroDeEntrada} é igual à {numero}')