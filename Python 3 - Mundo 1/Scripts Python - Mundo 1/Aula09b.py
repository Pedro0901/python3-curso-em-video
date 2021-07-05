# ANÁLISE DE STRINGS

frase = 'Curso em Video Python'
print(len(frase)) # Comprimento da string da variavel frase (caracteres)
print(frase.count('o')) #Mostra a quantidade de letras 'o' que temos na variavel frase
print(frase.count('o', 0, 13)) #Contagem com fatiamento (o 13 nao será incluido)
print(frase.find('deo')) # Mostra em que momento (em que posição) começou a palavra 'deo'
print(frase.find('Android'))
print('Curso' in frase) #Retorna True ou False
