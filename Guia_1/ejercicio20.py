"""Tarjeta de Bingo. Realizar un programa que genere 15 números aleatorios enteros en el 
rango del 1 al 100, que representaría la tarjeta de bingo de una persona. Una vez 
generado los números aleatorios solicitar al usuario que ingrese 3 números enteros, 
a parƟr de allí mostrar los siguientes mensajes: Si el usuario no marcó ninguno de los números, 
indicarlo diciendo “El jugador tiene mala suerte, no marcó ninguna casilla”. Caso contrario mostrar 
“El jugador marcó algún número de la tarjeta”."""

import random
#declaramos variables
num_r = 0
num1 = 0
num2 = 0
num3 = 0

#pedimos al usuario que ingrese los numeros
num1 = int(input("Ingrese un primer numero: "))
num2 = int(input("Ingrese un segundo numero: "))
num3 = int(input("Ingrese un tercer numero: "))

#usamos for para ir de 1 a 16
for i in range (1,16):
    #delcaramos una variable con random de rango 1-100
    num_r = random.randrange(1,100)
    #mostramos en pantalla el numero random
    print(num_r)
    #le sumamos uno a i
    i = i+1

#usamos condicional para saber si algun numero ingresado se repite con el random
if (num1 == num_r) or (num2 == num_r) or (num3 == num_r):
    #mostramos en pantalla que acertó
    print("¡El jugador marcó algun numero de la tarjeta!")
else:
    #mostramos en pantalla que no acertó
    print("El jugador tiene mala suerte, no marcó ninguna casilla")
