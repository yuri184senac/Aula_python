numeros = [1,2,3,4,5,6,7]

for x in range(len(numeros)):
    numeros[x] = numeros[x]**2
x = x + 1
print(numeros)