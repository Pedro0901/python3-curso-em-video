# RETORNANDO VALORES "return"

def somar(a=0, b=0, c=0):
	s = a + b + c
	#print(f'A soma vale {s}.')
	return s


'''
Podemos jogar o 's' para uma variavel
resp = somar(3, 2, 5)

# Ou para um print
print(somar(3, 2, 5))
somar(2, 2)
somar(6)
'''
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)

print(f'Meus cálculos deram {r1}, {r2}, {r3}.')
