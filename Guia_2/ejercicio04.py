"""Decimal a Hexadecimal: Generar n números aleatorios entre el rango 
de 5000 y 450000, por cada uno de ellos mostrar y generar el numero 
hexadecimal."""

import random

#declaramos variables
cantidad = 0
decimales = 0
i = 0

print("-- D E C I M A L  A  H E X A D E C I M A L --")
#preguntamos la cantidad de numeros aleatorios
cantidad = int(input("Ingrese la cantidad de numeros que quiere generar: "))

#usamos while para generar los n numeros
while i < cantidad:
    #usamos random entre los rangos pedidos
    decimales = random.randrange(5000,450000)
    #mostramos en pantalla los numeros generados
    print(decimales, "decimales =", hex(decimales), "hexadecimales")
    i=i+1