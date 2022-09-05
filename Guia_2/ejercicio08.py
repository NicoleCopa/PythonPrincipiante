"""Ventas por sucursal. Ingresar una serie de números por teclado que 
representan la cantidad de ventas realizadas en las diferentes 
sucursales de un país de una determinada empresa. Los requerimientos 
del programa son: Informar la cantidad de ventas ingresadas. Total de 
ventas. Cantidad de ventas cuyo valores estén comprendidos entre 
100 y 300 unidades. Cantidad de ventas con 400,500 y 600 unidades. 
Indicar si hubo una cantidad de ventas inferior a 50 unidades. Usted 
deberá ingresar cantidad es de ventas hasta que se ingrese un valor 
negativo."""

ventas = 1
cantVentas = int()
totalVentas = int()
contador1 = int()
contador2 = int()
contador3 = int()
contador4 = int()

print("-- V E N T A S  P O R  S U C U R S A L --")
print("")

while (ventas > 0):
    ventas = int(input("Ingrese la cantidad de ventas - (Para FINALIZAR ingrese un numero 'NEGATIVO') "))
    cantVentas = cantVentas + 1
    totalVentas = totalVentas + ventas
    if ventas >= 400 and ventas < 500:
        contador1 = contador1 + 1
    elif ventas >= 500 and ventas < 600:
        contador2 = contador2 + 1
    elif ventas >= 600 and ventas < 700:
        contador3 = contador3 + 1
    elif ventas < 50:
        contador4 = contador4 + 1

print("")
print("I N F O R M A C I Ó N")
print("")
print("La cantidad de ventas es:", cantVentas)
print("El total de ventas es:", totalVentas)
print("La cantidad de ventas con 400 es:", contador1)
print("La cantidad de ventas con 500 es:", contador2)
print("La cantidad de ventas con 600 es:", contador3)
print("La cantidad de ventas inferiores a 50 es:", contador4)
