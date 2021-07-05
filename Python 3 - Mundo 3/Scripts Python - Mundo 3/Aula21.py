def contador(i, f, p):
	#DOCSTRING
	"""
	-> Faz uma contagem e mostra na tela.
	:param i: início da contagem
	:param f: fim da contagem
	:param p: passo da contagem
	:return: sem retorno
	Função criada por Pedro Dantas.
	"""
	c = i
	while c <= f:
		print(f'{c} ', end='..')
		c += p
	print('FIM')

print(help(contador))
