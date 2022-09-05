"""Complejo de cines. Desarrollar un programa que permita procesar 
funciones de un complejo de cines. Por cada función se conoce:
cantidad de espectadores y descuento(S/N). La carga termina cuando la 
cantidad de espectadores sea igual a 0(cero). El programa deberá:
Calcular la recaudación total del complejo, considerando que el valor 
de la entrada es de $50 en los días con descuento y $75 en los días sin 
descuento. Determinar cuántas funciones con descuentos efectuaron y 
qué porcentaje representan sobre el total de funciones"""

#declaramos variables
espectadores = int()
descuento = str()
precio = int()
monto = int()
funciones_conD = int()
funciones = int()
porcentaje = float()

print("-- C O M P L E J O  D E  C I N E S --")
print("")

#pedimos que ingresen los espectadores
espectadores = int(input("Ingrese la cantidad de espectadores (para finalizar, ingrese '0'): "))

while espectadores != 0:
    
    #pedimos que ingrese si tiene o no descuento
    descuento = str(input("Descuento (S/N): "))
    
    #definimos precios con if
    if (descuento == "S"):
        precio = 50
        #usamos contador para saber el total de funciones con descuento
        funciones_conD = funciones_conD + 1
    else:
        precio = 75

    #usamos acumuladores para el monto por funcion
    monto = monto + (espectadores * precio)

    #contador para funciones totales
    funciones = funciones + 1

    #pedimos nuevamente que ingresen los espectadores
    espectadores = int(input("Ingrese la cantidad de espectadores (para finalizar, ingrese '0'): "))

#resolución
print("")
print("La recudación total es de: $", monto)

if funciones != 0:
    porcentaje = funciones_conD * 100 / funciones
else:
    porcentaje = 0

print("El porcentaje total de funciones con descuentoe es de:", round(porcentaje, 2), "%")
