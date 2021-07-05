'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''
total = totMil = menor = cont = 0

barato = ' '
while True:
	produto = str(input('Nome do Produto: ')).strip()
	preco = float(input('Preço: R$'))
	cont += 1
	total += preco
	if preco > 1000:
		totMil += 1
	if cont == 1:
		menor = preco
		barato = produto
	else:
		if preco < menor:
			menor = preco
			barato = produto
	resp = ' '
	while resp not in 'SN':
		resp = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
		print('\n')
	if resp == 'N':
		break
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'{totMil} produtos custam mais de R$1000.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}') 
