"""Suma - División - Potencia. Se necesita desarrollar un programa 
que permita calcular la suma de tres números. Si el resultado es 
mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en 
caso contrario elevar el resultado al cubo."""

#declaramos variables
num1 = 0.0
num2 = 0.0
num3 = 0.0
suma = 0.0
division = 0
potencia = 0.0

#ingreso de datos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

#cuentas
suma = num1 + num2 + num3
division = int(suma/2)
potencia = suma**3

#condicional
if suma > 10:
    print("El resultado de", num1, "+", num2, "+", num3, "=", suma, "/ 2 =", division)
else:
    print("El resultado de", num1, "+", num2, "+", num3, "=", suma, "^ 3 =", potencia)
