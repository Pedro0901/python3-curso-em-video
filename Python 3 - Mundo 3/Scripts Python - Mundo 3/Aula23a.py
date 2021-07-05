# TRATAMENTO DE ERROS E EXCEÇÕES - ANOTAÇÕES PARTE 2

# Usando um try com vários except's.
try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a / b

# Mostrando erros especificos
except (ValueError, TypeError): #Entre parenteses para colocarmos vários erros
	print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
	print('Não é possível dividir um número por 0.')
except KeyboardInterrupt:
	print('O usuário prefiriu não informar os dados.')
except Exception as erro:
	print(f'O erro encontrado foi {erro.__cause__}.')
else:
	print(f'O resultado foi {r:.2f}')
finally:
	print('Volte sempre! Muito obrigado!')
