import math
#ENTRADA:
print('PROGAMA QUE CALCULA A ÁREA E HIPOTENUSA DE UM TRIÂNGULO:')

a = float(input('Informe o valor do cateto a'))
b = float(input('Infome o valor do cateto b'))


area = (a * b)/2

raiz = a**2 + b**2

c = math.sqrt(raiz)

print('O valor da hipotenusa é igual a %.2f' %(c))


