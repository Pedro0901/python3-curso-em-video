'''
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
e que se encontram no intervalo de 1 até 500.
'''
soma = 0 #Aculumador
cont = 0 #Contador
for c in range(1, 501, 2):
	if c % 3 == 0:
		cont = cont + 1 
		soma = soma + c
print('A soma de todo os {} valores solicitados é: {}'.format(cont, soma))
