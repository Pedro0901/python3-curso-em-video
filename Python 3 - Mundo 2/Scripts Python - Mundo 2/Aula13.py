for c in range(0, 6): #Primeiro numero dentro do parentese é onde a contagem começa, o 2º é onde PARA. (Para e nao mostra o numero)
	print(c)

print('-------------DIVISÓRIA-------------')

for c in range(6, 0, -1): #O -1 informa que você quer contar do maior para o menor. (De traz pra frente)
	print(c)
print('\nFIM')

print('-------------DIVISÓRIA-------------')

for c in range(0, 7, 2): #Conta de 0 a 7 pulando de 2 em 2. O 2 informa que você quer pular de 2 em 2.
	print(c)	

print('-------------DIVISÓRIA-------------')

n = int(input('\nDigite um número: '))
for c in range(0, n+1):
	print(c)

print('-------------DIVISÓRIA-------------')

i = int(input('\nInicio: '))
f = int(input('\nFim: '))
p = int(input('\nPasso: '))
for c in range(i, f+1, p):
	print(c)

print('-------------DIVISÓRIA-------------')

s = 0
for c in range(0, 4):
	n = int(input('\nDigite um valor: '))
	s += n #Mesma coisa que s = s + n (S recebe S mais N)
print('\nO somatório de todos os valores foi: {}'.format(s))	
