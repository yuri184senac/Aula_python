#GRUPO
#Guilherme
#João Gabriel
#Thiago Luiz
#Yuri Roliz

print('Validador de senha')
senha = input('Informe a senha: ');

def verLetraMaiu(senha):
    if senha.lower() == senha:
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
        
        return False
    else:
        return True

def verNumero(senha): 
      for char in senha:
        if char.isdigit():
            return True


def validarSenha(senha):
    if (verTamanho(senha) and verLetraMaiu(senha) and verSeComecaNumero(senha) and verNumero(senha)):
        print('senha é válida')
    else:
        print('senha é inválida')

validarSenha(senha)