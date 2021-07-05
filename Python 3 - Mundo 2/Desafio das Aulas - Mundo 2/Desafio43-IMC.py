'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
	print('\nSeu IMC é de: {:.1f}'.format(imc))
	print('\nVocê está ABAIXO DO PESO normal!')
elif imc >= 18.5 and imc <= 25:
	print('\nSeu IMC é de: {:.1f}'.format(imc))
	print('\nVocê está no Peso Ideal!')
elif imc > 25.0 and imc <= 30.0:
	print('\nSeu IMC é de: {:.1f}'.format(imc))
	print('\nVocê está com Sobrepeso!')
elif imc > 30.0 and imc <= 40.0:
	print('\nSeu IMC é de: {:.1f}'.format(imc))
	print('\nVocê está com OBESIDADE!')
elif imc > 40.0:
	print('\nSeu IMC é de: {:.1f}'.format(imc))
	print('\nVocê está com OBESIDADE MÓRBIDA, cuidado!')
