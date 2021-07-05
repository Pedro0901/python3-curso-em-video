'''for c in range(1, 5):
	n = int(input('Digite um valor: '))
print('FIM')
 * Usamos for quando sabemos o inicio e o final *
'''

#Usamos while quando nao sabemos o final
n = 1

# FLAG - Condição de parada - PONTO DE PARADA
while n != 0:
	n = int(input('Digite um valor: '))
print('FIM')

# ------------------------------ #
'''r = 'S'
while r == 'S':
	n = int(input('Digite um valor: '))
	s = str(input('Deseja continuar [S/N]? ')).upper()
print('FIM')'''

# ------------------------------ #
n = 1
par = impar = 0

while n != 0:
	n = int(input('Digite um valor: '))
	if n != 0:
		if n % 2 == 0:
			par += 1
		else:
			impar += 1
print('Você digitou {} numeros pares, e {} numeros impares!'.format(par, impar))
