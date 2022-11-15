"""Sólo menores que 7. Desarrollar un programa de Phyton que permita cargar por teclado un secuencia de números, uno por uno. 
Siempre se supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a procesar. El programa debe:
a) Determinar el porcentaje que cantidad de números pares representa en la cantidad total de números ingresados.
b) Determinar cuántos de los números ingresados tenían su último dígito igual a 4 o igual a 5.
c) Determinar el menor de los números ingresados que sean divisibles por 3.
d) Determinar si la secuencia estaba formada sólo por números menores a 7."""

print("-- S O L O  M E NO R E S  D E  7 --")
#función para crear la secuencia de numeros
def secuencia():
    #declaramos variables y lista
    numeros = int(1)
    lista = []
    #usamos while para que se repita mientras sea distinto de 0
    while (numeros != 0):
        #pedimos al usuario que ingrese un numero
        numeros = int(input("Ingrese un numero - Para finalizar ingrese '0': "))
        #guardamos el numero dentro de la lista si es distinto de 0
        if numeros != 0:
            lista.append(numeros)
    #hacemos return a lista
    return lista
#Función para Punto A
def numeros_pares(lista):
    #declaramos variables
    pares = int()
    numIngresados = int()
    porcentaje = float()
    #usamos for para recorrer los numeros de la lista
    for numeros in lista:
        #usamos un contador para saber la cantidad de numeros
        numIngresados = numIngresados + 1
        #usamos condicional para saber que numeros son pares
        if (numeros % 2 == 0):
            #usamos contador para saber cuantos son par
            pares = pares + 1
    #sacamos el porcentaje de numeros pares en total
    porcentaje = round(((pares * 100) / numIngresados),2)
    #mostramos por pantalla lo pedido
    print("La cantidad de números pares que representa en la cantidad total de números ingresados es:", porcentaje, "%")
#Función para Punto B
def ultimo_digito(lista):
    #declaramos variables
    ultimosDigitos = int()
    #usamos for para recorrer los numeros de la lista
    for numeros in lista:
        #usamos condicional para saber que num terminan en 4 o 5
        if (numeros % 10 == 4) or (numeros % 10 == 5):
            #usamos contador para saber el total
            ultimosDigitos = ultimosDigitos + 1
    #mostramos por pantalla lo pedido
    print("La cantidad de números ingresados que tenían su último dígito igual a 4 o 5 son:", ultimosDigitos)
#Función para Punto C
def divisibles(lista):
    #declaramos variables
    divisiblesPor3 = int()
    menor = 9999
    #usamos for para recorrer los numeros de la lista
    for numeros in lista:
        #usamos condicional para saber que numero es menor
        if menor > numeros:
            menor = numeros
        #si el numero menor es divisible por 3, lo guardamos en una variable
        if (menor % 3 == 0):
            divisiblesPor3 = menor
    #mostramos por pantalla lo pedido
    print("El menor de los números ingresados que son divisibles por 3 es:", divisiblesPor3)
#Función para Punto D
def menores_de_7(lista):
    #declaramos variables
    menoresDe7 = int()
    #usamos for para recorrer los numeros de la lista
    for numeros in lista:
        #usamos condicional para saber si hay algun numero mayor o igual a 7 y declaramos la variable como 1
        if (numeros >= 7):
            menoresDe7 = 1
    #usamos condicional para saber si lo anterior se cumple
    if menoresDe7 >= 1:
        #si se cumple, mostramos que la secuencia no está formada solo por num menores a 7
        print("La secuencia no está formada sólo por numeros menores a 7.")
    else:
        #mostramos lo contrario
        print("La secuencia está formada sólo por números menores a 7.")

#Muestra por pantalla
lista = secuencia()
print(lista)
numeros_pares(lista)
ultimo_digito(lista)
divisibles(lista)
menores_de_7(lista)