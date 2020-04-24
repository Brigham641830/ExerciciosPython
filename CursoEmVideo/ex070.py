total = totmil = menor = cont = 0
barato = ''
print('-' * 25)
print('{:*^25}'.format('LOJA DO VILETE JUDEU'))
print('-' * 25)

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim do programa.')
print(f'O total de compras foi {total:.2f}')
print(f'Temos {totmil} produtos que custaram mais de R$1000,00')
print(f'O prouto mais barato foi {barato}')
