# POLIMORFISMO:
# cambiar el comportamientod de la super clase para adaptarlo a la subclase


class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'Soy {self.nombre} y Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    # ejemplo de polimorfismo
    def avanza(self):
        print(f'Soy {self.nombre} Ando en bicicleta')


def main():
    print('===================PRIMERA INSTANCIA===================')
    david = Persona('David')
    david.avanza()

    print('===================SEGUNDA INSTANCIA===================')
    juan = Ciclista('Juan')
    juan.avanza()


if __name__ == "__main__":
    main()
