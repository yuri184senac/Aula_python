vetor = [23,30,55,3,5,0,1,4,2,100,99,37]
i = 1;
x = 0;
print(vetor)
for i in range(len(vetor)):
    for x in range(len(vetor)):
        if vetor[x] > vetor[i]:
            maior = vetor[x];
            menor = vetor[i];
            vetor[x] = menor;
            vetor[i] = maior;
    i = i + 1;
    x = x + 1;
print(vetor)


