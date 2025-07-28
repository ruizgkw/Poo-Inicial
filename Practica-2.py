# Define una clase llamada Coche.
# Agrega un atributo marca y un método acelerar que imprima un mensaje indicando que el coche está acelerando.
# Instancia un objeto de la clase Coche y modifica el atributo marca fuera de la clase.
# Llama al método acelerar desde fuera de la clase.


class Coche:
    def __init__(self, marca):
        self.marca = marca

    def acelerar(self):
        print(f"El coche {self.marca} está arrancando")


Coche1 = Coche("Ford")
Coche1.acelerar()
Coche1.marca = "Ferrari"
Coche1.acelerar()
