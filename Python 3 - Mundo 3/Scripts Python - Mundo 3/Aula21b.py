# ESCOPO DE VARIAVEIS

def teste():
	global x
	x = 8 #Essa variavel só existe na função teste e nao no programa principal. (ESCOPO LOCAL)
	print(f'Na função teste, "n" vale {n}.')
	print(f'Na função teste, "x" vale {x}.')
	

#Programa Principal
n = 2 # Já a variavel n, funciona no programa principal e na função teste. (ESCOPO GLOBAL)
print(f'No programa principal, "n" vale {n}.')
teste()

#Para a variavel x funcionar no escopo global, devemos usar a palavra reservada "global", na função, antes da variavel
print(f'No programa principal, "x" vale {x}.')
