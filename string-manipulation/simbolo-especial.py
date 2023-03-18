caracteres_especial = ['@', '!']
frase = '@la!2'
count_especial = 0

for i in caracteres_especial:
    if frase.count(caracteres_especial[i]):
        count_especial =+1

print(count_especial)