''' TRATAMENTO DE ERROS E EXCEÇÕES '''

# Tente fazer esses comandos
''' Obs.: Um mesmo "try" pode ter vários except's. '''
try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a / b

# Se der problema...
#except:
	#print('Infelizmente, tivemos um problema :(')

# Outra forma de except
except Exception as erro:
	print(f'Problema encontrado foi {erro.__class__}')
	
# Se o try der certo... (opcional)
else:
	print(f'O resultado é {r:.2f}')
	
# "Finalmente", ele vai acontecer independente se deu certo ou se deu erro (opcional)
finally:
	print('Volte sempre! Muito Obrigado!!')
