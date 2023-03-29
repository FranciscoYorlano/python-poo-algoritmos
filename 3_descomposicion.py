# Consiste en partir un problema en problemas mas pequeños
# Las clases permiten crear mayores abstracciones en forma de componentes
# Cada clase se encarga de una parte del problema y el programa se vuelve mas
# facil de mantener


class Automovil:
    def __init__(self, marca, modelo, color, combustible=100):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.combustible = combustible
        self._estado = 0
        self._motor = Motor(cilindros=10)

    def acelerador(self, porcentaje=0.2):
        assert combustible < relacion, 'No tienes combustible'

        self._estado = 1
        print('Motor encendido')

        self.relacion = porcentaje**2
        self._motor.inyecta_gasolina(relacion)
        self.combustible -= relacion
        print(
            f'Menos {relacion} litros de combustible, quedan {self.combustible}')


class Motor:
    # 'gasolina' es un default key word del atributo tipo
    def __init__(self, cilindros, tipo='Gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0.0

    def inyecta_gasolina(self, cantidad):
        pass
