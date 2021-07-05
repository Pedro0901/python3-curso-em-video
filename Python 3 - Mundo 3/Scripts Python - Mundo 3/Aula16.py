# Toda tupla é entre parenteses
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

# Printando tudo de maneira organizada (Ordem alfabética)
print(sorted(lanche)) #Isso nao muda o estado natural da variavel, apenas muda na hora de printar

# Maneira clássica
for comida in lanche:
	print(f'Eu vou comer {comida}.')

# Usando o range
for cont in range(0, len(lanche)):
	print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# TUPLAS SÃO IMUTÁVEIS
# lanche[1] = 'Refrigerante' ISSO NAO EXISTE, IRÁ DAR ERRO.

# Usando a variavel composta
for pos, comida in enumerate(lanche):
	print(f'Eu vou comer {comida} na posição {pos}')
print('Comi muito!')
