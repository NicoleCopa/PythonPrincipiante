"""Ahorros. Escribir un programa en el cual 
muestre a fin de año el total de ahorro obtenido, 
si se pide en cada mes el 10% del sueldo ganado."""

#declaración de variables
total = 0.0
ahorro = 0.0
contador = 1
sueldo = 0.0

#utilizamos un while
while contador <= 12:
    #contador del mes que preguntamos
    print("Mes", contador) 
    #pregunta sueldo del mes actual
    sueldo = float(input("Ingrese cuanto ganó este mes: "))
    #acumulador de sueldo total
    total = total + sueldo
    #contador para seguir los meses y el while
    contador = contador + 1 
#ahorro del 10% del sueldo total
ahorro = total/10
#mostramos en pantalla cuanto fue el ahorro en todo el año
print("Su ahorro total del año fue de: $", ahorro)