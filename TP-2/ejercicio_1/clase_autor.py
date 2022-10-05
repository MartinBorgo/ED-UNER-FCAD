class Autor:
    def __init__(self, apellido, nombre):
        self.apellido = apellido
        self.nombre = nombre

    def __str__(self):
        return "Nombre: %s, Apellido: %s" %(self.nombre, self.apellido)

    def __eq__(self, otro):
        if isinstance(otro, Autor):
            return self.apellido == otro.apellido and self.nombre == otro.nombre
        else:
            print("El objeto a comparar no pertenece a una instancia de Autor")