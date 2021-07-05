from funcoes import *
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
	criarArquivo(arq)

while True:
	resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Programa'])
	if resposta == 1:
		#OPÇÃO DE LISTAR O CONTEUDO DE UM ARQUIVO
		lerArquivo(arq)
	elif resposta == 2:
		cabeçalho('NOVO CADASTRO')
		nome = str(input('Nome: '))
		idade = leiaInt('Idade: ')
		cadastrar(arq, nome, idade)
	elif resposta == 3:
		cabeçalho('Saindo do sistema... Até logo!')
		break
	else:
		print('ERRO! Digite uma opção válida!')
	sleep(2)
