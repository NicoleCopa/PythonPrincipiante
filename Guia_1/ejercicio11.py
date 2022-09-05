"""Multiplicación. Ingresar un número cualquiera
por teclado y que muestre su respectiva tabla 
del 1 al 10."""

num = 0

num = int(input("Ingrese un numero: "))

for i in range (1,11):
    print(num, "x", i, "=", num*i)
    i = i*num