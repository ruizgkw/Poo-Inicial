"""
Contiene la interfaz de consola con la que va a interactuar el usuario

"""

from agenda_contactos import AgendaContactos
from contacto import Contacto


class InterfazConsola:
    """ 
    Clase que maneja la interaccion con el usuario que maneja la consola

    """

    def __init__(self):
        """ Inicializa la interfaz con una nueva agenda de contactos """

        self.agenda = AgendaContactos()

    def mostrar_menu(self):
        """ Muestra el menu de opciones al usuario """

        print("\n--- Agenda de Contactos ---")
        print("1. Agregar Contacto")
        print("2. Listar Contactos")
        print("3. Buscar Contacto")
        print("4. Actualizar Contacto")
        print("5. Eliminar Contacto")
        print("6. Guardar Cambios")
        print("0. Salir")

    def ejecutar(self):
        """ Ejecuta el programa principal """

        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.actualizar_contacto()
            elif opcion == "5":
                self.eliminar_contacto()
            elif opcion == "6":
                self.guardar_contactos()
            elif opcion == "0":
                # preguntar si quiere guardar antes de salir
                if input("¿Desea guardar los cambios antes de salir? (s/n): ").lower() == "s":
                    self.guardar_contactos()
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def agregar_contacto(self):
        """ Solicita datos al usuaruio y agrega un nuevo contacto a la agenda """
        print("\n--- Agregar Contacto ---")
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        correo = input("Ingrese el correo del contacto: ")
        direccion = input("Ingrese la dirección del contacto: ")

        nuevo_contacto = Contacto(nombre, telefono, correo, direccion)

        if self.agenda.agregar_contacto(nuevo_contacto):
            print(f"✅Contacto '{nombre}' agregado con éxito.")
        else:
            print(f"❌Error al agregar el contacto '{nombre}'.")

    def buscar_contacto(self):
        """ Solicita un nombre al usuario y busca un contacto en la agenda """
        print("\n--- Buscar Contacto ---")
        termino = input("Ingrese el nombre del contacto a buscar: ")
        resultado = self.agenda.buscar(termino)

        if resultado:
            print(f"\n✅Contacto encontrados {len(resultado)} :")
            for i, contacto in enumerate(resultado, 1):
                print(f"{i}. {contacto}")

        else:
            print(f"❌No se encontraron contactos con el término '{termino}'.")

    def actualizar_contacto(self):
        """ Solicita un nombre al usuario y actualiza un contacto en la agenda """

        print("\n--- Actualizar Contacto ---")
        nombre = input("Ingrese el nombre del contacto a actualizar: ")
        contacto = self.agenda.buscar(nombre)

        if contacto:
            print("Ingrese los nuevos datos del contacto:")
            nuevo_nombre = input("Nuevo nombre: ")

            # Verificar si el nuevo nombre ya existe en la agenda
            resultado = self.agenda.buscar(nombre)
            contacto_encontrado = None

            for contacto in resultado:
                if contacto.nombre.lower() == nuevo_nombre.lower():
                    contacto_encontrado = contacto
                    break
            if contacto_encontrado:
                print(f"Contacto encontrado:\n{contacto_encontrado}")
                print(
                    "\nIntroduce los nuevos datos (Deja en blanco para mantener el valor actual):")
            nuevo_nombre = input(
                f"Nuevo nombre [{contacto_encontrado.nombre}]: ")
            nuevo_telefono = input(
                f"Nuevo teléfono [{contacto_encontrado.telefono}]: ")
            nuevo_correo = input(
                f"Nuevo correo [{contacto_encontrado.correo}]: ")
            nueva_direccion = input(
                f"Nuevo dirección [{contacto_encontrado.direccion}]: ")

            # Si deja en blanco, manterner el valor actual
            nuevo_nombre = None if nuevo_nombre == "" else nuevo_nombre
            nuevo_telefono = None if nuevo_telefono == "" else nuevo_telefono
            nuevo_correo = None if nuevo_correo == "" else nuevo_correo
            nueva_direccion = None if nueva_direccion == "" else nueva_direccion

            if self.agenda.actualizar(contacto_encontrado.nombre. nuevo_nombre. nuevo_telefono, nuevo_correo, nueva_direccion):
                print(
                    f"✅Contacto '{contacto_encontrado.nombre}' actualizado con éxito.")

            else:
                print(f"❌Error al actualizar el contacto '{nombre}'.")

    def eliminar_contacto(self):
        """ Solicita un nombre al usuario y elimina un contacto de la agenda """

        print("\n--- Eliminar Contacto ---")
        nombre = input("Ingrese el nombre del contacto a eliminar: ")

        if self.agenda.eliminar(nombre):
            print(f"✅Contacto '{nombre}' eliminado con éxito.")
        else:
            print(f"❌Error al eliminar el contacto '{nombre}'.")

    def listar_contactos(self):
        """ Muestra todos los contactos en la agenda """

        print("\n--- Lista de Contactos ---")
        contactos = self.agenda.listar()
        if contactos:
            for i, contacto in enumerate(contactos, 1):
                print(f"\n--- Contacto {i} ---")
                print(contacto)
            print(f"\nTotal de contactos: {len(contactos)}")
        else:
            print("No hay contactos en la agenda.")

    def guardar_contactos(self):
        """ Guarda los cambios en la agenda """

        if self.agenda.guardar():
            print("✅Cambios guardados con éxito.")
        else:
            print("❌Error al guardar los cambios.")
