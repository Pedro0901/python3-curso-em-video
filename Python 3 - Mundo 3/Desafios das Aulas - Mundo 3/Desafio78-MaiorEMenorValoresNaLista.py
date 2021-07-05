'''Exercício Python 078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado 
as suas respectivas posições na lista.
'''
listaum = []
maior = 0
menor = 0

for c in range(0, 5):
	listaum.append(int(input(f'Digite um valor para a posição {c}: ')))
	if c == 0:
		maior = menor = listaum[c]
	else:
		if listaum[c] > maior:
			maior = listaum[c]
		if listaum[c] < menor:
			menor = listaum[c]

print('=-' * 30)
print(f'Você digitou os valores: {listaum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for i, v in enumerate(listaum):
	if v == maior:
		print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')

for i, v in enumerate(listaum):
	if v == menor:
		print(f'{i}... ', end='')
print()
