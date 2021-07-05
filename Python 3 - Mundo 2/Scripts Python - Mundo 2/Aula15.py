cont = 1


while cont <= 10:
	print(cont, ' -> ', end='')
	cont += 1
print('Acabou')


# Exemplo de loop infinito (Para quebrar o loop infinito é só usar o break)
n = s = 0
while True:
	n = int(input('Digite um número: '))
	# 999 é um flag pra saída do loop infinito
	if n == 999:
		break
	s += n
#print('\nA soma vale {}'.format(s))
print(f'\nA soma vale {s}')
