#ENTRADA
#Primeiro vamos ter
operadores = ['^', 'v', 's'];
expressao = 'p^qss';

operadores_salvos = [];
contador = 0
for i in (range(len(expressao))):
    if expressao.count('q'):
        contador = contador + 1;

print(contador)



