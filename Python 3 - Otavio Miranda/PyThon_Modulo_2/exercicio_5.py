produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

import copy

novos_produtos = [
    {**p, 'preco': p['preco'] * 1.1} for p in 
copy.deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
    reverse=True
)

print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')