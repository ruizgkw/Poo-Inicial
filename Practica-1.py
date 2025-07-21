# Define una clase llamada Animal.
# Agrega un constructor __init__ que reciba los atributos Raza y Genero.
# Define un método llamado informacion que imprima el tipo de animal y genero.
# Instancia un objeto de la clase Animal y utiliza sus atributos y métodos fuera de la clase.

# Creamos la clase Animal
class Animal:
    def __init__(self, raza, genero):
        self.raza = raza
        self.genero = genero

    def informacion(self):
        print(f"El animal es un {self.raza} y su genero es {self.genero}")


animal1 = Animal("Perro", "Macho")

animal1.informacion()
