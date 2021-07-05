'''
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
Salario = float(input('Informe seu salário: '))

if Salario > 1250:
	print('\nQuem ganhava {:.2f} vai passar a ganhar {:.2f}'.format(Salario, Salario + (Salario * 10/100)))
else:
	print('\nQuem ganhava {:.2f} vai passar a ganhar {:.2f}'.format(Salario, Salario + (Salario * 15/100)))
