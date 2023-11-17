
# EJEMPLO 1 - Diccionario con Listas

diccionario = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

claves = ['gato', 'león', 'caballo']

for clave in claves:
    if clave in diccionario:
        print(clave, "->", diccionario[clave])
    else:
        print(clave, "no está en el diccionario")