# CREACIÓN DE CLASES:
# ATRIBUTOS:
# el metodo __init__  se usa para definir el estado inicial de nuestra instancia.
# el parametro inicial self es obligatorio y refiere a la instancia.
# las variables privadas de una clase comienzan con _

# METODOS (funciones dentro de objetos):
#
class Hotel:
    def __init__(self, nombre, max_huespedes, max_estacionamientos):
        self.nombre = nombre
        self.max_huespedes = max_huespedes
        self.max_estacionamientos = max_estacionamientos
        self.huespedes = 0

    def check_in(self, cantidad):
        self.huespedes += cantidad

    def check_out(self, cantidad):
        self.huespedes -= cantidad

    def ocupacion_total(self):
        return self.huespedes


# Instancias una clase:
Hilton = Hotel('Hilton', 50, 30)

print(hotel.max_huespedes)
print(hotel.max_estacionamientos)

# Uso de metodos del objeto instancido
hotel.check_in(5)
hotel.check_out(2)
print(hotel.ocupacion_total())


# ==================================================
# TIPOS DE DATOS ABSTRACTOS
# En python todo es un objeto y tiene un tipo
