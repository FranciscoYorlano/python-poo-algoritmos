# Enfocarnos en la informacion relevante.
# Separar la informacion central de los detalles secundarios


# Keyword class
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temp=20,):
        self._llenar_tanque(temp)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
        print('Se ha finalizado el lavado!')

    def _llenar_tanque(self, temp):
        print(f'Se esta llenando el tanque con agua a {temp}°C')

    def _anadir_jabon(self):
        print('Añadiendo jabon..')

    def _lavar(self):
        print('Lavando..')

    def _centrifugar(self):
        print('Centrifugando..')


if __name__ == '__main__':
    lavarropas = Lavadora()
    lavarropas.lavar()
