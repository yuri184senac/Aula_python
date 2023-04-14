#Escreva um programa que imprima todos os números pares compreendidos entre 85 e 907. O programa também deve calcular a soma destes valores:
soma = 0;
numero = 85;
while (numero <= 907):
    if (numero % 2 == 0):
        print(numero);
        soma = numero + soma;
        numero = numero + 1;
    else:
        numero = numero + 1;

print(f'A soma de todos os números listados acima é igual: {soma}');