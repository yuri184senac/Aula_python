algRomano = input('Insira o número romano:')

lista = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000 
}
numeroRomano = []
numero = []


#CHAR[1]= SIMBOLO ROMANO
#NUM[0] = SIMBOLO ROMANO
def parseToDecimal(algRomano):

    soma = 0
    for char in enumerate(algRomano):    
        for num in lista.items():
            if(num[0] == char[1]):
               numero.append(num[1])

    for i in numero:
        soma = i + soma
    print(soma)
    print(numero)

parseToDecimal(algRomano) 





