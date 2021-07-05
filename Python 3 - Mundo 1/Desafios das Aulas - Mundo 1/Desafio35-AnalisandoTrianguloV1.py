'''
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
A = int(input('Informe o comprimento da primeira reta: '))
B = int(input('Informe o comprimento da segunda reta: '))
C = int(input('Informe o comprimento da terceira reta: '))

if A < B + C and B < A + C and C < A + B:
	print('\nOs segmentos acima PODEM FORMAR triângulo!')
else:
	print('\nOs segmentos acima NÃO PODEM FORMAR triângulo!')
