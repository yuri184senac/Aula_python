
print('Validador de senha')
senha = input('Informe a senha: ');

def verLetraMaiu(senha):
    if senha.lower() == senha:
        print('sua senha não tem letra Maiúscula')
        return False 
    else:
        return True
      

def verTamanho(senha):
    if (len(senha) <= 8 and len(senha) >=6):
        return True
    else:
        return False

def verSeComecaNumero(senha):
    if senha[0].isdigit():
        print('primeiro item é um numero')
        return False
    else:
        return True

def verNumero(senha): 
    for i in senha:
        if i.isdigit():
            return True
        else:
            print('erro: A senha não tem números')
            return False



# def validarSenha(senha):
#     if (verTamanho(senha) and verLetraMaiu(senha) and verSeComecaNumero(senha) and verNumero(senha)):
#         print('SENHA VÁLIDA')
#     else:
#         print('SENHA INVÁLIDA')

