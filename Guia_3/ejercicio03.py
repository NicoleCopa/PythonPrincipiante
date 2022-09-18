"""Secuencia numérica. Ingresar una secuencia de números, de a uno por vez, la carga 
finaliza cuando el usuario ingresa el cero. Determinar
a) Porcentaje que representan los números divisibles por 3 sobre el total de números 
ingresados en la secuencia
b) Determinar la cantidad de números que son el cuadrado del número anterior
c) Determinar la posición del mayor elemento impar de la secuencia"""

#declaramos variables
num = int()
total = int()
divisibles = int()
anterior = int()
cuadrados = int()
mayor = int()
orden = int()
porcentaje = float()

#mostramos por pantalla el titulo del ejercicio
print("-- S E C U E N C I A  N U M E R I C A --")

#pedimos al usuario que ingrese un numero
num = int(input("Ingrese un numero: "))

#usamos while para terminar el programa cuando se ingrese 0
while num != 0:
    #usamos contador para saber el total de numeros ingresados
    total = total + 1
    #usamos condicional para saber que numeros son divisibles por 3
    if num % 3 == 0:
        #usamos contador para saber la cantidad de estos
        divisibles = divisibles + 1
    #usamos condicional para saber que numeros al cuadrados con iguales al anterior
    if anterior * anterior == num:
        #usamos contador para saber la cantidad de estos
        cuadrados = cuadrados + 1
    #usamos condicional para saber que numeros son impares
    if num % 2 != 0:
        #usamos maximo para saber que num impar es mas alto
        if mayor < num:
            #lo almacenamos en mayor
            mayor = num
            #guardamos en orden el num de pocision del num
            orden = total
    #declaramos anterior como el numero asi pedimos uno nuevo
    anterior = num
    #volvemos a pedir un nuemro numero al usuario
    num = int(input("Ingrese un numero: "))

#sacamos el porcentaje de los numeros divisibles por 3
porcentaje = divisibles * 100 / total
#mostramos por pantalla lo pedido
print("El pocentaje de todos los numero divisibles por 2 es: "+ str(round(porcentaje,2)) + "%")
print("La cantidad de numeros que son el cuadrado del anterior son:", cuadrados)
print("La posicion del mayor elemento impar de la secuencia es:", orden)
