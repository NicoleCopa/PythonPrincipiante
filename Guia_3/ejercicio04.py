"""Proceso de discriminantes Un matemático desea un simple programa que le permita cargar una serie de 
números que representan los discriminantes de diferentes ecuaciones de segundo grado, el proceso de la 
secuencia analiza cuando el matemático no desea seguir cargando discriminantes. Usted debe:
a) Determinar la cantidad de discriminantes que darán 2 raíces
b) Determinar la cantidad de discriminantes que darán una única raíz
c) Determinar la cantidad de discriminantes que daran raíces en el campo de los números imaginarios
d) Indicar el porcentaje que representa el punto c sobre el total de discriminantes procesados por el matemático"""

# b**2 - 4 * a * c
# <0 ----solucion imaginaria
# >0 ----soluciones reales y diferentes
# =0 ----soluciones reales e iguales

#declaramos variables
valorA = float()
valorB = float()
valorC = float()
opcion = int()
discriminante = float()
raicesDiferentes = int()
raicesImaginarias = int()
raicesIguales = int()
total = int()
porcentaje = float()

#mostramos titulo del ejercicio por pantalla
print("-- P R O C E S O  D E  D I S C R I M I N A N T E S --")

#usamos while para que se repita hasta que el usuario decida lo contrario
while (opcion != 2):

    #pedimos que ingrese los valores de a, b y c
    valorA = float(input("Ingrese el valor de 'a': "))
    valorB = float(input("Ingrese el valor de 'b': "))
    valorC = float(input("Ingrese el valor de 'C': "))

    #sacamos el determinante de "a, b y c"
    discriminante = ((valorB**2) - (4*valorA*valorC))

    #usamos condicional para saber que dará el discriminante y agruparlos
    if discriminante > 0:
        #usamos contador para los que dan 2 raíces
        raicesDiferentes = raicesDiferentes + 1
    elif discriminante < 0:
        #usamos contador para los que dan una única raíz
        raicesImaginarias = raicesImaginarias + 1
    elif discriminante == 0:
        #usamos contador para los que están en el campo de los imaginarios
        raicesIguales = raicesIguales + 1

    #preguntamos si quiere seguir cargando mas discriminantes o no
    opcion = int(input("¿Desea cargar más discriminantes? 1- SI / 2- NO: "))

#sumamos en total los distintos contadores para saber cual es el 100%
total = raicesDiferentes + raicesImaginarias + raicesIguales
#calculamos porcentaje
porcentaje = (raicesImaginarias * 100) / total

#mostramos por pantalla lo pedido
print("La cantidad de discriminantes que darán 2 raíces son:", raicesDiferentes)
print("La cantidad de discriminantes que darán una unica raíz son:", raicesImaginarias)
print("La cantidad de discriminantes que darán raíces imaginarias son:", raicesIguales)
print("El porcentaje que representan las raíces imaginarias sobre el total de discriminantes es:", porcentaje)
