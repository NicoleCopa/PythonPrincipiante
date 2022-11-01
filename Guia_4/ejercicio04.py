"""Programa que declare una lista y la vaya llenando de números hasta que introduzcamos 
un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos)."""

#declaramos variables y lista
lista = []
ingreso = int()
#usamos while para que el programa se repita hasta que el usuario ingese un num negativo
while ingreso >= 0:
    #pedimos al usuario que ingrese un numero negativo
    ingreso = int(input("Ingrese un número - Para finalizar ingrese un numero negativo: "))
    #agregamos el numero a la lista
    lista.append(ingreso)
#mostramos por pantalla los numeros introducidos
print("Los números introducidos son:", lista)
