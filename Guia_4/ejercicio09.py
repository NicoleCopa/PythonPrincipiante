"""Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
a) La temperatura media de cada día
b) Los días con menos temperatura
c) Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. Si no existe 
ningún día se muestra un mensaje de información."""

#declaramos listas y variables
temperatura = []
temperaturaOrdenada = []
ingreso = int()
maximo = int()
minimo = int()
media = float()

#usamos for para ingresar las temperaturas de los 5 dias
for i in range (1, 6):
    #imprimimos el dia
    print("Dia 0"+ str(i))
    #pedimos al usuario que ingrese la temperatura maxima y minima
    minimo = int(input("Ingrese la temperatura mínima del dia: "))
    maximo = int(input("Ingrese la temperatura máxima del dia: "))
    #sacamos la media de temperatura
    media = (minimo + maximo) / 2
    #mostramos por pantalla la temperatura media
    print("La temperatura media es:", media)
    #agregamos minimo, maximo e i a temperatura
    temperatura.append([minimo, maximo, i])
    i = i + 1
#ordenamos la lista temperatura y la agregamos en temperaturaOrdenada
temperaturaOrdenada = sorted(temperatura)
#mostramos por pantalla ambas listas
print(temperatura)
print(temperaturaOrdenada)
#mostramos por pantalla lo pedido
print("Los dias con menos temperatura son:")
print("Dia 0" + str(temperaturaOrdenada[0][2]) + " con " + str(temperaturaOrdenada[0][0]) + " grados") #el [0] es la sublista y [2] la posición
print("Dia 0" + str(temperaturaOrdenada[1][2]) + " con " + str(temperaturaOrdenada[1][0]) + " grados")
#le pedimos al usuario que ingrese una temperatura
ingreso = int(input("Ingrese una temperatura máxima para consultar con los otros dias: "))
#usamos for para recorrer la lista
for i in temperaturaOrdenada:
    #si i en posición 1 (tempMaxima) es igual a la temperatura ingresada, entonces coincide
    if (i[1] == ingreso):
        print("Dia 0" + str(i[2]) + ": coincide la temperatura máxima")
    else:
        print("Dia 0" + str(i[2]) + ": no coincide la temperatura máxima")
