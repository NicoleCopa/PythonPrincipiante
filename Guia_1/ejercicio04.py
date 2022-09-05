"""División con resto. Plantear un algoritmo que 
permita informar, para dos valores a y b el 
resultado de la división a/b y el resto de esa 
división."""

#declaración de variables
num1 = 0.0
num2 = 0.0
division = 0.0
resto = 0.0

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un segundo numero: "))

#division y resto
division = num1 / num2
resto = num1 % num2

print("El resultado de la división es", division, ", y su resto es", resto)
