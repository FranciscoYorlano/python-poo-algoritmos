# OPTIMIZACIÓN:
# encontrar el input que nos regresa el output mas bajo/alto de una función

# PROBLEMA DEL MORRAL: similar al problema del cajero electronico

def morral(tamaño, pesos, valores, n):

    if n == 0 or tamaño == 0:
        return 0

    if pesos[n - 1] > tamaño:
        return morral(tamaño, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamaño - pesos[n - 1], pesos, valores, n - 1),
               morral(tamaño, pesos, valores, n - 1))


if __name__ == '__main__':

    tamaño = 250

    pesos = [10, 20, 30, 40, 50, 100, 115, 120]
    valores = [60, 100, 120, 130, 150, 200, 250, 156]

    n = len(valores)

    resultado = morral(tamaño, pesos, valores, n)
    print(resultado)
