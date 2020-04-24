produtos = ('Caderno', 10.00,
           'Caneta', 6.00,
           'Notebook', 2500.00,
           'Esquadro', 3.00,
           'Compasso', 9.99,
           'Livros', 200.00,
           'Kindle', 450.00,
            'Mochila', 150.00)
print('-' * 30)
print(f'{"Preços da Loja Vilete":^30}')
print('-' * 30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<20}', end='')
    else:
        print(f'R${produtos[pos]:>8.2f}')
print('-' * 30)
