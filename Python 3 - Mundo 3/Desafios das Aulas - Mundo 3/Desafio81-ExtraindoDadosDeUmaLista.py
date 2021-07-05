'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                 
Depois disso, mostre:

A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

num = []

while True:
	num.append(int(input('Digite um número: ')))
	escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()
	if escolha in 'Nn':
		break
print('=-' * 30)
print(f'Foram digitados {len(num)} números!')
num.sort(reverse=True)
print(f'A lista de valores em ordem decrescente são: {num}')
if 5 in num:
	print('O número 5 faz parte da lista!')
else:
	print('O número 5 NÃO faz parte da lista!')
print('=-' * 30)
