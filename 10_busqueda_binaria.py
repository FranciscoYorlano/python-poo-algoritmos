# BUSQUEDA BINARIA
# Asume que la lista de busqueda esta ordenada
# El problema se divide en dos en cada iteracion
# En el peor de los casos es
import random
import time


def busqueda_binaria(lista, objetivo):
    # minimo, maximo y respuesta x:
    minimo = 0
    maximo = len(lista)
    i = (minimo + maximo) // 2

    # medición de iteraciones y tiempo de respuesta:
    iteraciones = 0

    # iteraciones de busqueda binari
    while lista[i] != objetivo and iteraciones < len(lista):
        print(f"""
        =============ITERACIÓN: {iteraciones}
        minimo={minimo};
        maximo={maximo};
        i = {i} -> lista[i] = {lista[i]}
        """)

        if lista[i] == objetivo:
            return f'Encontrado en el indice {i}'
        elif abs(minimo - maximo) == 1:
            break
        elif lista[i] < objetivo:
            minimo = i + 1
        elif lista[i] > objetivo:
            maximo = i - 1

        i = (minimo + maximo) // 2
        iteraciones += 1
    return False


if __name__ == '__main__':
    tamano = int(input("Elige un tamaño de lista: "))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, tamano) for i in range(tamano)])

    print('Comenzando busqueda binaria')
    t0 = time.time()
    encontrado = busqueda_binaria(lista, objetivo)
    tf = time.time()
    print(
        f'El elemento {objetivo} {encontrado if encontrado else "no existe"} en la lista')
    # prueba_cronometro:
    if tf - t0 >= 1:
        print(
            f'Se resolvio en {tf - t0} segundos')
    else:
        print(
            f'Se resolvio en {(tf - t0) * 1000} milisegundos')
