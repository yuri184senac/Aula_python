
print('Validador de senha')
senha = input('Informe a senha: ');

def verLetraMaiu(senha):
    if senha.lower() == senha:
        print('sua senha não tem letra Maiúscula')
        return False 
      

def verTamanho(senha):
    if (len(senha) <= 8 and len(senha) >=6):
        return True
    else:
        return False

def verSeComecaNumero(senha):
    if senha[0].isDigit():
        print('primeiro item é um numero')
        return False

def verNumero(senha):
    for i in senha:
        if senha[i].isDigit():
            return True
        else:
            print('erro: A senha não tem números')
            return False


def validarSenha(senha):
    
