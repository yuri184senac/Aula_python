#QUESTÃO 02:
#frase = "CompreiUmCarro2020!EvendiPorR$20mil"
frase = input("Insira uma frase com minimo de 20 caracteres")
if frase<20:
    print('tem menos que o desejado')
#LETRA A
print(f'O tamanho da frase é de {len(frase)} caracteres')
#---------------------------------------------------
#LETRA B
count_letra = 0;
count_numero = 0;
count_simbolo = 0

for i in range(len(frase)):
    if frase[i].isalpha():
        count_letra=+1
    if frase[i].isalnum():
        count_numero=+1

print(f'Quantidade total de letras = {count_letra}');
print(f'Quantidade total de números = {count_numero}');
#print(f'quantidade de o é igual a {nome.count()}');
#---------------------------------------------------
#LETRA C
print(f' A quantidade de ocorrências do primeiro caractere é igual a {frase.count(frase[0])}');

#LETRA D
print(f' 1. Frase maiúscula: "{frase.upper()}"')
print(f' 1. Frase minúscula: "{frase.lower()}"')