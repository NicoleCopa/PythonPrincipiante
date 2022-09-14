"""Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10."""

#declaramos la variable
num = 0

#mostramos por pantalla el titulo del ejercicio
print("-- M U L T I P L I C A C I O N --")

#le preguntamos al usuario el numero
num = int(input("Ingrese un numero: "))

#usamos for apra ir de a 1 a 11
for i in range (1,11):
    #mostramos num, i y num*i
    print(num, "x", i, "=", num*i)
    #le multiplicamos num a i y lo declaramos en i
    i = i*num
