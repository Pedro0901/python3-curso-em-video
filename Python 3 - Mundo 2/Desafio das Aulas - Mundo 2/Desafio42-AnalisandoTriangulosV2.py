'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''
A = int(input('Informe o comprimento da primeira reta: '))
B = int(input('Informe o comprimento da segunda reta: '))
C = int(input('Informe o comprimento da terceira reta: '))

if A < B + C and B < A + C and C < A + B:
	print('\nOs segmentos acima PODEM FORMAR triângulo!')
	if A == B == C:
		print('\nEQUILÁTERO! Todos os lados são iguais.')
	elif A == B != C or B == C != A or C == A != B:
		print('\nISÓSCELES! Dois lados são iguais, e um diferente.')
	elif A != B != C:
		print('\nESCALENO! Todos os lados são diferentes.')
else:
	print('\nOs segmentos acima NÃO PODEM FORMAR triângulo!')
