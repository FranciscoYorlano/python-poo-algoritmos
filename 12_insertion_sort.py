# Complejidad algoritmica O(n**2) en el peor de los casos
import random
import time


def insertion_sort(lista):


C: \Users\franc\Google Drive\Programacion\Course notes Platzi\Data Science\02 - POO y algoritmos con Python\12_insertion_sort.py
   for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion_actual = i

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        lista[posicion_actual] = valor_actual

    return lista


if __name__ == '__main__':
    tamano = int(input("Elige un tamaño de lista: "))

    lista = [random.randint(0, tamano) for i in range(tamano)]
    print('Lista creada.')

    print('Comenzando insertion sort..')
    t0 = time.time()
    lista_ordenada = insertion_sort(lista)
    tf = time.time()

    print('Imprimiento lista ordenada....')
    print(lista_ordenada)

    # prueba_cronometro:
    if tf - t0 >= 1:
        print(
            f'Se resolvio en {tf - t0} segundos')
    else:
        print(
            f'Se resolvio en {(tf - t0) * 1000} milisegundos')
