total18 = totalH = totalM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]').upper().strip()[0])
    if idade >= 18:
        total18 += 1
    if sexo in 'Mm':
        totalH += 1
    if sexo in 'Ff' and idade < 20:
        totalM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]').upper().strip()[0])
    if resp == 'N':
        break
print(f'O total de {total18} maiores de idade, {totalH} homens e {totalM20} mulheres abaixo de 20 anos.')
