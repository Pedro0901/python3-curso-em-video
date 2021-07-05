# FATIAMENTO DE STRINGS

frase = 'Curso em Video Python'
print(frase[9])
#print(frase[inicio:final])
print(frase[9:13]) #Numero inicial é de onde começa o fatiamento, numero dps dos : é onde o fatiamento para. (Numero final nao é incluido no print)
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2]) #Começa no 9, termina no 21, porém pulando de 2 em 2.
print(frase[:5]) #Quando o usuario omite o inicio, ele começa do caracter 0.
print(frase[15:]) #indiquei o inicio mas nao o final. Ele fatia do 15 até o final da string
print(frase[9::3]) #Começa no 9 e vai até o final, porém pulando de 3 em 3, e mostrando a letra que for a 3º casa pulada (por causa dos ::)

