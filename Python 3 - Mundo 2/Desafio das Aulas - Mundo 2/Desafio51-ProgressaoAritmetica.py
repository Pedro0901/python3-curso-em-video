'''
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
'''
print('==============================')
print('    10 TERMOS DE UMA P.A      ')
print('==============================')

primeiro = int(input('\nPrimeiro termo: '))
razao = int(input('\nRazão: '))
decimo = primeiro + (10 - 1) * razao

print('\n')
for c in range(primeiro, decimo, razao):
	print('{}'.format(c), end=' → ')
print('ACABOU!!!')
