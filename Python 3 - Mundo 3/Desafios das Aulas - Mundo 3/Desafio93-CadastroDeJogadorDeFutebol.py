'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
dicio = dict()
partidas = list()

dicio['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dicio["Nome"]} jogou? '))
for c in range(0, tot):
	partidas.append(int(input(f'	Quantos gols na partida {c+1}? ')))
dicio['Gols'] = partidas[:]
dicio['Total'] = sum(partidas)
print('=-' * 30)
print(dicio)
print('=-' * 30)

for k, v in dicio.items():
	print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {dicio["Nome"]} jogou {len(dicio["Gols"])} partidas.')

for i, v in enumerate(dicio['Gols']):
	print(f' => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dicio["Total"]}')
