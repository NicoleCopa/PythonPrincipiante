"""Diseñar el algoritmo correspondiente a un programa, que:
a) Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
b) Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
c) Muestra el contenido de la tabla en pantalla."""
#Inicializo variables
filas = 5
columnas = 5
tabla = []

#for para crear las columnas y filas
for i in range (filas):
    tabla.append([0]*columnas)

#recorremos f en fila
for f in range(filas):
    #recorremos c en columna
    for c in range(columnas):
        #si el valor de la posición f con c es igual, se pone un 1 ej: (0;0),(1;1),(2;2)... etc
        if (f == c):
            tabla[f][c] = 1
        else:
            tabla[f][c] = 0

print("-- D I A G O N A L --")

#recorremos la fila en tabla
for fila in tabla:
    #recorremos valor en fila
    for valor in fila:
        #por cada valor de fila, se le pone el espacio entre ellos
        print(valor, end=" ") #end para que en vez de poner abajo el valor, lo pone al lado separado con un espacio
    #espacio entre filas
    print()

"""
1  0  0  0  0
0  1  0  0  0
0  0  1  0  0
0  0  0  1  0
0  0  0  0  1
"""
