class Contacto:
    """
    Clase que representa un contacto con nombre, teléfono y correo electrónico.

    Atributos:
        nombre (str): Nombre del contacto.
        telefono (str): Número de teléfono del contacto.
        correo (str): Dirección de correo electrónico del contacto.
        direccion (str): direccion de ubicacion del contacto. 

    Métodos:
        __init__(self, nombre, telefono, correo, direccion): Inicializa un nuevo contacto.
        __str__(self): Devuelve una representación en cadena del contacto.
    """

    def __init__(self, nombre, telefono, correo='', direccion=''):
        """
        Inicializa un nuevo contacto.

        Args:
            nombre (str): Nombre del contacto.
            telefono (str): Número de teléfono del contacto.
            correo (str): Dirección de correo electrónico del contacto.
        """
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def actualizar_contacto(self, nombre=None, telefono=None, correo=None, direccion=None):
        """
        Actualiza los datos del contacto.

        Args:
            nombre (str): Nuevo nombre del contacto.
            telefono (str): Nuevo número de teléfono del contacto.
            correo (str): Nueva dirección de correo electrónico del contacto.
            direccion (str): Nueva dirección de ubicación del contacto.
        """
        if nombre is not None:
            self.nombre = nombre
        if telefono is not None:
            self.telefono = telefono
        if correo is not None:
            self.correo = correo
        if direccion is not None:
            self.direccion = direccion

    def __str__(self):
        """
        Devuelve una representación en cadena del contacto.

        Returns:
            str: Cadena que representa al contacto.
        """
        return f"Nombre: {self.nombre}\n, Teléfono: {self.telefono}\n, Correo: {self.correo}\n, direccion: {self.direccion}\n"
