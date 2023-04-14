#Yuri Conder Roliz Sabbagh
import math
#Entrada de dados
a = float(input('Valor de a: '));
b = float(input('Valor de b: '));
c = float(input('Valor de c: '));


if (a != 0):
    DELTA = b**2-(4*a*c);
    r1 = ( -b+math.sqrt(DELTA) )/(2*a);
    r2 = ( -b-math.sqrt(DELTA) )/(2*a);
    print('R1 = %.5f' %(r1));
    print('R2 = %.5f' %(r2));
else:
    print('"Impossível calcular 123"');
    