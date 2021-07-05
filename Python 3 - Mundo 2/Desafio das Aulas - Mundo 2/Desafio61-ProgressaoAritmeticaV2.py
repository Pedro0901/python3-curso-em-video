'''
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
print('Gerador de P.A')
print('-=-=-=-=-=-=-=-=')

primeiro = int(input('\nPrimeiro termo: '))
razao = int(input('\nRazão: '))
termo = primeiro
cont = 1

while cont <= 10:
	print('{} → '.format(termo), end='')
	termo += razao
	cont += 1
print('FIM')
