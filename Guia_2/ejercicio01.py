"""Ciclistas: La final de una carrera de ciclistas tiene n competidores
(n se ingresa por teclado). Desarrollar un programa que permita cargar,
por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera.
Determinar si el tiempo del ganador es menor al tiempo record, mostrar 
un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas."""

#declaracion de variables
competidores = 0
nombre = ""
tiempo = 0
tiempoR = 0
promedio = 0.0
suma = 0
ganador = ""
minimo = 999
i = 0

#mostramos por pantalla
print("-- C I C L I S T A S --")
print("")

competidores = int(input("Ingrese la cantidad de competidores: "))
tiempoR = int(input("Ingrese el tiempo record: "))

#usamos ciclo while para preguntar por todos los competidores
while i < competidores:
    nombre = str(input("Ingrese el nombre del competidor: "))
    tiempo = int(input("Ingrese el tiempo de carrera del competidor: "))
    suma = suma + tiempo

    #usamos minimo para saber el menor tiempo y el ganador
    if tiempo < minimo:
        minimo = tiempo
        ganador = nombre
    
    i = i+1

#respuestas
print("El ciclista ganador es:", ganador)

if minimo < tiempoR:
    print("El record es del ganador, con un tiempo de:", minimo)
else:
    print("El tiempo record sigue siendo de:", tiempoR)

promedio = suma / competidores #sacamos promedio de tiempo
print("El promedio es de:", promedio)