"""Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco 
enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule 
lista3 = lista1 + lista2."""

import random

lista1 = []
lista2 = []
lista3 = []
suma = []

for i in range (0,5):
    numero1 = random.randrange(100)
    numero2 = random.randrange(100)
    lista1.append(numero1)
    lista2.append(numero2)
    suma.append(sum(lista1+lista2))
    i = i + 1
    
lista3.append(suma)

print(lista1,lista2)
print(lista3)
