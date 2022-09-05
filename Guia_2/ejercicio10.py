"""Búsqueda de mayor Realizar un programa que permita buscar el mayor de 10.000 números aleatorios
generados en el rango de[0,100.000]."""

import random
#declaramos variables
num = int()
mayor = 0

print("-- B U S Q U E D A  D E  M A Y O R --")

#usamos for para obtener los 10.000 numeros
for i in range (10000):
    num = random.randrange(0, 1000000)
    #usamos maximos
    if num > mayor:
        mayor = num
    i = i+1
#mostramos en pantalla el numero mayor
print("El número mayor entre los 10.000 números aleatorios es:", mayor)