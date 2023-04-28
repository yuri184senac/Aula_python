print('VERIFICADOR DE TRIÂNGULOS');
print('- O objetivo deste programa é verificar se os valores inseridos pelo usuário formam um triângulo retângulo');
print('Programa realizado por Yuri Conder Roliz Sabbagh');

# ENTRADA
lado = ['a', 'b', 'c'];
valorLado = [];
for i in range(len(lado)):
    valorLado.insert(i, int(input(f' Insira o valor do lado {lado[i]} = ')));
    i = i + 1
#VALIDACAO ENTRADA
for i in range(len(valorLado)):
    while valorLado[i] < 0:
        valorLado[i] = int(input(f' Insira um valor maior que zero no lado {lado[i]} = '))
#PROCESSO
hipotenusa = (valorLado[0] ** 2 + valorLado[1] ** 2) ** (1/2);
msg = 'Os catetos inseridos';
print(msg, 'formam um triângulo retângulo') if ( hipotenusa == valorLado[2] ) else print(msg, 'não formam um triângulo retângulo');
