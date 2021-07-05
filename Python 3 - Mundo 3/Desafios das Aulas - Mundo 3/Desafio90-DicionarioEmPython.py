'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
'''
aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Media'] = float(input('Média do aluno: '))

print('=-' * 30)
print(f'- Nome é igual a {aluno["Nome"]}')
print(f'- Média é igual a {aluno["Media"]}')

if aluno['Media'] >= 6:
	aluno['Situação'] = 'Aprovado!'
else:
	aluno['Situação'] = 'Recuperação!'
print(f'- Situação é igual a {aluno["Situação"]}')
