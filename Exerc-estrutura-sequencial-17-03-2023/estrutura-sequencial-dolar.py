#Yuri Conder Roliz Sabbagh
#Exercicio-de-estrutura-Sequencial

#ENTRADA DE DADOS
print('Bem vindo ao meu conversor de dolar');
print('INSTRUÇÕES DE USO:');
print('1.Primeiro insira a contação atual do dólar $');
print('2.Informe a quantidade dólares disponíveis');
print('');
cotacao_dolar_real = float(input('Nós informe o valor da cotação atual do dólar R$ '));
qtde_dolares = float(input('Quantia em dólar $ '));
#PROCESSO DE DADOS
qtde_real = cotacao_dolar_real * qtde_dolares;
#SAÍDA DE DADOS
print('Quantia em real -> R$ %.2f'%(qtde_real));

