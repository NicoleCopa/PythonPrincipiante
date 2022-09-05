"""Secuencia de impares. Cargar por teclado dos números, e imprimir 
los números impares que se encuentran comprendidos entre ellos, en 
forma ascendente y descendente."""

num1 = 0
num2 = 0

print("-- S E C U E N C I A  D E  I M P A R E S --")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))

if num1 < num2:
    print("Numeros impares en forma ascendente:")
    for i in range (num1, num2, 1):
        residuo = i % 2
        if residuo != 0:
            print(i)
    print("Numeros impares en forma descendente:")
    for i in range (num2, num1, -1):
        residuo = i % 2
        if residuo != 0:
            print(i)
else:
    print("Numeros impares en forma ascendente:")
    for i in range (num2, num1, 1):
        residuo = i % 2
        if residuo != 0:
            print(i)
    print("Numeros impares en forma descendente:")
    for i in range (num1, num2, -1):
        residuo = i % 2
        if residuo != 0:
            print(i)