# HERENCIA: Permite modelar una jerarquia de clases
# Superclass->Subclass


# SUPERCLASE =====================================
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


# SUBCLASES ======================================
# La clase Cuadrado extiende al Rectangulo
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)  # super refiere a la super clase, algo asi como self


if __name__ == "__main__":
    rectangulo = Rectangulo(3, 4)
    print(rectangulo.area())
    print(type(rectangulo))

    cuadrado = Cuadrado(5)
    print(cuadrado.area())
    print(type(cuadrado))
