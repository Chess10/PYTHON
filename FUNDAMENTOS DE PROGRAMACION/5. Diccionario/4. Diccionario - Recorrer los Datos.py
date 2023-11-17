
diccionario = {
                "gato" : "chat",
                "perro" : "chien",
                "caballo" : "cheval"
                }

# El Metodo keys(), permite recorrer a traves de las claves dentro del Diccionario

# EJEMPLO 1

for key in diccionario.keys():      # Metodo Keys()
    print(key, "->", diccionario[key])


# El Metodo items(), permite recorrer a traves de las claves dentro del Diccionario

# EJEMPLO 2

for spanish, french in diccionario.items():     # spanish, {gato, perro, caballo} son las claves
    print(spanish, "->", french)                # french, {chat, chien, cheval}  son los valores


# El Metodo values(), permite retornar los valores del diccionario sin las claves

# EJEMPLO 3

for french in diccionario.values():
    print(french)
