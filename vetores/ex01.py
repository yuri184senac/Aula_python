vetor = [3,5,0,1,4,2]


print(vetor)
i = 1;
x = 0;

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


