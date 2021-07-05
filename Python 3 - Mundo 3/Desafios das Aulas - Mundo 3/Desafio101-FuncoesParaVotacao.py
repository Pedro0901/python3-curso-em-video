'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber 
como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se
uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
from datetime import date


def linha():
	print('-' * 40)


def voto(nasc):
	if idade < 16:
		return f'Com {idade} anos: NÃO VOTA.'
	elif idade >= 16 and idade < 18:
		return f'Com {idade} anos: VOTO OPCIONAL.'
	elif idade >= 18 and idade < 65:
		return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
	elif idade >= 65:
		return f'Com {idade} anos: VOTO OPCIONAL.'
	

linha()
data_atual = date.today()
ano = int(input('Informe seu ano de nascimento: '))
idade = data_atual.year - ano
print(voto(idade))
