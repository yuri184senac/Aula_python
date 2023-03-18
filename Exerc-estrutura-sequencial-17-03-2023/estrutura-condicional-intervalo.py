#Entrada de dados
n1 = float(input('Insira um número: '));

if((n1 >= 75) and (n1 <= 100)):
    print('pertence ao intervalo [75, 100]');
elif(n1 >= 50):
    print('pertence ao intervalo [50,75]');
elif(n1 >= 25):
    print('pertence ao intervalo [25, 50]');
elif(n1 >= 0):
    print('pertence ao intervalo [0, 25]');
else:
    print('Não pertence a nenhum dos intervalos');