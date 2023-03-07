#função de multiplicação com parametros nao nomeados

def multiplicacao(*args):
    resultad = 1
    for numero in args:
        resultad *= numero
    #print(resultad)    
    return resultad
    
multiplicar = multiplicacao(4, 4, 4)        
print(multiplicar)

#criar função se o numero e par ou impar

def par_impar(nu):
    nu = int(input("Informe um número: "))
    if nu % 2 == 0:
        return True
    return False

print(par_impar(4))
print(par_impar(5))