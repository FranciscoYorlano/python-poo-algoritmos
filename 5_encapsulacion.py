# ENCAPSULACION:
# La encapsulacion describe el hecho de que los objetos se usan como cajas negras.
# Permite agrupar datos y su comportamiento
# Controla el acceso a dichos datos
# Previene modificaciones no autorizadas

# La encapsulacion es un mecanismo de control. El estado (atributos) de un objeto
# solo debe ser modificado por medio de los metodos de dicho objeto.
# La tecnica es conocida como ocultacion de datos, le permite que los atributos de un
# objeto puedan ocultarse pra que no sean accedidos desde fuera de la definicion de una

class Coche():

    # Con init especificamos el metodo constructor de la clase:
    def __init__(self, largo, ancho, color):
        # atributos encasulado ('__') para evitar que se modifique desde fuera de la clase
        self.__largo = largo
        self.__ancho = ancho
        self.__ruedas = 4
        self.__en_marcha = False
        self.__motor = None
        self.__color = color

    def on_off(self, arrancado_apagado):
        if arrancado_apagado:
            if self.__chequeo_interno():
                self.__en_marcha = True
                print('Encendido!')
            else:
                print('Llevame a un mecanico!')

        elif not arrancado_apagado:
            self.__en_marcha = False
            print('Apagado!')

    def pintar(self, color_nuevo):
        self.__color = color_nuevo
        print(f'Se pinto del coche de color {self.__color}')

    def estado(self):
        print(
            f'El coche mide {self.__largo} por {self.__ancho} cm. Tiene {self.__ruedas} ruedas. Es de color {self.__color}')

    # Encapsulamos el metodo ya que no tiene sentido usarlo desde fuera de la clase
    def __chequeo_interno(self):
        print('Inicio de chequeo interno')
        self.gasolina = 'OK'
        self.aceite = 'OK'
        self.puertas = 'OK'

        if self.gasolina == 'OK' and self.aceite == 'OK' and self.puertas == 'OK':
            return True
        else:
            return False


print('==============PRIMERA INSTANCIA==============')
mercedes = Coche(520, 230, 'gris')
mercedes.on_off(True)
mercedes.estado()
mercedes.on_off(False)
# mercedes.__chequeo_interno() >>> esta linea da error porque el metodo esta encapsulado

print('==============SEGUNDA INSTANCIA==============')

audi = Coche(500, 230, 'azul')
audi.on_off(True)
# Como esta encapsulada aunque intentamos modificarla no se modifica:
audi.__ruedas = 2
audi.estado()

# Como el atributo color esta encapsulado no se puede modificar:
audi.__color = 'verde'
audi.estado()

# Si se puede modificar mediante un metodo:
audi.pintar('amarillo')
audi.estado()
