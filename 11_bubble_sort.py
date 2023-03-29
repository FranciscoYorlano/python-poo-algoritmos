# BUBBLE SORT
# Recorre la lissta comparando elemento adyacentes e intercambiandolos si estan
# en el orden incorrecto. Este procedimiento se repite hasta que no se requieren
# mas intercambios.

# COMPLEJIDAD ALGORITMICA O(n**2)
import time
import random


def ordenamiento_de_burbuja(lista):
    n = len(lista)
    iteraciones = 0

    for i in range(n):
        print(f'{i} iteracion primera')
        for j in range(0, n - i - 1):      # O(n) * O(n) = O(n**2) >> Crecimiento cuadratico
            if lista[j] > lista[j + 1]:
                print(f'{lista[j]} > {lista[j + 1]}, reasignando')
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        print(f'{lista[j]} < {lista[j + 1]}, OK')
        iteraciones += 1

    print(f'Lista ordenada.. {iteraciones} iteraciones')
    return lista


if __name__ == '__main__':
    tamano = int(input("Elige un tamaño de lista: "))

    lista = [random.randint(0, tamano) for i in range(tamano)]
    print('Lista creada.')

    print('Comenzando bubble sort..')
    t0 = time.time()
    lista_ordenada = ordenamiento_de_burbuja(lista)
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
