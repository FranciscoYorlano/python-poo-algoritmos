# Clase sobre comparacion de algoritmos, mediante los metodos:
# 1) Cronometrar
# 2) Contar operaciones
# 3) Notacion asintótica

# Por ultimo: Resumen de complejidad algorítmica


import time

import sys
sys.setrecursionlimit(1000000)

# ENTORNO DE PRUEBAS ==========================================
if __name__ == '__main__':  # ERROR DE CALCULO op = 25 != 64
    op = 0
    prueba = 6

    def fibonacci_prueba(prueba):
        global op
        op = op + 1
        if prueba == 0 or prueba == 1:

            return 1
        # Por cada llamada se generan 2 >> crecimiento exponencial

        return fibonacci_prueba(prueba - 1) + fibonacci_prueba(prueba - 2)

    # start
    t0 = time.time()
    print(fibonacci_prueba(prueba))
    tf = time.time()
    # end

    # prueba_cantidad_operaciones:
    print(f'{op} operaciones de las {2**prueba} esperadas')

    # prueba_cronometro:
    if tf - t0 >= 1:
        print(
            f'Se resolvio en {tf - t0} segundos')
    else:
        print(
            f'Se resolvio en {(tf - t0) * 1000} milisegundos')


# ==========================================================
# 1) CRONOMETRAR TIEMPO DE RESPUESTA:
# t va a depender mucho del hardware


def cronometro_de_tiempo():
    n = 5000
    print(f'{n}!')

    # CALCULO POR WHILE
    t0 = time.time()
    a = factorial_while(n)
    # cronometro:
    if time.time() - t0 >= 1:
        print(
            f'El calculo por iteracion while se resolvio en {time.time() - t0} segundos')
    else:
        print(
            f'El calculo por iteracion while se resolvio en {(time.time() - t0) * 1000} milisegundos')

    # CALCULO POR FOR
    t0 = time.time()
    b = factorial_for(n)
    # cronometro:
    if time.time() - t0 >= 1:
        print(
            f'El calculo por iteracion for se resolvio en {time.time() - t0} segundos')
    else:
        print(
            f'El calculo por iteracion for se resolvio en {(time.time() - t0) * 1000} milisegundos')

    # CALCULO POR RECURSIVIDAD
    t0 = time.time()
    c = factorial_r(n)
    # cronometro:
    if time.time() - t0 >= 1:
        print(
            f'El calculo por recursividad se resolvio en {time.time() - t0} segundos')
    else:
        print(
            f'El calculo por recursividad se resolvio en {(time.time() - t0) * 1000} milisegundos')

    if a == b == c:
        print('CALCULADO!')


def factorial_r(n):
    '''
    Calcula n! por recursividad
    n int
    return n!
    '''

    if n == 1:
        return n
    else:
        return n * factorial_r(n-1)


def factorial_for(n):
    '''
    Calcula n! mediante productoria con un bucle for
    n int
    return n!
    '''
    respuesta = 1
    for i in range(1, n+1):
        respuesta *= i

    return respuesta


def factorial_while(n):
    '''
    Calcula n! mediante productoria con un bucle while
    n int
    return n!
    '''
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

# ==========================================================
# 2) CONTEO ABSTRACTO DE OPERACIÓN:
# Mide la eficiencia de un algoritmo en base a la cantidad de operaciones que se realizan
# Va mas alla de medir el tiempo (metodo anterior)


def f(x):
    respuesta = 0
    operaciones = 0

    # 1000 iteraciones siempre
    for i in range(1000):
        respuesta += 1
        operaciones += 1

    # x iteraciones
    for i in range(x):
        respuesta += x
        operaciones += 1

    # x**2 iteraciones por 2 operaciones cada iteracion >>> 2x**2
    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1
            operaciones += 1

    print(
        f'Se realizaron {operaciones} operaciones de las {2 * x**2 + x + 1000} esperadas')
    return respuesta


def cuenta_de_operaciones():
    for n in range(50):
        print(f'f({n}) : ')
        print(f'f de {n} = {f(n)}')

# ==========================================================
# 3) CRECIMIENTO ASINTÓTICO
# Mejor forma para medir la eficiencia de un algoritmo.
# El enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito.
# Big O


# LEY DE LA SUMA --------------------------------
def g(x):
    for i in range(x):  # O(n)
        print(i)

    for i in range(x):  # O(n)
        print(i)
# Big O de g >> O(n) + O(n) = O(2n)


def h(x):
    for i in range(x):       # O(n)
        print(i)

    for i in range(x ** x):  # O(n**2)
        print(i)
# Big O de h >> O(n) + O(n**2) = O(n + n**2) = O(n**2)  ((Se ignora el termino de menor exponente))


# LEY DE LA MULTIPLICACIÓN ----------------------
def k(x):
    for i in range(x):      # O(n)

        for j in range(x):  # O(n)
            print(i, j)
# Big O de k >> O(n) * O(n) = O(n**2)


# RECURSIVIDAD MULTIPLE -------------------------
def fibonacci(x):
    if x == 0 or x == 1:
        return 1
    # Por cada llamada se generan 2 >> crecimiento exponencial

    return fibonacci(x - 1) + fibonacci(x - 2)
# Big O de fibonacci >> O(2**n)

# ==========================================================
# 3) CLASES DE COMPLEJIDAD ALGORÍTMICA

#O(1) >> Constante

#O(n) >> Linea

# O(log n) >> Logaritmica

# O(nlogn) >> Logaritmica lineal:

# a partir de esta linea no es recomendable usarlos para inputs grandes

# O(n**k), con k entero >> Polinomial

# O(k**n), con k entero >> Exponencial

# O(n!) >> Factorial
