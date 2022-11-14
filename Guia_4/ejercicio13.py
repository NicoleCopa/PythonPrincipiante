"""De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
Para guardar esta información se van a utilizar dos arreglos:
- Nombre: Lista para guardar los nombres de los conductores.
- kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor. 
Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado."""

#declaramos variables y listas
nombre = []
total_kms = []
conductores = int()
conductor = str()
acumulador = int()

#pedimos al usuario que ingrese la cantidad de conductores
conductores = int(input("Ingrese la cantidad de conductores: "))
#usamos for para repetir por todos los conductores
for i in range (conductores):
    #pedimos al usuario que ingrese el nombre del conductor
    conductor = str(input("Ingrese el nombre del conductor: "))
    #usamos for para pasar por los dias de la semana
    for dia in range (1,8):
        #imprimimos el dia por pantalla
        print("Dia 0"+ str(dia))
        #pedimos al usuario que ingrese los kilometros que realizó
        kilometros = int(input("Ingrese los kilómetros que realizó: "))
        #usamos un acumulador para guardar todos los kilometros
        acumulador = acumulador + kilometros
    #agregamos acumulador en la lista
    total_kms.append(acumulador)
    #agregamos conductor a la lista
    nombre.append(conductor)
    #reiniciamos el acumulador en 0
    acumulador = 0
#usamos for para pasar por todos los conductores y repetir el print
for j in range (conductores):
    #imprimimos lo pedido en pantalla
    print(nombre[j], "ha realizado", total_kms[j], "kms")
