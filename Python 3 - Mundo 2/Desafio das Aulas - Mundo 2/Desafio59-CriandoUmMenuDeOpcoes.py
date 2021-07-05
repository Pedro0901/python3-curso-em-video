'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
	print('''\n	[ 1 ] Somar.
	[ 2 ] Multiplicar.
	[ 3 ] Maior.
	[ 4 ] Novos números.
	[ 5 ] Sair do programa.''')
	opcao = int(input('\n>>>>>> Qual é a sua opção? '))
	if opcao == 1:
		soma = n1 + n2
		print('\nA soma entre {} + {} é {}.'.format(n1, n2, soma))
	elif opcao == 2:
		produto = n1 * n2
		print('\nO resultado de {} * {} é {}.'.format(n1, n2, produto))
	elif opcao == 3:
		if n1 > n2:
			maior = n1
		else:
			maior = n2
		print('\nEntre {} e {} o maior valor é {}.'.format(n1, n2, maior))
	elif opcao == 4:
		print('\nInforme os numeros novamente: ')
		n1 = int(input('Primeiro valor: '))
		n2 = int(input('Segundo valor: '))
	elif opcao == 5:
		print('\nFinalizando...')
	else:
		print('\nOpção inválida!')
	print('=-=' * 10)
	sleep(2)
print('Fim do programa! Volte sempre!')
