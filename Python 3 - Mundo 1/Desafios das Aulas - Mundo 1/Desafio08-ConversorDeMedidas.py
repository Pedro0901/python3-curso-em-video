'''
Exercício Python 008: Escreva um programa que leia um valor em 
metros e o exiba convertido em centímetros e milímetros.
'''
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida {medida}m corresponde a {cm}cm e {mm}mm.')
