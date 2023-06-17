#Participantes:
# João Saad
# Thiago Braga
# Guilherme Lopes
# Yuri Roliz
salario = float(input('Informe o seu salário R$:'));
tempo = int(input('informe o tempo de serviço:'))

def calcula_bonus(sal, tempo):
    novoSalario = 0
    if (tempo >= 10):
        novoSalario = sal + (25*sal)/100
    elif (tempo >= 7):
        novoSalario = sal + (20*sal)/100
    elif (tempo >= 4):
        novoSalario = sal + (15*sal)/100
    elif (tempo >= 1):
        novoSalario = sal + (10*sal)/100
    elif (tempo < 1):
        novoSalario = sal + (5*sal)/100
        
    print(f'O novo salário do funcionário é R$:{novoSalario}');
    
calcula_bonus(salario, tempo)

        