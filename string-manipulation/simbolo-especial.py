caracteres_especial = ['@', '~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', '\'', '(', ')', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
frase = 'yuriconder@_123*'
count_especial = 0

for i in range(len(caracteres_especial)):
    if frase.count(caracteres_especial[i]):
        count_especial = frase.count(caracteres_especial[i]) + count_especial;
i=+1
print(count_especial)