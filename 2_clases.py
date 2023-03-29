class Coordenada:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        z_diff = (self.z - otra_coordenada.z)**2

        return (x_diff + y_diff + z_diff)**0.5


def main():
    a = Coordenada(56, 5, 0)
    b = Coordenada(-6, 2, 1)

    print(a.distancia(b))
    print(type(a))

    # El metodo 'isinstance(<obj>, <class>)' devuelve True si efectivamente es instancia
    print(isinstance(a, Coordenada))


if __name__ == '__main__':
    main()
