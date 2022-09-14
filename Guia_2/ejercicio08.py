"""Ventas por sucursal. Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las diferentes 
sucursales de un país de una determinada empresa. Los requerimientos del programa son: Informar la cantidad de ventas ingresadas. Total de 
ventas. Cantidad de ventas cuyo valores estén comprendidos entre 100 y 300 unidades. Cantidad de ventas con 400,500 y 600 unidades. 
Indicar si hubo una cantidad de ventas inferior a 50 unidades. Usted deberá ingresar cantidad es de ventas hasta que se ingrese un valor negativo."""

#declaramos variables
ventas = 1
cantVentas = int()
totalVentas = int()
contador1 = int()
contador2 = int()
contador3 = int()
contador4 = int()

#mostramos por pantalla el titulo del ejercicio
print("-- V E N T A S  P O R  S U C U R S A L --")
print("")

#usamos while mientras ventas sea mayor a 0
while (ventas > 0):
    #pedimos al usuario que ingrese la cantidad de ventas
    ventas = int(input("Ingrese la cantidad de ventas - (Para FINALIZAR ingrese un numero 'NEGATIVO') "))
    #usamos contador para la cantidad de ventas
    cantVentas = cantVentas + 1
    #usamos un acumulador para el total de ventas
    totalVentas = totalVentas + ventas
    #usamos condicional para saber si las ventas estan entre 400 y 500
    if ventas >= 400 and ventas < 500:
        #usamos contador
        contador1 = contador1 + 1
    #usamos condicional para saber si las ventas estan entre 500 y 600
    elif ventas >= 500 and ventas < 600:
        #usamos contador
        contador2 = contador2 + 1
    #usamos condicional para saber si las ventas estan entre 600 y 700
    elif ventas >= 600 and ventas < 700:
        #usamos contador
        contador3 = contador3 + 1
    #usamos condicional para saber si las ventas son menores a 50
    elif ventas < 50:
        #usamos contador
        contador4 = contador4 + 1

#mostramos en pantalla la infromación pedida
print("")
print("I N F O R M A C I Ó N")
print("")
print("La cantidad de ventas es:", cantVentas)
print("El total de ventas es:", totalVentas)
print("La cantidad de ventas con 400 es:", contador1)
print("La cantidad de ventas con 500 es:", contador2)
print("La cantidad de ventas con 600 es:", contador3)
print("La cantidad de ventas inferiores a 50 es:", contador4)
