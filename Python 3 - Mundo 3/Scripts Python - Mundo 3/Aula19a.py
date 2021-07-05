#Dicionario dentro de uma lista

brasil = list()
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print()
print(brasil[0]['UF'])
