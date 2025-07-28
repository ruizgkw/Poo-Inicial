# Define una clase llamada Calculadora.
# Agrega un constructor que inicialice un atributo resultado en 0.
# Define métodos para sumar, restar y mostrar el resultado.
# Instancia un objeto de la clase Calculadora y utiliza sus métodos para realizar operaciones y mostrar el resultado final.

class calculadora:  # definimos la clase calculadora
    def __init__(self):
        self.resultado = 0

    def sumar(self, num1, num2):  # definimos el metodo sumar
        self.resultado = num1 + num2

    def restar(self, num1, num2):  # definimos el metodo restar
        self.resultado = num1 - num2

    # metodo mostrar_resultado, esto imprime el resultado de la operacion
    def mostrar_resultado(self):
        print(f"El resultado es: {self.resultado}")


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación a realizar (suma o resta): ")

calcular = calculadora()  # instanciamos el objeto calcular y definimos las operaciones
if operacion == "suma":
    calcular.sumar(num1, num2)
    calcular.mostrar_resultado()
elif operacion == "resta":
    calcular.restar(num1, num2)
    calcular.mostrar_resultado()
