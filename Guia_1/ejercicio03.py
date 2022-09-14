"""Escriba un programa que transforme todas las letras de una palabra
 en mayúsculas, minúsculas y la primera con minúsculas(capitalización)."""

#declaramos variable
palabra = str()

#preguntamos al usuario una palabra
palabra = str(input("Ingrese una palabra: "))

#mostramos por pantalla la palabra como se pide usando capitalizacion, upper y lower 
print(palabra.upper(), palabra.lower(), palabra.capitalize())
