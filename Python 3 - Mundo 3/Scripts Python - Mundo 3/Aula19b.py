estado = dict()
brasil = list()

for c in range(0, 3):
	estado['UF'] = str(input('Unidade Federativa: '))
	estado['Sigla'] = str(input('Sigla do Estado: '))
	brasil.append(estado.copy()) # em dict usamos o metodo copy. Em list usamos [:] para fazer uma copia
	
for e in brasil:
	for v in e.values():
		#print(f'O campo {k} tem valor {v}')
		print(v)
