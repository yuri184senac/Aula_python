#Exercicio 06
import math
#Verificar a condição de existência do triângulo
#Entrada  de dados
a=int(input('Insira um valor para o lado a:'));
b=int(input('Insira um valor para o lado b:'));
c=int(input('Insira um valor para o lado c:'));
if ( ( (abs(b-c) < a) and (a < (b+c)) ) and ( (abs(a-c) < b) and (b < (a+c)) ) and ( (abs(a-b) < c) and (c < (a+b)) ) ):
    print('TRIÂNGULO EXISTENTE');
else:
    print('TRIANGULO NÃO EXISTENTE');