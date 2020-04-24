n = int(input('Digite um número para ver a sua tabuada: '))
multiplicador = 0
while n > 0 and multiplicador <= 10:
    for multiplicador in range (1, 11):
        print(f'{n} x {multiplicador} = {n*multiplicador}')
        multiplicador += 1
    multiplicador = 0
    n = int(input('Digite um número: '))
print('Impossível mostrar a tabuada de números negativos, tabuada encerrada.')
