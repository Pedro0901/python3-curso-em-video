'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
while True:
	n = int(input('Quer ver a tabuada de qual número? '))
	if n < 0:
		break
	print('-'*30)
	for c in range(1, 10):
		print(f'{n} x {c} = {n*c}')
	print('-'*30)
print('\nPROGRAMA TABUADA ENCERRADO. Volte sempre!')
