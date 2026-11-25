# Elaborado por: Alexandra De Gracia y Diego Kim
# Fecha de creacion: 24/11/2026
# Ultima modificacion: 24/11/2026
# Version: 1.4

import pickle
from clases import Persona

rutaArchivo = "tse_personas"

# Padres originales: 5 hombres y 5 mujeres.
# Formato: (cedula, nombre completo, sexo, ubicacion, fecha de nacimiento)
datosPersonasIniciales = [
    ("1-0234-0101", "Jorge Mora Rojas", "M",
     "Carmen Central San José", "05/03/1960"),
    ("2-0150-0202", "Luis Vargas Solano", "M",
     "Alajuela Alajuela Alajuela", "12/07/1958"),
    ("3-0405-0303", "Carlos Jiménez Mora", "M",
     "Oriental Central Cartago", "20/11/1962"),
    ("4-0120-0404", "Pedro Araya Soto", "M",
     "Heredia Heredia Heredia", "01/02/1955"),
    ("5-0310-0505", "Mario Chaves Ruiz", "M",
     "Liberia Liberia Guanacaste", "15/09/1959"),
    ("1-0234-0606", "Ana Thames Arce", "F",
     "Carmen Central San José", "18/04/1962"),
    ("2-0150-0707", "María Rojas Castro", "F",
     "Alajuela Alajuela Alajuela", "22/08/1961"),
    ("3-0405-0808", "Rosa Díaz Mora", "F",
     "Oriental Central Cartago", "30/01/1963"),
    ("6-0180-0909", "Laura Fonseca Pérez", "F",
     "Puntarenas Puntarenas Puntarenas", "09/12/1960"),
    ("7-0210-1010", "Elena Brenes Quirós", "F",
     "Limón Limón Limón", "27/06/1957"),
]


def crearDatosIniciales():
    """
    Funcionalidad:
    Crea la lista con los 10 padres originales, sin padre ni madre registrados.
    Entrada:
    - Ninguna
    Salida:
    - listaPersonas(list): Lista de 10 objetos Persona (5 hombres y 5 mujeres).
    """
    listaPersonas = []
    for cedula, nombre, sexo, ubicacion, fecha in datosPersonasIniciales:
        listaPersonas.append(Persona(cedula, nombre, sexo, ubicacion,
                                     fecha, "", "", "", ""))
    return listaPersonas


def guardarPersonas(listaPersonas):
    """
    Funcionalidad:
    Escribe la lista de objetos Persona en el archivo binario.
    Entrada:
    - listaPersonas(list): Lista de objetos Persona a guardar.
    Salida:
    - Ninguna
    """
    with open(rutaArchivo, "wb") as archivoBinario:
        pickle.dump(listaPersonas, archivoBinario)


def cargarPersonas():
    """
    Funcionalidad:
    Lee la lista de personas desde el archivo binario o lo recrea con los datos iniciales si no existe o esta danado.
    Entrada:
    - Ninguna
    Salida:
    - listaPersonas(list): Lista de objetos Persona cargados.
    """
    listaPersonas = []
    try:
        with open(rutaArchivo, "rb") as archivoBinario:
            listaPersonas = pickle.load(archivoBinario)
    except (FileNotFoundError, EOFError, pickle.UnpicklingError,
            AttributeError, ValueError, OSError):
        listaPersonas = []
    if not isinstance(listaPersonas, list) or len(listaPersonas) == 0:
        listaPersonas = crearDatosIniciales()
        guardarPersonas(listaPersonas)
    return listaPersonas
