"""Área de un triángulo. Desarrolle un programa para calcular el área de un triángulo, cargando
por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base."""

#declaramos las variables
area = 0.0
base = 0.0
altura = 0.0

#mostramos por pantalla el titulo del ejercicio
print("-- A R E A  D E  U N  T R I A N G U L O --")

#preguntamos al usuario el valor de la base
base = float(input("Ingrese la base del triangulo: "))

#calculamos la altura y el area del triangulo
altura = base**2
area = (base * altura) / 2

#mostramos por pantalla el resultado
print("El área del triangulo es:", area)
