"""Escribir un programa que pregunte un nombre de usuario, y que 
después muestre por pantalla si su cantidad de letras es par o impar."""

nombre = ""
nombre = str(input("Ingrese su nombre: "))
contador = int(len(nombre)) % 2

if (contador == 0):
    print("El nombre -", nombre, "- tiene una cantidad de lentras par (", int(len(nombre)), ")")
else:
    print("El nombre -", nombre, "- tiene una cantidad de lentras impar (", int(len(nombre)), ")")
