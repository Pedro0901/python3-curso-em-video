from math import hypot


'''
Maneira matemática (sem importações)
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
'''

# Usando biblioteca math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hip))
