"""Números pares e impares Se pide desarrollar un programa que permita leer una serie de números. 
La nalización de carga de datos se presenta cuando el usuario ingrese un número negativo. Los 
requerimientos funcionales del programa son: La sumatoria de solo los números que estén comprendidos
entre 50 y 100. Cantidad de valores pares ingresados. Cantidad de valores impares ingresados. Informar si 
en la carga de números se ingreso al menos un número 0. Informar si la serie contiene solo números pares 
e impares alternados."""

#declaramos variables
num = int()
sumatoria = int()
cantidad = int()
pares = int()
impares = int()

#inicializamos un while mientras los numeros sean mayores a 0
while num >= 0:
    #pedimos al usuario que ingrese un numero
    num = int(input("Ingrese un numero - Para finalizar ingrese num NEGATIVO: "))
    #usamos condicional para la suma de numeros entre 50 y 100
    if num >= 50 and num <= 100:
        sumatoria = sumatoria + num
    #usamos condicional para la cantidad de numeros pares
    if num % 2 == 0:
        pares = pares + 1
    #usamos condicional para la cantidad de numeros impares
    else:
        impares = impares + 1
    #usamos condicional para la cantidad de veces que se ingresó 0
    if num == 0:
        cantidad = cantidad + 1
        
#mostramos en pantalla lo pedido
print("La sumatoria de los números entre 50 y 100 es:", sumatoria)
print("La cantidad de números pares ingresados es de:", pares)
print("La cantidad de números impares ingresados es de:", impares)
if cantidad > 0:
    print("En la carga de numeros se ingresaron", cantidad, "'0'")
else:
    print("En la carga de numeros no se ingresó ningún '0'")
