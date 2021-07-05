'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10),
	randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores {n}')
print(f'O menor número foi: {sorted(n)[0]}') #Poderia ter usado o método min(n)
print(f'O maior número foi: {sorted(n)[-1]}') #Poderia ter usado o método max(n)
