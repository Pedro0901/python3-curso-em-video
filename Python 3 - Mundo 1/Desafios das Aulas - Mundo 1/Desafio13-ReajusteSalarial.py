'''
Exercício Python 013: Faça um algoritmo que leia o salário de 
um funcionário e mostre seu novo salário, com 15% de aumento.
'''
salario = float(input('Qual é o salário do Funcionário: R$ '))
novo = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento receberá R${novo}.')
