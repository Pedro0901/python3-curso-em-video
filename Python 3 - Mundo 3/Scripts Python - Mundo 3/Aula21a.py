# PARAMETROS OPCIONAIS

def somar(a, b, c=0):
	s = a + b + c
	print(f'A soma vale {s}.')


#Nesse caso, a recebe 3, b recebe 2, c recebe 5
somar(3, 2, 5)

# Nesse outro caso, a recebe 8, b recebe 4, e como o C não é informado, ele continua valendo 0.
somar(8, 4)

#OUTRO EXEMPLO DE PARAMETROS OPCIONAIS

def somar2(a=0, b=0, c=0):
	s = a + b + c
	print(f'A soma vale {s}.')
	

somar2(3, 2, 5)
somar2(8, 4)
somar2(2)
#Com o uso dos parametros opcionais, podemos chamar a função sem parametro nenhum.
somar2()
