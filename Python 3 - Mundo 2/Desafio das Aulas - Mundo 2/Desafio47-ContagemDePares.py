'''
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
for c in range(2, 52, 2):
	if c % 2 == 0:
		print(c, end=' ')
