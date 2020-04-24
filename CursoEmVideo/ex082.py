'''valores = []
impar = []
par = []
while True:
    n = int(input('Digite um valor: '))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Ss':
        valores.append(n)
        if n % 2 == 0:
            par.append(n)
        elif n % 2 == 1:
            impar.append(n)
    else:
        break
print(f'Os valores digitados foram {valores} \nOs valores pares digitados foram {par} \nOs valores ímpares digitados foram {impar}.')
'''

num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('* * * ' * 7)
print(f'Os valores digitados foram {num} \nOs valores pares foram {pares} \nOs valores ímpares foram {impares}.')
