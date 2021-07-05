'''
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade > 80:
	print('\nVocê foi multado!')
	multa = (velocidade - 80) * 7
	print('\nValor da Multa: R${:.2f}'.format(multa))
else:
	print('\nTenha um bom dia! Dirija com cuidado.')
