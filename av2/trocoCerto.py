print('MERCADO');

produto_valor= float(input('Infome o valor do produto R$:'))
valor_pago = float(input('Informe o valor pago em dinheiro R$:'))
troco = valor_pago - produto_valor
meuTroco = 'Seu troco é' 

#processo
def separaCedulas(valor):
  global meuTroco 
  n100 = valor // 100
  resto = valor % 100

  n50 = resto // 50
  resto1 = resto % 50

  n20 = resto1 // 20
  resto2 = resto1 % 20

  n10 = resto2 // 10
  resto3 = resto2 % 10

  n5 = resto3 // 5
  resto4 = resto3  % 5

  n2 = resto4 // 2
  n1 = resto4 // 1

  if (n100 != 0):
    meuTroco += f' {n100}x notas de 100'

  if (n50 != 0):
    meuTroco += f' {n50}x notas de 50'

  if (n20 != 0):
    meuTroco += f' {n20}x notas de 20'

  if (n10 != 0):
    meuTroco += f' {n10}x notas de 10'

  if (n5 != 0):
    meuTroco += f' {n5}x notas de 5'
  
  if (n2 != 0):
    meuTroco += f' {n2} notas de 100'
  
  if (n1 != 0):
    meuTroco += f' {n1} notas de 1'
    

separaCedulas(troco)
print(meuTroco)




