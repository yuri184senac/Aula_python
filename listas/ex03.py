nomes = ['Beto', 'Julia', 'Paula', '', 'Isabela', '']
print(nomes)

# for i in range(len(nomes)):
#     if nomes[i] == '':
#         nomes.remove(i)

# print(nomes)

nomes = [nome for nome in nomes if nome != '']
print(nomes)