#Participantes:
# João Saad
# Thiago Braga
# Guilherme Lopes
# Yuri Roliz

resultado = 1;
while True:
    n1 = int(input('Informe o número:'))
    potencia = int(input('Informe o valor da potência: '))  
    if (n1 > 1 and potencia >=2): break

    else:
        print('Os valores inseridos não são permetidos')
    
    
for i in range(potencia):
        resultado = n1*resultado
        
print(resultado)

