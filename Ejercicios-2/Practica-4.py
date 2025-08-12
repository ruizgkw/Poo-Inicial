
# Ejercicio 1: El Reino Animal
# Objetivo: Demostrar Abstracción, Encapsulamiento y Herencia.

# Imagina que estás construyendo un sistema para gestionar diferentes tipos de animales en un zoológico virtual.

# Instrucciones:

# Clase Base Animal:

# Crea una clase base llamada Animal.
# Esta clase debe tener atributos privados como nombre (String) y edad (int).
# Implementa un constructor para inicializar estos atributos.
# Aplica Encapsulamiento proporcionando métodos públicos getNombre(), getEdad(), setNombre(), setEdad().
# Define un método abstracto hacerSonido() (o un método virtual que pueda ser sobreescrito) que no tome argumentos y no devuelva nada. Este método representará el sonido característico de cada animal.
# Define un método concreto comer() que imprima un mensaje genérico como "El animal está comiendo.".
# Clases Derivadas Perro y Gato:

# Crea dos clases, Perro y Gato, que hereden de la clase Animal.
# Cada clase debe tener un constructor que llame al constructor de la clase base.
# Sobreescribe el método hacerSonido() en cada clase para que imprima el sonido específico del animal (e.g., "Guau guau!" para Perro, "Miau miau!" para Gato).
# Clase de Prueba (Main o similar):

# En tu método principal, crea instancias de Perro y Gato.
# Llama a los métodos getNombre(), getEdad(), comer() y hacerSonido() para cada instancia.
# Demuestra cómo puedes tratar a un Perro o un Gato como un Animal (por ejemplo, en una lista de Animales) y llamar a hacerSonido() para observar el comportamiento polimórfico (aunque el polimorfismo se verá más a fondo en el Ejercicio 2, aquí ya se empieza a vislumbrar).


class Animal:  # se crea la clase
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

# se definen los metodos getter y
# getter nos permite tener acceso a atributo privados de una clase
# Setter es un método público que se usa para modificar (cambiar) el valor de un atributo privado de una clase, de forma controlada y segura.

    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        self.__edad = edad
# se feninen los metodos de comer y hacer sonido

    def hacerSonido(self):
        pass

    def comer(self):
        print("El animal está comiendo.")

# se crean subclases gato y perro


class Perro(Animal):
    # se crea un constructor que llama al constructor principal de la clase base
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hacerSonido(self):
        print("Guau guau!")


class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hacerSonido(self):
        print("Miau miau!")


if __name__ == "__main__":
    perro = Perro("spy", 3)
    gato = Gato("Whiskey", 5)

    print("datos individuales: ")
    print(f"Nombre: {perro.getNombre()}, Edad: {perro.getEdad()}")

    perro.comer()
    perro.hacerSonido()

    print()

    print(f"Nombre: {gato.getNombre()}, Edad: {gato.getEdad()}")

    gato.comer()
    gato.hacerSonido()

    print("\nDemostración de polimorfismo con lista de animales:")

    animales = [perro, gato]
    for animal in animales:
        print(f"Nombre: {animal.getNombre()}, Edad: {animal.getEdad()}")
        animal.hacerSonido()
