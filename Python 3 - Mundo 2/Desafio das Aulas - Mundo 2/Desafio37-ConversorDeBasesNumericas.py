'''
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''
num = int(input('Digite um numero inteiro: '))
print('''\nEscolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('\nSua opção: '))

if opcao == 1:
	print('\n{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
	print('\n{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
	print('\n{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
	print('\nOpção inválida. Tente novamente!')
