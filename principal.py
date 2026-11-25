# Elaborado por: Alexandra De Gracia y Diego Kim
# Fecha de creación: 24/11/2026
# Última modificación: 24/11/2026
# Versión: 1.2

from archivos import cargarPersonas

# Programa Principal
listaPersonas = cargarPersonas()

print("Total de personas:", len(listaPersonas))
for persona in listaPersonas:
    print(persona.obtenerCedula(), persona.obtenerNombreCompleto())