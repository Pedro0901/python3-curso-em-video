'''
Exercicio Python 113: Reescreva a função leiaInt() que
fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite
e crie também uma função leiaFloat() com a mesma funcionalidade
'''
def leiaInt(msg):
	while True:
		try:
			n = int(input(msg))
		except (ValueError, TypeError):
			print('ERRO: Por favor digite um número inteiro válido.')
			continue #Para jogar novamente pro while
		except KeyboardInterrupt:
			print('Usuário preferiu não digitar esse número.')
			return 0
		else:
			return n


def leiaFloat(msg):
	while True:
		try:
			n = float(input(msg))
		except (ValueError, TypeError):
			print('ERRO: Por favor digite um número inteiro válido.')
			continue #Para jogar novamente pro while
		except KeyboardInterrupt:
			print('Usuário preferiu não digitar esse número.')
			return 0
		else:
			return n


n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')
