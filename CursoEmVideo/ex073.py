times = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense',\
        'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',\
        'Bahia', 'Vasco da Gama', 'Atlético Minieiro', 'Fluminense',\
        'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí'
print(times)
primeiros = print(f'Os 5 primeiros times classificados no Brasileirão foram: {times[0:5]}')
ultimos = print(f'Os 4 ultimos colocados foram: {times[-4:]}')
ordem = print(f'Os times organizados em ordem alfabética ficam listados da seguinte forma: {sorted(times)}')
posição = print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
