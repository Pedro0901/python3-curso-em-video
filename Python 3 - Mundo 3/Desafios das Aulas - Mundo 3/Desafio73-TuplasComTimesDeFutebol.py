'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Bragantino.

obs.: Usarei a tabela do Campeonato Brasileiro de 2020.
'''
times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
		'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino',
		'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport',
		'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

print('=-'*30)
print(f'Lista de times do Brasileirão: {times}')
print('=-'*30)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('=-'*30)
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print('=-'*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*30)
print(f'O Bragantino está na {times.index("Bragantino") + 1}ª posição.')
