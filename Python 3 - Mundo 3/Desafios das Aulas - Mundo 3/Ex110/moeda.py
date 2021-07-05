# Funções ex110

def aumentar(preco = 0, taxa = 0, formato=False):
	res = preco + (preco * taxa/100)
	return res if formato is False else moeda(res)
	
	
def diminuir(preco = 0, taxa = 0, formato=False):
	res = preco - (preco * taxa/100)
	return res if formato is False else moeda(res)

def dobro(preco = 0, formato=False):
	res = preco * 2
	return res if formato is False else moeda(res)
	

def metade(preco = 0, formato=False):
	res = preco / 2
	return res if formato is False else moeda(res)
	

def moeda(preco = 0, moeda = 'R$'):
	return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco = 0, taxaA = 10, taxaR = 5):
	print('-' * 32)
	print('RESUMO DO VALOR'.center(30))
	print('-' * 32)
	print(f'Preço analisado: \t{moeda(preco)}')
	print(f'Dobro do preço: \t{dobro(preco, True)}')
	print(f'Metade do preço: \t{metade(preco, True)}')
	print(f'{taxaA}% de aumento: \t{aumentar(preco, taxaA, True)}')
	print(f'{taxaR}% de redução: \t\t{diminuir(preco, taxaR, True)}')
	print('-' * 32)
