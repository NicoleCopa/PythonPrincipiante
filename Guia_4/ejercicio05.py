"""Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), 
y posterior ordene los elementos de menor a mayor."""

import random
#declaramos variables y lista
lista = []
numeros = int()
ordenados = int()
#usamos for para que se repita 10 veces el programa
for i in range (10):
    #declaramos un numero aleatorio en numeros
    numeros = random.randrange(10)
    #agregamos el valor a la lista
    lista.append(numeros)
#declaramos ordenados como la lista ordenada de forma ascendente con sorted
ordenados = sorted(lista)
#mostramos por pantalla lo pedido
print("Los números inicializados de forma aleatória son:", lista)
print("Los números ordenados de forma ascendente son:", ordenados)
