nome = str(input('Qual é o seu nome? '))

# Condição Simples #
'''
#if nome == 'Pedro':
#	print('Que nome bonito!')
#
#print('Tenha um bom dia, {}!'.format(nome))
'''
# Condição composta #
'''
if nome == 'Pedro':
	print('Que nome bonito!')
else:
	print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
'''

# Condição Aninhada
if nome == 'Pedro':
	print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo':
	print('Seu nome é bem comum no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
	print('Belo nome feminino!')

#Else é opcional
#else:
#	print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
