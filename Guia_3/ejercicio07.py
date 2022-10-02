"""Secuencia numérica II. Ingresar un secuencia de números, de a uno por vez, la carga 
finaliza cuando el usuario ingresa el cero. Determinar:
a) El promedio de los números que son múltiplos de 6
b) Cantidad de números que son divisor exacto del anterior
c) Indicar la cantidad de veces que se generó una secuencia ascendente de 3 o más números impares"""

num = int(1)
anterior = int(1)
impar = int()
cantMultiplos = int()
totalMultiplos = int()
divisor = int()
promedio = float()

while (num != 0):

    num = int(input("Ingrese un número - para finalizar ingrese '0': "))
    
    if (num % 6 == 0):
        cantMultiplos = cantMultiplos + 1
        totalMultiplos = totalMultiplos + num
    
    if (anterior % num == 0):
        divisor = divisor + 1

    """if (num % 2 != 0):
        if (impar == 0 or num > anterior):
            impar = impar + 1
        else:
            impar = 1
    else:
        impar = 0"""
    
    anterior = num

if cantMultiplos > 0:
    promedio = totalMultiplos / cantMultiplos

print("El promedio de los múltiplos de 6 es:", round(promedio,2))
print("La cantidad de números que son divisor exacto del anterior es:", divisor)
print("La cantidad de veces que se generó una secuencia ascendente de 3 o más numeros impares es:", impar)
