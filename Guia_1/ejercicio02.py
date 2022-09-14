"""Escribir un programa que pregunte un nombre de usuario, y que 
después muestre por pantalla si su cantidad de letras es par o impar."""

#declaramos variables
nombre = str()
nombre = str(input("Ingrese su nombre: "))

#mostramos en pantalla el titulo del ejercicio
print("-- N O M B R E S --")

#usamos len para saber cuantas letras tiene el nombre y lo guardamos en contador
contador = int(len(nombre)) % 2

#usamos una condicional dependiendo si el nombre es par o impar
if (contador == 0):
    #mostramos mensaje si el nombre es par
    print("El nombre -", nombre, "- tiene una cantidad de lentras par (", int(len(nombre)), ")")
else:
    #mostramos mensaje si el nombre es impar
    print("El nombre -", nombre, "- tiene una cantidad de lentras impar (", int(len(nombre)), ")")
