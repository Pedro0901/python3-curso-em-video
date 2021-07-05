'''
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

[ FORMA ALTERNATIVA ]
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('\nO inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
	print('\nTemos um palíndromo!')
else:
	print('\nA frase digitada não é um palíndromo!')
 
