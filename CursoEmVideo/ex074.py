from random import randint
n = (randint(0,999), randint(0,999), randint(0,999), randint(0,999), randint(0,999))
for num in n:
    print(f'{num} ', end='')
print(f'\nO maior valor sorteado foi {max(n)} e o menor valor foi {min(n)}')
