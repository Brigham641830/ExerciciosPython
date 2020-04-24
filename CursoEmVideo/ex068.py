from random import randint

escolha_jogador = int(input('Escolha um número de 0 a 10: '))
escolha_computador = randint(0, 10)
opcao = str(input('Impar ou Par? [I/P] ').upper().strip()[0])
soma = escolha_jogador + escolha_computador
vitoria = 0
ganhador = 'jogador'

while ganhador == 'jogador':
    if opcao in 'Pp' and soma % 2 == 0:
        vitoria += 1
        ganhador = 'jogador'
        escolha_jogador = int(input('Escolha um número de 0 a 10: '))
        opcao = str(input('Impar ou Par? [I/P]').upper().strip()[0])
    elif opcao in 'Ii' and soma % 2 == 1:
        vitoria += 1
        ganhador = 'jogador'
        escolha_jogador = int(input('Escolha um número de 0 a 10: '))
        opcao = str(input('Impar ou Par? [I/P]').upper().strip()[0])
    else:
        print(f'O computador ganhou! Você venceu {vitoria} vezes.')
        ganhador = 'computador'
        if soma % 2 == 0:
            print(f'Você escolheu {escolha_jogador} e o computador {escolha_computador}, somando {soma} que é PAR, você perdeu!')
        elif soma % 2 == 1:
            print(f'Você escolheu {escolha_jogador} e o computador {escolha_computador}, somando {soma} que é IMPAR, você perdeu! ')
