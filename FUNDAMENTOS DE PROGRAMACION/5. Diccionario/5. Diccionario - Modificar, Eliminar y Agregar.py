# MODIFICAR

# EJEJMPLO 1 - Modificar Valor por su Clave

diccionario = {'gato': 'minou', 'perro': 'chien', 'caballo': 'cheval'}

diccionario['gato'] = 'minou'            # Asignamos la Clave y reemplazamos su clave
print(diccionario)


# AGREGAR

# EJEMPLO 1 - Agregar Valor con su Clave

diccionario_1 = {'gato': 'minou', 'perro': 'chien', 'caballo': 'cheval'}

diccionario_1['cisne'] = 'cygne'
print(diccionario_1)

# Usamos el metodo update(), permite actualizar el diccionario
# EJEMPLO 2
dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary.update({"pato": "canard"})       # update({ clave : valor })
print(dictionary)


# ELIMINAR

# Con la instruccion del, asi como en las listas
# EJEMPLO 1

dictionary_1 = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dictionary_1['perro']           # Solo es necesario eliminar su clave y se elimina tambien su valor
print(dictionary_1)                 # Porque no puede exitir una clave sin valor y un valor sin su clave

# Usamos el metodo popitem(), permite elimar el ultimo elemento del diccionario
# EJEMPLO 2
dictionary_2 = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary_2.popitem()
print(dictionary_2)


# El metodo clear(), permite elimar todos los elementos del diccionario
# EJEMPLO 3

dictionary_3 = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dictionary_2.clear()
print(dictionary_3)
