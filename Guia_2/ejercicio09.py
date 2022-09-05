"""Promedio de números aleatorios: Realice un programa que permita calcular el promedio de 1000 
números aleatorios generados en el rango de [0,100000]."""

import random
#declaramos variables
num = int()
promedio = float()
total = int()

print("-- P R O M E D I O  D E  N U M E R O S  A L E A T O R I O S --")

#usamos for para tener los 1000 numeros
for i in range (1000):
    num = random.randrange(0,100000)
    #usamos un acumulador para saber la suma total
    total = total + num
    i = i+1
#sacamos el promedio
promedio = total / 1000
#mostramos en pantalla el promedio
print("El promedio de los 1000 números aleatorios es:", round(promedio,2))