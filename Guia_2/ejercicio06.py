"""Mostrar por pantalla el promedio de los números ingresados por 
teclado. Se deja de pedir que el usuario agregue números una vez 
ingrese 0 (cero)."""

#declaramos variables
num = 1
total = int()
cantidad = int()
promedio = float()
#mostramos por pantalla
print("-- P R O M E D I O  D E  N U M E R O S --")
#usamos while para finalizar el programa en 0
while num != 0:
    #pedimos que ingrese un numero o que finalice programa con 0
    num = int(input("Ingrese un numero - (si desea salir, ingrese '0'): "))
    #usamos acumulador para saber la suma total
    total = total + num
    #usamos acumulador para saber cuantas veces se ingresa numeros
    cantidad = cantidad + 1
#sacamos el promedio de todos los numeros
promedio = total / cantidad
#mostramos respuesta por pantalla
print("El promedio de los numeros ingresados es:", round(promedio, 2))