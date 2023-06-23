#Grupo:

print('MERCADO');

produto_valor= float(input('Infome o valor do produto R$:'))
valor_pago = float(input('Informe o valor pago em dinheiro R$:'))
troco = valor_pago - produto_valor
meuTroco = 'Seu troco é' 

#processo
def separaCedulas(valor):
  global meuTroco 

  n200 = valor // 200
  resto = valor % 200

  n100 = resto // 100
  resto1 = resto % 100

  n50 = resto1 // 50
  resto2 = resto1 % 50

  n20 = resto2 // 20
  resto3 = resto2 % 20

  n10 = resto3 // 10
  resto4 = resto3 % 10

  n5 = resto4 // 5
  resto5 = resto4  % 5

  n2 = resto5 // 2
  n1 = resto5 // 1

  if (n200 != 0):
    meuTroco += f' {n200:.0f} x notas de 200'

  if (n100 != 0):
    meuTroco += f' {n100:.0f} x notas de 100'

  if (n50 != 0):
    meuTroco += f' {n50:.0f} x notas de 50'

  if (n20 != 0):
    meuTroco += f' {n20:.0f} x notas de 20'

  if (n10 != 0):
    meuTroco += f' {n10:.0f} x notas de 10'

  if (n5 != 0):
    meuTroco += f' {n5:.0f} x notas de 5'
  
  if (n2 != 0):
    meuTroco += f' {n2:.0f} x notas de 100'
  
  if (n1 != 0):
    meuTroco += f' {n1:.0f} x notas de 1'
    

separaCedulas(troco)
print(meuTroco)




