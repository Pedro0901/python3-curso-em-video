num = [2, 5, 9, 1]
# LISTAS SÃO MUTÁVEIS
num[2] = 3 

# Para adicionar algum numero no final da lista
num.append(7)
print(num)

# Coloca tudo em ordem
num.sort()
print(num)

# Coloca a lista do maior para o menor
num.sort(reverse=True)
print(num)

# Para inserir algum valor em alguma posição
num.insert(2, 0) # insere na posição 2 o número 0
print(num)

num.insert(2, 2)
print(num)

# Para remover um numero de uma lista
if 4 in num:
	num.remove(2) # Só removerá o primeiro numero 2 da lista
	print(num)
else:
	print('Não achei o número 4')

#Removendo elementos da lista
num.pop(2) #Sem passar parametro nenhum = Elimina o ultimo numero da lista
print(num)

# Para mostrar o tamanho da lista
print(f'Essa lista tem {len(num)} elementos.')
