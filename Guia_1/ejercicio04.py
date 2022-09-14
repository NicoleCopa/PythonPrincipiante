"""División con resto. Plantear un algoritmo que permita informar, para dos valores a y b el 
resultado de la división a/b y el resto de esa división."""

#declaración de variables
num1 = 0.0
num2 = 0.0
division = 0.0
resto = 0.0

#mostramos por pantalla el titulo del ejercicio
print("-- D I V I S I O N  C O N  R E S T O --")

#preguntamos al usuario los dos numeros
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un segundo numero: "))

#hacemos la division y resto
division = num1 / num2
resto = num1 % num2

#mostramos por pantalla lo pedido
print("El resultado de la división es", division, ", y su resto es", resto)
