"""Sílaba "de" en la primera mitad: Desarrollar un programa en Python que permita cargar por teclado un texto completo. 
Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:
a) Determinar cuántas palabras tenían al menos un caracter que era en realidad un dígito (un caracter entre '0' y '9').
b) Determinar cuántas palabras tenían 3 o menos letras, cuántas tenían 4 y hasta 6 letras, y cuántas tenían más de 6 letras.
c) Determinar la longitud de la palabra más larga del texto.
d) Determinar cuántas palabras contuvieron la expresión "de", pero en la primera mitad de la palabra"""

def analisis_texto():
    #declaramos variables
    texto = str()
    textoSinPunto = str()
    palabra = str()
    palabrasIngr = int()
    palabrasDigitos = int()
    palabrasCortas = int()
    palabrasMed = int()
    palabrasLargas = int()
    palabraMasLarga = int()
    palabrasConDe = int()
    #mostramos titulo por pantalla
    print("-- A N A L I S I S  D E  T E X T O --")
    #hacemos uso de while para que el programa siga mientras no termine con punto
    while not(texto.endswith(".")):
        #pedimos al usuario que ingrese un texto
        texto = str(input("Ingrese un texto (para finalizar, termine el texto con un punto): ")).lower()
        if (texto.endswith(".")): 
            textoSinPunto = texto[0: len(texto)-1]
        else: 
            textoSinPunto = texto
        for palabra in textoSinPunto.split():
            #Usamos condicional para saber la cantidad de palabras que tienen digitos
            if not palabra.isalpha(): 
                palabrasDigitos = palabrasDigitos + 1
            #usamos condicional para clasificar las palabras por su tamaño
            if len(palabra) <= 3: 
                palabrasCortas = palabrasCortas + 1
            if len(palabra) >= 4 and len(palabra) <= 6: 
                palabrasMed = palabrasMed + 1
            if len(palabra) > 6: 
                palabrasLargas = palabrasLargas + 1
            #Usamos condicional para determinar la palabra mas larga
            if (palabrasIngr == 1) or (len(palabra) > palabraMasLarga):
                palabraMasLarga = len(palabra)
            #Punto D: Cantidad de palabras con "de"
            if (palabra.find("de") < int(len(palabra) / 2)) and (palabra.find("de") != -1):
                palabrasConDe = palabrasConDe + 1
    #mostramos por pantalla lo pedido
    print("")
    print("La cantidad de palabras que tienen al menos un digito son:", palabrasDigitos)
    print("La cantidad de palabras que tienen 3 letras o menos son:" ,palabrasCortas)
    print("La cantidad de palabras que tienen entre 4 y 6 letras son:", palabrasMed)
    print("La cantidad de palabras que tienen mas de 6 letras:", palabrasLargas)
    print("La longitud de la palabra mas larga del texto son:", palabraMasLarga, "letras.")
    print("La cantidad de palabras que tienen la expresion 'de' en la primera mitad de la palabra son:", palabrasConDe)
#mostramos por pantalla el def de analisis_texto
analisis_texto()
