import math
import argparse
import threading
# Librería para dividir la cantidad de hilos.
from timeit import default_timer as timer

# Para pedir los datos al usuario, la cantidad de elementos y
# la forma de mostrar los datos

parser = argparse.ArgumentParser(description='Ingrese')
parser.add_argument('x', type=int, help='Ingrese la cantidad elementos de la lista')
parser.add_argument('-t', '--t', type=str, help='Ingrese t para guardarlo en texto o p para mostrarlo en pantalla')
args = parser.parse_args()


# Función para generar el arreglo de x elementos
def arreglox(x):
    p = list(range(x))
    return p


# Función para generar 4 arreglos de igual tamaño
# Se divide el arreglo en 4 puntos y se toman estos segmentos
# para hacer 4 nuevos arreglos.
def split_list(a_list):
    cuarto = math.ceil(len(a_list)/4)
    mitad = cuarto*2
    tres_cuartos = cuarto*3
    return a_list[:cuarto], a_list[cuarto:mitad], a_list[mitad:tres_cuartos], a_list[tres_cuartos:]
# Decuelve los arreglos
# Función para calcular la potencia cuadrada de los elemntos en el arreglo


def potencia(lista):
    for i in range(0, len(lista)):
        lista[i] = pow(lista[i], 2)
    return lista


# Funció para tomar la desición de seleccionar t para crear un tex
# o p para imprimir en pantalla el resultado del tiempo
# en caso de no ingresar nada gracias a argparse muestra el resultado
# en pantalla.
def impresion(t, datos):
    if t == 't':
        with open('Resultados.txt', 'w') as filehandle:
            for listitem in datos:
                filehandle.write('%s\n' % listitem)

    # Si no se ingresa un dato se imprime en pantalla
    else:
        print("Tiempo con 1 hilo: ", end_1 - start_1, "segundos \n")
        print("Tiempo real con 4 hilos: ", end_2 - start_2, "segundos")

# Se crea un arreglo vacío para poner los datos que se imprimen en pantalla


info = []


Lista = arreglox(args.x)
# Se asigna el arreglo de x elementos a Lista


# Se inicia el contador para determinar el tiempo que tarda en realizarce
# la operación, ademas se llama a la función para determinar la potencia
# de los elementos del arreglo
start_1 = timer()

potencia(Lista)
# Se llama a la función de potencia donde se agrega la Lista de x
# elementos generada.
end_1 = timer()
# Finaliza el contador

# Parte con 4 hilos
# Se llama a la función para generar los 4 arreglos
A_1, A_2, A_3, A_4 = split_list(arreglox(args.x))

# Se crean los 4 hilos cada uno con un arreglo distinto.
t1 = threading.Thread(target=potencia, args=(A_1, ))
t2 = threading.Thread(target=potencia, args=(A_2, ))
t3 = threading.Thread(target=potencia, args=(A_3, ))
t4 = threading.Thread(target=potencia, args=(A_4, ))

# Se inicia el contador para determinar el tiempo de 4 hilos
start_2 = timer()
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
end_2 = timer()
# Se finaliza el contador

# Se llena una lista con los elementos de información para ser
# guardados en un archivo de texto
info.append("Tiempo con 1 hilo: ")
info.append(end_1 - start_1)
info.append("segundos \n")
info.append("Tiempo real con 4 hilos: ")
info.append(end_2 - start_2)
info.append("segundos \n")

impresion(args.t, info)
