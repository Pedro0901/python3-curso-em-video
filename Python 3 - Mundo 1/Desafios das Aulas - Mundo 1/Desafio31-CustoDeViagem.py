'''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
Distancia = int(input('Qual a distância de sua viagem? (em KM) '))

if Distancia <= 200:
	print('\nO preço da passagem é: R${:.2f}'.format(Distancia * 0.50))
else:
	print('\nO preço da passagem é: R${:.2f}'.format(Distancia * 0.45))
