# 5.	Uma seguradora de saúde está oferecendo um plano de saúde promocional
# em que todos os conveniados pagam R$ 100,00 mais um adicional, de
# acordo com sua idade. As regras para esse adicional seguem a tabela abaixo:

print('Estamos oferecendo um plano de saúde promocional, conveniados pagaram R$ 100,00 mais um adicional');

idade = int(input('Qual é a sua idade:'));

if (idade >= 60):
    adicional = 400;
elif (idade > 45):
    adicional = 250;
elif (idade > 30):
    adicional = 130;
elif (idade > 10):
    adicional = 90;
elif (idade <= 10):
    adicional = 60;

print (f'Você pagará R${100+adicional: .2f} reais');