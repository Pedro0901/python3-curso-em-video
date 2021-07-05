#pessoas = dict() Poderia criar o dicionário dessa maneira também
pessoas = {'Nome': 'Pedro', 'Sexo': 'M', 'Idade': 18}
print(pessoas['Nome'])
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.') #Usar aspas duplas dentro dos parenteses

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

#del pessoas['Sexo']
pessoas['Nome'] = 'Gustavo'
pessoas['Peso'] = 98.5

for k, v in pessoas.items():
	print(f'{k} = {v}')
