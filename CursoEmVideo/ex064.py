cont = n = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma = soma + n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('A quantidade de números digitados foi {} e a soma deles é {}.'.format(cont, soma))
