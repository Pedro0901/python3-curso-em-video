'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''
from datetime import date

atual = date.today().year
nascimento = int(input('Informe sua data de nascimento: '))
idade = atual - nascimento

if idade >= 0 and idade <= 9:
	print('\nSua idade é de {} anos.'.format(idade))
	print('\nCategoria: MIRIM!')
elif idade > 9 and idade <= 14:
	print('\nSua idade é de {} anos.'.format(idade))
	print('\nCategoria: INFANTIL!')
elif idade > 14 and idade <= 19:
	print('\nSua idade é de {} anos.'.format(idade))
	print('\nCategoria: JÚNIOR!')
elif idade > 19 and idade <= 25:
	print('\nSua idade é de {} anos.'.format(idade))
	print('\nCategoria: SÊNIOR!')
elif idade > 25:
	print('\nSua idade é de {} anos.'.format(idade))
	print('\nCategoria: MASTER!')
else:
	print('\nIdade inválida!')
