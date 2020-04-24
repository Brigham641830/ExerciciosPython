numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = 0
continua = 'S'
while True:
    if continua in 'Ss':
        if escolha in range(0, 20):
            escolha = int(input('Escolha um número entre 0 e 20: '))
            escolhido = numeros[escolha]
            print(f'O numero que você digitou foi o {escolhido}')
            continua = str(input('Quer continuar? [S/N] ').upper().strip()[0])
    else:
        break
