# Elaborado por: Alexandra De Gracia y Diego Kim
# Fecha de creacion: 24/11/2026
# Ultima modificacion: 24/11/2026
# Version: 1.3


class Persona:
    """
    Funcionalidad:
    Representa a una persona registrada en el Tribunal Supremo de Elecciones.
    Entrada:
    - Ninguna
    Salida:
    - Ninguna
    """

    def __init__(self, pCedula, pNombreCompleto, pSexo, pUbicacion,
                 pFechaNacimiento, pPadre, pNacionalidadPadre,
                 pMadre, pNacionalidadMadre):
        """
        Funcionalidad:
        Inicializa un objeto Persona con todos sus datos personales y familiares.
        Entrada:
        - pCedula(str): Cedula en formato P-TTTT-AAAA.
        - pNombreCompleto(str): Nombre completo de la persona.
        - pSexo(str): Sexo de la persona ("M" o "F").
        - pUbicacion(str): Ubicacion en formato "Distrito Canton Provincia".
        - pFechaNacimiento(str): Fecha de nacimiento en formato DD/MM/AAAA.
        - pPadre(str): Nombre completo del padre ("" si no esta registrado).
        - pNacionalidadPadre(str): Nacionalidad del padre.
        - pMadre(str): Nombre completo de la madre ("" si no esta registrada).
        - pNacionalidadMadre(str): Nacionalidad de la madre.
        Salida:
        - Ninguna
        """
        self.cedula = pCedula
        self.nombreCompleto = pNombreCompleto
        self.sexo = pSexo
        self.ubicacion = pUbicacion
        self.fechaNacimiento = pFechaNacimiento
        self.padre = pPadre
        self.nacionalidadPadre = pNacionalidadPadre
        self.madre = pMadre
        self.nacionalidadMadre = pNacionalidadMadre

    def asignarCedula(self, pCedula):
        """
        Funcionalidad:
        Asigna el numero de cedula de la persona.
        Entrada:
        - pCedula(str): Nueva cedula de la persona.
        Salida:
        - Ninguna
        """
        self.cedula = pCedula

    def asignarNombreCompleto(self, pNombreCompleto):
        """
        Funcionalidad:
        Asigna el nombre completo de la persona.
        Entrada:
        - pNombreCompleto(str): Nuevo nombre completo de la persona.
        Salida:
        - Ninguna
        """
        self.nombreCompleto = pNombreCompleto

    def asignarSexo(self, pSexo):
        """
        Funcionalidad:
        Asigna el sexo de la persona.
        Entrada:
        - pSexo(str): Sexo de la persona ("M" o "F").
        Salida:
        - Ninguna
        """
        self.sexo = pSexo

    def asignarUbicacion(self, pUbicacion):
        """
        Funcionalidad:
        Asigna la ubicacion de la persona.
        Entrada:
        - pUbicacion(str): Nueva ubicacion de la persona.
        Salida:
        - Ninguna
        """
        self.ubicacion = pUbicacion

    def asignarFechaNacimiento(self, pFechaNacimiento):
        """
        Funcionalidad:
        Asigna la fecha de nacimiento de la persona.
        Entrada:
        - pFechaNacimiento(str): Nueva fecha de nacimiento (DD/MM/AAAA).
        Salida:
        - Ninguna
        """
        self.fechaNacimiento = pFechaNacimiento

    def asignarPadre(self, pPadre):
        """
        Funcionalidad:
        Asigna el nombre completo del padre de la persona.
        Entrada:
        - pPadre(str): Nombre completo del padre.
        Salida:
        - Ninguna
        """
        self.padre = pPadre

    def asignarNacionalidadPadre(self, pNacionalidadPadre):
        """
        Funcionalidad:
        Asigna la nacionalidad del padre de la persona.
        Entrada:
        - pNacionalidadPadre(str): Nacionalidad del padre.
        Salida:
        - Ninguna
        """
        self.nacionalidadPadre = pNacionalidadPadre

    def asignarMadre(self, pMadre):
        """
        Funcionalidad:
        Asigna el nombre completo de la madre de la persona.
        Entrada:
        - pMadre(str): Nombre completo de la madre.
        Salida:
        - Ninguna
        """
        self.madre = pMadre

    def asignarNacionalidadMadre(self, pNacionalidadMadre):
        """
        Funcionalidad:
        Asigna la nacionalidad de la madre de la persona.
        Entrada:
        - pNacionalidadMadre(str): Nacionalidad de la madre.
        Salida:
        - Ninguna
        """
        self.nacionalidadMadre = pNacionalidadMadre

    def obtenerCedula(self):
        """
        Funcionalidad:
        Obtiene el numero de cedula de la persona.
        Entrada:
        - Ninguna
        Salida:
        - cedula(str): Cedula de la persona.
        """
        return self.cedula

    def obtenerNombreCompleto(self):
        """
        Funcionalidad:
        Obtiene el nombre completo de la persona.
        Entrada:
        - Ninguna
        Salida:
        - nombreCompleto(str): Nombre completo de la persona.
        """
        return self.nombreCompleto

    def obtenerSexo(self):
        """
        Funcionalidad:
        Obtiene el sexo de la persona.
        Entrada:
        - Ninguna
        Salida:
        - sexo(str): Sexo de la persona ("M" o "F").
        """
        return self.sexo

    def obtenerUbicacion(self):
        """
        Funcionalidad:
        Obtiene la ubicacion de la persona.
        Entrada:
        - Ninguna
        Salida:
        - ubicacion(str): Ubicacion de la persona.
        """
        return self.ubicacion

    def obtenerFechaNacimiento(self):
        """
        Funcionalidad:
        Obtiene la fecha de nacimiento de la persona.
        Entrada:
        - Ninguna
        Salida:
        - fechaNacimiento(str): Fecha de nacimiento de la persona.
        """
        return self.fechaNacimiento

    def obtenerPadre(self):
        """
        Funcionalidad:
        Obtiene el nombre completo del padre de la persona.
        Entrada:
        - Ninguna
        Salida:
        - padre(str): Nombre completo del padre.
        """
        return self.padre

    def obtenerNacionalidadPadre(self):
        """
        Funcionalidad:
        Obtiene la nacionalidad del padre de la persona.
        Entrada:
        - Ninguna
        Salida:
        - nacionalidadPadre(str): Nacionalidad del padre.
        """
        return self.nacionalidadPadre

    def obtenerMadre(self):
        """
        Funcionalidad:
        Obtiene el nombre completo de la madre de la persona.
        Entrada:
        - Ninguna
        Salida:
        - madre(str): Nombre completo de la madre.
        """
        return self.madre

    def obtenerNacionalidadMadre(self):
        """
        Funcionalidad:
        Obtiene la nacionalidad de la madre de la persona.
        Entrada:
        - Ninguna
        Salida:
        - nacionalidadMadre(str): Nacionalidad de la madre.
        """
        return self.nacionalidadMadre
