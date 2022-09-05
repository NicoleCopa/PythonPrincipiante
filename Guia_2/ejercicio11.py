"""Menores y promedio Realizar un programa que genere 5000 numeros aleatorios en el rango de 
[0,100000] y que permita: Determinar el menor de los numeros generados en forma aleatoria. Calcular el 
valor promedio de los números menores a 10.000."""

import random
#declaramos las variables
num = int()
menor = 99999
promedio = int()
contador = int()
total = int()

print("-- M E N O R E S  Y  P R O M E D I O --")

#usamos for para obtener los 5000 numeros
for i in range (0, 5000):
    num = random.randrange(0, 100000)
    #usamos minimo
    if (num < menor):
        menor = num
    #usaos condicional para todos los numeros menores a 10.000
    if (num < 10000):
        #usamos contador para saber cuantos hay
        contador = contador + 1
        #usamos acumulador para sacar el promedio
        total = total + num
    i = i + 1
#sacamos promedio
promedio = total / contador
#mostramos en pantalla el menor y el promedio pedido
print("El numero menor es:", menor)
print("El promedio de los numeros menores a 10.000 es:", promedio)