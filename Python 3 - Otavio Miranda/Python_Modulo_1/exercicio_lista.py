import os

lista_compras= ['Arroz', 'Feijão', 'Macarrao']
item_inserir = ''
item_deletado = ''
lista_antiga = []

os.system('cls')

while True:
    pergunta = input('Selecione uma opção: [i]nserir, [a]pagar, [l]istar, [s]air :  ')
    pergunta.lower()
    if pergunta == 'i':
        item_inserir = input('Qual item vai inserir: ')
        lista_compras.append(item_inserir)
    elif pergunta == 'a':
        try:
            item_deletado = input('Informe o item deletado: ')
            item_deletado = int(item_deletado)
            if type(item_deletado) == int:
                lista_antiga = lista_compras
                lista_antiga = tuple(lista_antiga)
                lista_compras.pop(item_deletado)
                print(f'Essa é a lista antiga {lista_antiga}')
                print(f'Essa é a lista atualizada {lista_compras}')
        except:
            print('Digite apenas número para apagar um indice')
    elif pergunta == 'l':
        for item in enumerate(lista_compras):
            print(item)
    elif pergunta == 's':
        break 
    else:
        print('Digite [i], [a], [l] ou [s]')   

