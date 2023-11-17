# QUE ES UN DICCIONARIO
# El diccionario es otro tipo de estructura de datos de Python. No es una secuencia
# (pero puede adaptarse fácilmente a un procesamiento secuencial)
# y además es mutable.

# Un DICCIONARIO es un conjunto de pares de (claves y valores).

# Cada Clave debe ser Unica
# Una clave puede ser un tipo de dato de cualquier tipo
# Un diccionario no es una lista, asi que no tienen un orden de almacenamiento
# Un diccionario es una herramienta de un solo sentido, es decir: un diccionario español a francés,
# pero no en viceversa, osea de frances a Españo.


# EJEMPLO 1 - Crear un Diccionario
# diccionario {clave: valores, clave: valores, ...,}

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)


# OBSERVACIONES: Las cadenas los podrias implemtar con: (" " o ' '), no afecta el resultado o la busqueda


# EJEMPLO 1
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
              }

# EJEMPLO 2
phone_numbers = {'jefe': 5551234567,
                 'Suzy': 22657854310
                 }

