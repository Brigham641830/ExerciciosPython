cont =  soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999: break
    cont += 1
    soma = soma + n
print(f'A quantidade de números digitados foi {cont} e a soma deles é {soma}.')
