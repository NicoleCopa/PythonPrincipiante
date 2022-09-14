"""Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar."""

#declaramos las variables
a = 0
b = 1
c = 0

#mostramos por pantalla un mensaje de lo que vamos a mostrar
print("Los numeros de la sucesión de Fibonacci son: ")

#usamos for para ir de 1 a 10 con paso 1
for i in range (1,10,1):
    #mostramos la variable c
    print(c)
    #igualamos a con b
    a = b
    #igualamos b con c
    b = c
    #sumamos a + b y lo igualamos con c
    c = a+b
