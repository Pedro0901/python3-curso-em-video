num = soma = quant = 0

while True:
	num = int(input('Digite um número (999 para PARAR): '))
	quant += 1
	if num == 999:
		quant -= 1
		break
	soma += num
print(f'\nO total de números digitados foi {quant} e a soma deles é {soma}')
