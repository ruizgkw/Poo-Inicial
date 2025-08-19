import json
import os
from contacto import Contacto


class AgendaContactos:

    """
    Clase que gestiona una coleccion de contactos

    Atributos:
        contactos: (List): Lista de Objetos Contacto
        Ruta_archivo (Str): ruta al archivo de alamacenamiento

    """

    def __init__(self, ruta_archivo='contactos.json'):
        """
        Inicializa una nueva agenda de contactos.

        Args:
            ruta_archivo (str, optional): Ruta al archivo de almacenamiento de los contactos.
        """
        self.contactos = []
        self.ruta_archivo = ruta_archivo
        # intentar cargar contactos existente si el archivo ya existe
        self.cargar_contactos()

    def agregar_contacto(self, contacto):
        """
        Agrega un nuevo contacto a la agenda.

        Args:
            contacto (Contacto): Objeto de contacto a agregar.
        Returns:
            bool: True si se agrego correctamente, false si ya existe
        """

        # verificar si el contacto ya existe con el mismo nombre
        for c in self.contactos:
            if c.nombre.lower() == contacto.nombre.lower():
                print("El contacto ya existe")
                return False
        # Si no existe lo agrega a la lista
        self.contactos.append(contacto)
        return True

    def buscar(self, termino):
        """
        Busca contactos que coincidan con un termino de busqueda.

        Args:
            termino (str): Termino de busqueda en nombre, telefono o email

        Returns:
            List: Lista de contactos que coinciden con el termino de busqueda.
        """
        resultados = []
        termino = termino.lower()

        for contacto in self.contactos:
            if (termino in contacto.nombre.lower() or
                termino in contacto.telefono.lower() or
                termino in contacto.correo.lower() or
                    termino in contacto.direccion.lower()):
                resultados.append(contacto)

        return resultados

    def actualizar(self, nombre=None, telefono=None, correo=None, direccion=None):
        """
        Actualiza los datos de un contacto existente.

        Args:
            nombre (str): Nombre del contacto a actualizar.
            telefono (str, optional): Nuevo numero de telefono.
            correo (str, optional): Nueva direccion de correo.
            direccion (str, optional): Nueva direccion de ubicacion.
        """
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                contacto.actualizar_contacto(
                    nombre, telefono, correo, direccion)
                return True
        return False

    def eliminar(self, nombre):
        """
        Elimina un contacto de la agenda.

        Args:
            nombre (str): Nombre del contacto a eliminar.

        Returns: 
            bool: True si se elimina correctamente,false si no se elimina
        """
        for i, contacto in enumerate(self.contactos):
            if contacto.nombre.lower() == nombre.lower():
                del self.contactos[i]
                return True
            return False

    def listar(self):
        """
        Lista todos los contactos en la agenda.

        Returns:
            List: Lista de todos los contactos en la agenda.
        """
        return self.contactos

    def guardar(self):
        """
        bool: true si se guardo correctamente, false si no se guardo
        """
        try:
            # Convertir la lista de contactos a diccionarios

            datos = []
            for contacto in self.contactos:
                datos.append({
                    'nombre': contacto.nombre,
                    'telefono': contacto.telefono,
                    'correo': contacto.correo,
                    'direccion': contacto.direccion
                })
            # Guardar en formato JSON
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar los contactos: {e}")
            return False

    def cargar_contactos(self):
        """
        Carga los contactos desde un archivo JSON.

        Returns:
            bool: True si se cargaron correctamente, False si no se cargaron.
        """
        if not os.path.exists(self.ruta_archivo):
            return False
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
            # Convertir los diccionarios a objetos Contacto

            self.contactos = []
            for dato in datos:
                contacto = Contacto(
                    dato['nombre'],
                    dato['telefono'],
                    dato.get['correo', ""],
                    dato.get['direccion', ""])
                self.contactos.append(contacto)
            return True
        except Exception as e:
            print(f"Error al cargar los contactos: {e}")
            return False
