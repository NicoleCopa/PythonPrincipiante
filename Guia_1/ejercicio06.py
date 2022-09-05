"""Área de un triángulo. Desarrolle un programa
para calcular el área de un triángulo, cargando
por teclado el valor de la base, pero sabiendo
que su altura es igual al cuadrado de la base."""

area = 0.0
base = 0.0
altura = 0.0

base = float(input("Ingrese la base del triangulo: "))
altura = base**2
area = (base * altura) / 2
print("El área del triangulo es:", area)