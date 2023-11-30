class Persona:
    def __init__(self, nombre, apellido, dni, edad):
        '''Constructor de la clase Persona.

        Args:
            nombre (str): El nombre de la persona.
            apellido (str): El apellido de la persona.
            dni (str): El DNI de la persona.
            edad (int): La edad de la persona.
        '''
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad

    def obtener_nombre_completo(self):
        '''Obtiene el nombre completo de la persona.

        Returns:
            str: El nombre completo de la persona con la primera letra en mayúscula.
        '''
        return f"{self.nombre.capitalize()} {self.apellido.capitalize()}"

    def obtener_dni(self):
        '''Obtiene el DNI de la persona.

        Returns:
            str: El DNI de la persona.
        '''
        return self.dni

    def obtener_edad(self):
        '''Obtiene la edad de la persona.

        Returns:
            int: La edad de la persona.
        '''
        return self.edad