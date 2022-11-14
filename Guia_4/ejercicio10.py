"""Diseñar el algoritmo correspondiente a un programa, que:
a) Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
b) Carga la tabla con valores numéricos enteros.
c) Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla."""

#declaramos las variables
tabla = []
columna = 5
fila = 5

#for para crear las columnas y filas
for i in range (fila):
    tabla.append([0]*columna)

#recorremos f en fila
for f in range (fila):
    #recorremos c en columna
    for c in range (columna):
        #el valor de la tabla en f y c, osea (0;0) , (0;1) , (0;2)... etc y agregamos un valor en cada posición
        tabla[f][c] = int(input("Ingrese un número: "))

#recorremos la fila en tabla
for fila in tabla:
    #recorremos valor en fila
    for valor in fila:
        #por cada valor de fila, se le pone el espacio entre ellos
        print(valor, end=" ") #end para que en vez de poner abajo el valor, lo pone al lado separado con un espacio
    #espacio entre filas
    print()
