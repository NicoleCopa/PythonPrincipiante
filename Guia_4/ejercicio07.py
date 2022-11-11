"""Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco 
enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3 = lista1 + lista2."""

#declaramos listas
lista1 = []
lista2 = []
lista3 = []

#usamos for para que el programa se repita 5 veces
for i in range (0,5):
    #pedimos al usuario un numero la lista1
    numero1 = int(input("Ingrese un numero para la lista 1: "))
    #agregamos el numero a lista1
    lista1.append(numero1)
    #pedimos al usuario un numero la lista2
    numero2 = int(input("Ingrese un numero para la lista 2: "))
    #agregamos el numero a lista2
    lista2.append(numero2)
    #sumamos el valor de lista1 y lista2 y lo agregamos a lista3
    lista3.append(sum(lista1+lista2))
    #sumamos i
    i = i + 1
#mostramos por pantalla lo pedido
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("La suma de ambas listas:", lista3)
