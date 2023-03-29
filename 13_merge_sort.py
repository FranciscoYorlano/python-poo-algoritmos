# MERGE SORT
# divide la lista en partes iguales hasta que queden sublistas de 1 o 0 elementos.
# Luego las combina de manera ordenada
# Complejidad O(n log n)
import random
import time


def merge_sort(lista):
    if len(lista) > 1:
        middle = len(lista) // 2
        left = lista[:middle]
        right = lista[middle:]
        print(left, '='*5, right)

        # Llamada recursiva en cada mitad
        merge_sort(left)
        merge_sort(right)

        # Iteradores para recorrer sub listas y lista principal
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
        print(f'Left: {left}, Right: {right}')

    return lista


if __name__ == '__main__':
    tamano = int(input("Elige un tamaño de lista: "))

    lista = [random.randint(0, tamano) for i in range(tamano)]
    print(lista)
    print('Lista creada.')

    print('Comenzando insertion sort..')
    t0 = time.time()
    lista_ordenada = merge_sort(lista)
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
