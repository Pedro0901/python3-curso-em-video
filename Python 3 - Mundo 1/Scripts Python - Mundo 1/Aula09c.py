# TRANSFORMAÇÃO DE STRINGS

frase = 'Curso em Video Python'
print(frase.replace('Python', 'Android')) #Substitui uma palavra por outra
print(frase.upper()) # Deixa a frase toda em CAPSLOCK, MAIUSCULA.
print(frase.lower()) # Deixa a frase toda em minuscula
print(frase.capitalize()) #Deixa todos os caracteres em minusculos, com exceção do primeiro, que ficará maiusculo
print(frase.title()) #Deixa todas as primeiras letras de cada palavra em maiusculo
frase2 = '    Aprenda Python   '
print(frase2)
print(frase2.strip()) # retira os espaços desnecessários
print(frase2.rstrip()) # retira os espaços desnecessarios do right, lado direito
print(frase2.lstrip()) # retira os espaços desnecessarios do left, lado esquerdo
