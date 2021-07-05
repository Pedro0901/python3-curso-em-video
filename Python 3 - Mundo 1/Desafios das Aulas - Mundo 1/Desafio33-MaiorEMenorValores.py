'''
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
A = int(input('Digite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
C = int(input('Digite o terceiro valor: '))

Menor = A

if B < A and B < C:
	Menor = B
if C < A and C < B:
	Menor = C

Maior = A

if B > A and B > C:
	Maior = B
if C > A and C > B:
	Maior = C

print('\nmenor valor digitado foi {}'.format(Menor))
print('\nO maior valor digitado foi {}'.format(Maior))
