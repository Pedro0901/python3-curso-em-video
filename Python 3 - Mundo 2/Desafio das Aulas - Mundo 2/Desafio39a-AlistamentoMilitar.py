'''
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem, o sexo, e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
sexo = str(input('\nInforme o seu sexo: ')).upper()
print('\nQuem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))

if sexo == 'MASCULINO' or sexo == 'M':
	if idade == 18:
		print('\nVocê tem que se alistar IMEDIATAMENTE!')
	elif idade < 18:
		saldo = 18 - idade 
		print('\nAinda faltam {} anos para o alistamento!'.format(saldo))
		ano = atual + saldo
		print('\nSeu alistamento será em {} ano.'.format(ano))
	elif idade > 18:
		saldo = idade - 18
		print('\nVocê ja deveria ter se alistado a {} anos.'.format(saldo))
		ano = atual - saldo
		print('\nSeu alistamento foi em {}'.format(ano))
elif sexo == 'FEMININO' or sexo == 'F':
	print('\nO alistamento para o sexo feminino NÃO É OBRIGATÓRIO!')
else:
	print('\nResposta inválida')
