"""Escribir un programa que pida dos números 
y muestre como resultado su división, cociente 
y resto."""

num1 = 0.0
num2 = 0.0
cociente = 0.0
resto = 0.0

num1 = float(input("Ingrese un nuemro: "))
num2 = float(input("Ingrese otro nuemro: "))

cociente = num1/num2
resto = num1%num2

print("La división", num1, "/", num2, "=", cociente, "y su resto es", resto)
