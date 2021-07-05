a = [2, 3, 4, 7]

# A partir do momento em que igualamos uma lista na outra, o python cria uma ligação entre elas
# b = a

# Ou seja, essa alteração valerá para as duas listas (a e b)
# b[2] = 8

# Para fazermos uma cópia de lista, usamos:
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
