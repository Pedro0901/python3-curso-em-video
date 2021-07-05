'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele 
marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que 
algum dado não tenha sido informado corretamente.
'''

def ficha(nome='', gols=0):
	print('-' * 40)
	if nome == '':
		nome = '<desconhecido>'
	if gols == '':
		gols = 0
	print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
	
	
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: ')).strip()
ficha(nome, gols)
