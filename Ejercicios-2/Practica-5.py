# Ejercicio 2: Calculadora de Formas Geométricas

# Objetivo: Demostrar Abstracción y Polimorfismo.

# Vas a construir una aplicación que calcule el área y el perímetro de diferentes formas geométricas.

# Instrucciones:

# Clase Abstracta Forma:

# Crea una clase abstracta llamada Forma.
# Esta clase debe tener un método abstracto calcularArea() que devuelva un double.
# Esta clase debe tener un método abstracto calcularPerimetro() que devuelva un double.
# (Opcional) Puedes añadir un atributo nombre para la forma y su encapsulamiento.

# Clases Concretas Circulo y Rectangulo:
# Crea dos clases, Circulo y Rectangulo, que hereden de la clase Forma.
# Circulo debe tener un atributo para el radio.
# Rectangulo debe tener atributos para ancho y alto.
# Implementa los constructores para inicializar sus atributos.
# Sobreescribe los métodos calcularArea() y calcularPerimetro() en cada clase con la lógica específica para esa forma.
# Para Circulo: Área = π * radio², Perímetro = 2 * π * radio.
# Para Rectangulo: Área = ancho * alto, Perímetro = 2 * (ancho + alto).
# Clase de Prueba (Main o similar):

# Crea una lista (o array) de objetos de tipo Forma.
# Añade instancias de Circulo y Rectangulo a esta lista.
# Itera sobre la lista y, para cada Forma, llama a calcularArea() y calcularPerimetro().
# Observa cómo, a pesar de que todas las llamadas se hacen a través de una referencia de tipo Forma, el método correcto (específico de Circulo o Rectangulo) es invocado. Esto es el Polimorfismo en acción.
# Imprime los resultados de área y perímetro para cada forma.
#######################################################################################################################################
#######################################################################################################################################

# Para una clase abstracta en python utilizamos el modulo abc y el decorador @abstractmethod

from abc import ABC, abstractmethod
import math


# Una clase Abstacta se puede decir que sirve como una plantilla y que no se instancía directamente


class forma(ABC):

    def __init__(self, nombre: str):
        self._nombre = nombre

    @abstractmethod
    def calcularArea(self) -> float:
        # -> nos permite indicar que el metodo debe devolver un numero de tipo float
        pass

    @abstractmethod
    def calcularPerimetro(self) -> float:
        pass

# metodo para obtener el nombre de la forma
    def getNombre(self) -> str:
        return self._nombre


class Circulo(forma):

    """
       Implementación concreta de una forma: Círculo.
       - Atributo principal: radio (float positivo).
       - Fórmulas:
           * Área       = π * r^2
           * Perímetro  = 2 * π * r
       """

    def __init__(self, radio: float):

        # Validamos que el radio sea mayor que 0

        if not isinstance(radio, (int, float)):
            raise TypeError("El radio debe ser un número")

        if radio <= 0:
            raise ValueError("El radio debe ser mayor que 0")

        super().__init__("circulo")
        self.__radio = radio

    def calcularArea(self) -> float:
        return math.pi * (self.__radio ** 2)

    def calcularPerimetro(self) -> float:
        return 2 * math.pi * self.__radio

    def getRadio(self) -> float:
        return self.__radio


class Rectangulo(forma):
    def __init__(self, ancho: float, alto: float):

        # validamos que los valores sean mayores que 0
        if ancho <= 0 or alto <= 0:
            raise ValueError("El ancho y el alto deben ser mayores que 0")

        if not isinstance(ancho, (int, float)):
            raise TypeError("El ancho debe ser un número")

        super().__init__("rectangulo")
        self.__ancho = ancho
        self.__alto = alto

    def calcularArea(self) -> float:
        return self.__ancho * self.__alto

    def calcularPerimetro(self) -> float:
        return 2 * (self.__ancho + self.__alto)

    def getAncho(self) -> float:
        return self.__ancho

    def getAlto(self) -> float:
        return self.__alto


if __name__ == "__main__":

    formas: list[forma] = [
        Circulo(5),
        Rectangulo(4, 6),
        Circulo(3.8),
        Rectangulo(22, 8)
    ]

    print("Calculadora de Formas Geométricas")

    for f in formas:
        area = f.calcularArea()
        perimetro = f.calcularPerimetro()

        print(f"{f.getNombre():<10} - Área: {area:.2f}, Perímetro: {perimetro:.2f}")
