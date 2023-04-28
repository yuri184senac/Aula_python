caracteres_especiais = ['@', '~', '!', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', '\'', '(', ')', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'];

frase = 'yuriconder*@@';
count_especiais = 0;

for i in range(len(caracteres_especiais)):
    if frase.count(caracteres_especiais[i]):
        count_especiais = frase.count(caracteres_especiais[i]) + count_especiais;
i=+1;
print(count_especiais);
print()