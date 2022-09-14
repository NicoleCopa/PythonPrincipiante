"""Secuencia de impares. Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en 
forma ascendente y descendente."""

#declaramos variables
num1 = 0
num2 = 0

#mostramos por pantalla el titulo del ejercicio
print("-- S E C U E N C I A  D E  I M P A R E S --")

#pedimos al usuario que ingrese los numeros
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))

#usamos condicional para saber cual es mayor
if num1 < num2:
    #mostramos mensaje por pantalla 
    print("Numeros impares en forma ascendente:")
    #usamos for para ir de num1 a num2 en rango 1
    for i in range (num1, num2, 1):
        #sacamos el resto de i por 2 y lo almacenamos en residuo
        residuo = i % 2
        #si el residuo es diferente a 0 (impar)
        if residuo != 0:
            #mostramos por pantalla el num i
            print(i)

    print("Numeros impares en forma descendente:")
    #usamos for para ir de num1 a num2 en rango -1
    for i in range (num2, num1, -1):
        #sacamos el resto de i por 2 y lo almacenamos en residuo
        residuo = i % 2
        #si el residuo es diferente a 0 (impar)
        if residuo != 0:
            #mostramos por pantalla el num i
            print(i)
else:
    #hacemos el mismo procedimiento pero siendo num1 mayor a num2
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
