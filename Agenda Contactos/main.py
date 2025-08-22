"""
Ejecuta el sistema agenda contactos

"""

from interfaz_consola import InterfazConsola


def main():
    """ Funcion principal del programa """
    print("Bienvenido a la Agenda de Contactos")
    app = InterfazConsola()
    app.ejecutar()


if __name__ == "__main__":
    main()
