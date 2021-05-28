#3. Generar una lista de números aleatoriamente y resuelva lo siguiente:
#a. indicar el rango de valores de la misma, diferencia entre menor y mayor
#b. indicar el promedio
#c. ordenar la lista de manera creciente y mostrar dichos valores
#d. ordenar la lista de manera decreciente y mostrar dichos valores
#e. hacer un barrido que solo muestre los número impares no múltiplos de 3

from random import randint


numeros = []

for i in range (0,100):
    numero1 = randint(1,100)
    numeros.append(numero1)

numeros.sort()

print ("El menor de la lista es",numeros[0])
print ("El mayor de la lista es",numeros[99])

print(numeros)
for lista in range (0,99):
    if (lista % 9==0, lista % 5==0, lista % 7==0,lista % 3==0):
        print(lista)
           
