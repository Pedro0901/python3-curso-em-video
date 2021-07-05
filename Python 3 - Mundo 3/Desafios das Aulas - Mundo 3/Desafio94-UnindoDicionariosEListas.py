'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
'''
galera = list()
pessoa = dict()
soma = media = 0

while True:
	pessoa.clear()
	pessoa['Nome'] = str(input('Nome: '))

	while True:
		pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
		if pessoa['Sexo'] in 'MF':
			break
		print('ERRO! Por favor, digite apenas M ou F.')

	pessoa['Idade'] = int(input('Idade: '))
	soma += pessoa['Idade']
	galera.append(pessoa.copy())
	while True:
		resp = str(input('Quer continuar? [S/N] ')).upper()[0]
		if resp in 'SN':
			break
		print('ERRO! Responda apenas com S ou N.')
	if resp == 'N':
		break

print('=-' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')

for p in galera:
	if p['Sexo'] == 'F':
		print(f'{p["Nome"]} ', end='')

print()
print(f'Lista das pessoas que estão acima da média: ', end='')

for p in galera:
	if p['Idade'] >= media:
		print('    ')
		for k, v in p.items():
			print(f'{k} = {v}; ', end='')
		print()
print('<<< ENCERRADO! >>>')
		
