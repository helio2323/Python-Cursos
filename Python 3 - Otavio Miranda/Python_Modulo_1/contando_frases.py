frase = 'Python é uma linguagem de programação de alto nível,' \
'interpretada e de código aberto. Ela foi criada no início dos anos' \
'1990 por Guido van Rossum e tem sido amplamente utilizada em muitas' \
'áreas diferentes, incluindo ciência da computação, data science,' \
'desenvolvimento de aplicativos web, automação de tarefas e muito mais.'

i = 0

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    
    if i > 0:
        letra_anterior = frase[i-1]
        if letra_atual >= letra_anterior:
            print(letra_atual, quantas_vezes_letra_apareceu)
            print('A letra atual aparece + vezes que a anterior')



    
    i += 1


