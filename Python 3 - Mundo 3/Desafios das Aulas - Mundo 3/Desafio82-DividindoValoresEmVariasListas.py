'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
num = []
pares = []
impares = []

while True:
	num.append(int(input('Digite um valor: ')))
	escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()
	if escolha in 'Nn':
		break

for i, v in enumerate(num):
	if v % 2 == 0:
		pares.append(v)
	else:
		impares.append(v)

print('=-' * 30)
print(f'A lista completa de números é: {num}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é: {impares}')
print('=-' * 30)
