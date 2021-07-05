'''
Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print(f'O produto que custava R${preco}, na promoção com 5% de desconto vai custar R${novo}.')
