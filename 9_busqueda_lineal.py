# ALGORITMO DE BUSQUEDA LINEAL
# se busca en todos los elementos de manera secuencial
# el peor de los casos es O(n)
import random


def busqueda_lineal(lista, objetivo):
    match = False

    for i in lista:
        print(f'buscando linea {i}')
        if i == objetivo:
            match = True
            break

    return match


if __name__ == '__main__':
    tamano_lista = int(input("Elige un tamaño para la lista: "))

    objetivo = int(input("Elige un número objetivo: "))

    lista = [random.randint(0, tamano_lista) for i in range(tamano_lista)]

    print(lista)
    encontrado = busqueda_lineal(lista, objetivo)
    print(
        f'El elemento {objetivo} {"existe" if encontrado else "no existe"} en la lista')
    # OP. TERNARIO: <valor true> if <condicion> else <valor false>
