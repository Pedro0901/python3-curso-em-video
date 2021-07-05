'''
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30/100

print('\nPara pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('\nA prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
	print('\nEmpréstimo pode ser CONCEDIDO!')
else:
	print('\nEmpréstimo NÃO pode ser CONCEDIDO!')
