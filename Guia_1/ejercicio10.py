"""Ingresar la cantidad de números de la 
sucesión de Fibonacci a mostrar."""

a = 0
b = 1
c = 0

print("Los numeros de la sucesión de Fibonacci son: ")

for i in range (1,10,1):
    print(c)
    a = b
    b = c
    c = a+b