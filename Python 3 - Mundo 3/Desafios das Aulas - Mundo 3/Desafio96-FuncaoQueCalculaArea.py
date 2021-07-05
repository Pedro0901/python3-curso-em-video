'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura (b) e comprimento (h) ) e mostre a área do terreno.
'''
def area(b, h):
	print('-' * 30)
	a = b * h
	print(f'A área de um terreno de {b}x{h} é de: {a}m².')


b = float(input('Largura (m): '))
h = float(input('Comprimento (m): '))
area(b, h)
