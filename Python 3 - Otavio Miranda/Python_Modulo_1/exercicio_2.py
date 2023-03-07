"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

numero_int = input('Digite um número inteiro: ')
if numero_int.isdigit():

    numero_int = int(numero_int)
    numero_type = type(numero_int)
    numero_check = (numero_int % 2)
    print(numero_check)

    if numero_type == int:
        print(f'Parabens você digitou {numero_int} que é um número inteiro')
    else:
        print(f'Algo errado, você digitou um(a) {numero_type} ao inves de um número inteiro')

    if numero_check == 1:
        print('O número que você digitou é IMPAR')    
    else:
        print('O número que você digitou é PAR')    

else:
    print('Você não digitou um número inteiro')            

