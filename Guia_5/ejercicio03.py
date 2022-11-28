"""Solamente 'a' Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado en punto. 
En base al texto ingresado, determinar: 
a) Cuál es la longitud de la palabra más larga. 
b) Cuántas palabras tienen la a como única vocal 
c) Qué 
Ejemplo: "el agua clara salta por las piedras." 
La longitud de la palabra más larga es 7 letras.
Las palabras cuya única vocal es la a son: 3 El porcentaje de estas palabras sobre el total es 43 %"""

print("-- S O L A M E N T E  'A' --")

def analisis_texto(texto):
    #declaramos variables
    vocales = ("e", "i", "o", "u")
    palabrasIngr = int()
    palabraLarga = int()
    palabrasA = int()
    porcentPalabrA = float()
    contador = int()
    #
    for palabra in texto.split():
        #usamos condicional para saber cual es la palabra mas larga
        if (palabrasIngr == 1 or len(palabra) > palabraLarga):
            palabraLarga = len(palabra)
        #usamos for para saber cuantas palabras tienen unicamente la vocal A
        for letra in palabra:
            if (letra in vocales): 
                contador = contador + 1
        if (contador == 0): 
            palabrasA = palabrasA + 1 
        contador = 0 
        palabrasIngr = palabrasIngr + 1
    #sacamos el porcentaje
    porcentPalabrA = int(palabrasA * 100 / palabrasIngr) #Punto A
    #mostramos por pantalla lo pedido
    print(f"La longitud de la palabra mas larga es:", palabraLarga, "letras")
    print(f"Las palabras que tienen como unica vocal la 'A' son:", palabrasA)
    print(f"El porcentaje de las que sólo tienen la vocal 'A' sobre el total es:", porcentPalabrA, "%")
#mostramos por pantalla el def analisis_texto con el texto dentro
analisis_texto("el agua clara salta por las piedras.")
