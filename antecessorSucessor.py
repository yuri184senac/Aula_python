#ENTRADA
print("Bem vindo ao programa que calcula o antecessor e sucessor de um número");
num1 = int(input("Insira um número inteiro e descubra o seu antecessor e sucessor : "));

#PROCESSO
 #Essa resolução ocupa mais espaço na memória
antecessorNum1 = num1 - 1
sucessorNum1 = num1 + 1
#SAIDA
print(f'O successor do número {num1} é {sucessorNum1} e o seu antecessor é {antecessorNum1}');

#Solução que consome menos memória
num = int(input("Insira um número inteiro e descubra o seu antecessor e sucessor :"));
print(f'O sucessor do número {num} é {num+1} e o seu antecessoer é {num-1}');