#GRUPO
#Guilherme
#João Gabriel
#Thiago Luiz
#Yuri Roliz
print('MERCADO');

produto_valor= float(input('Infome o valor do produto R$:'))
valor_pago = float(input('Informe o valor pago em dinheiro R$:'))
troco = valor_pago - produto_valor
meuTroco = 'No troco você vai precisar de \n  ' 

#processo
def separaCedulas(valor):
  global meuTroco 

  n20 = valor // 20
  resto3 = valor % 20

  n10 = resto3 // 10
  resto4 = resto3 % 10

  n5 = resto4 // 5
  resto5 = resto4  % 5

  n2 = resto5 // 2
  n1 = resto5 % 2


  if (n20 != 0):
    meuTroco += f' {n20:.0f} x notas de 20 \n '

  if (n10 != 0):
    meuTroco += f' {n10:.0f} x notas de 10 \n '

  if (n5 != 0):
    meuTroco += f' {n5:.0f} x notas de 5 \n '
  
  if (n2 != 0):
    meuTroco += f' {n2:.0f} x notas de 2 \n '
  
  if (n1 != 0):
    meuTroco += f' {n1:.0f} x notas de 1 \n '
    

separaCedulas(troco)
print(meuTroco)




