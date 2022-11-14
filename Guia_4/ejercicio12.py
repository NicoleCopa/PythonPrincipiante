"""Diseñar el algoritmo correspondiente a un programa, que:
Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’. Carga la tabla con dos únicos valores 0 y 1, 
donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, 
mientras que el resto de los elementos contendrán el valor 0.
111111111111111
100000000000001
100000000000001
100000000000001
111111111111111
Visualiza el contenido de la matriz en pantalla."""

#Inicializo variables
filas = 5
columnas = 15
tabla = []

#for para crear las columnas y filas
for i in range (filas):
    tabla.append([0]*columnas)

#recorremos f en fila
for f in range(filas):
    #recorremos c en columna
    for c in range(columnas):
        #si el valor de la posición f con c es igual, se pone un 1 ej: (0;0),(1;1),(2;2)... etc
        if (f == 0) or (f == 4) or (c == 0) or (c == 14):
            tabla[f][c] = 1
        else:
            tabla[f][c] = 0

print("-- M A R C O --")

#recorremos la fila en tabla
for fila in tabla:
    #recorremos valor en fila
    for valor in fila:
        #por cada valor de fila, se le pone el espacio entre ellos
        print(valor, end=" ") #end para que en vez de poner abajo el valor, lo pone al lado separado con un espacio
    #espacio entre filas
    print()
