"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

cpf = 0
cpf_dez = 0
multiplicador = 10
multiplicador_2 = 11
lista_resultados = []
lista_resultados_2 = []
resultado_1 = 0
resultado_2 = 0
resultado_3 = 0
resultado_4 = 0
primeiro_digito = 0
segundo_digito = 0
i = ''
a = 1
a = int(a)
b = 1
c = 1

cpf = input('Digite seu CPF: ')

# Verifica digitos e faz multiplicação do 0 até o 9
for i in cpf:
    if a < 10:
        resultado_1 = (int(i) * multiplicador)
        lista_resultados.append(resultado_1)
        multiplicador -= 1
        a += 1

for m in lista_resultados:
    resultado_2 = (resultado_2 + m)
resultado_2 = int(resultado_2)
primeiro_digito = ((resultado_2 * 10) % 11)

cpf_dez = cpf + str(primeiro_digito)

for z in cpf_dez:    
    if c < 12:
        resultado_3 = (int(z) * multiplicador_2)
        lista_resultados_2.append(resultado_3)
        multiplicador_2 -= 1
        c += 1

for x in lista_resultados_2:
    resultado_4 = (resultado_4 + x)    
resultado_4 = int(resultado_4)
segundo_digito = ((resultado_4 * 10) % 11)

if primeiro_digito > 9:
    primeiro_digito = 0
elif primeiro_digito <=9:
    primeiro_digito = primeiro_digito

if segundo_digito > 9:
    segundo_digito = '0'
elif segundo_digito <= 9:
    segundo_digito = segundo_digito 


print(lista_resultados)
print(lista_resultados_2)
print(primeiro_digito)
print(segundo_digito)





"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""