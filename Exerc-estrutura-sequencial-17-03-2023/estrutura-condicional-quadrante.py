#Yuri Conder Roliz Sabbagh
#Entrada de dados
x = float(input('Informe o valor de x: '));
y = float(input('Informe o valor de y: '));

if ((x > 0) and (y > 0)):
    print('Q1');
elif((x < 0) and (y > 0)):
    print('Q2');
elif ((x < 0) and (y < 0)):
    print('Q3');
elif ((x > 0) and (y < 0)):
    print('Q4');
elif ((x == 0) and (y == 0)):
    print('Origem');
elif((x == 0) and ((y > 0)) or (y < 0)):
    print('Eixo Y');
elif((x > 0 ) or (x < 0) and (y == 0)):
    print('Eixo X');
