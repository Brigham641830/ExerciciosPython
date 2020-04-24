valores = list()
maior = menor = 0
for v in range (0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v+1}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}...', end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}...', end='')

