'''
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randrange

# Aleatoriza numeros
Num = randrange(0,5)

# Pede numero ao usuário
X = int(input('Tente descobrir qual foi o número escolhido pelo computador: '))

# Mostra o numero escolhido pelo computador
print('\nO numero escolhido pelo computador foi: {}'.format(Num))

# If para resultados
if Num == X:
	print('\nParabéns, você acertou!')
else:
	print('\nVocê errou! Tente novamente.')
