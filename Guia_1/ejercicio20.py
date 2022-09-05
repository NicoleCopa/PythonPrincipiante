"""Tarjeta de Bingo. Realizar un programa que 
genere 15 números aleatorios enteros en el 
rango del 1 al 100, que representaría la 
tarjeta de bingo de una persona. Una vez 
generado los números aleatorios solicitar 
al usuario que ingrese 3 números enteros, 
a parƟr de allí mostrar los siguientes mensajes: 
Si el usuario no marcó ninguno de los números, 
indicarlo diciendo “El jugador tiene mala suerte, 
no marcó ninguna casilla”. Caso contrario mostrar 
“El jugador marcó algún número de la tarjeta”."""

import random

num_r = 0

num1 = int(input("Ingrese un primer numero: "))
num2 = int(input("Ingrese un segundo numero: "))
num3 = int(input("Ingrese un tercer numero: "))

for i in range (1,16):
    num_r = random.randrange(1,100)
    print(num_r)
    i = i+1

if (num1 == num_r) or (num2 == num_r) or (num3 == num_r):
    print("¡El jugador marcó algun numero de la tarjeta!")
else:
    print("El jugador tiene mala suerte, no marcó ninguna casilla")