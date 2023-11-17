# ELIMINAR LOS VALORES REPETIDOS DE LA LISTA, USANDO CONJUNTOS

# Version mas detallada
my_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 9]  # 0 -9
lista_actual = []

for i in range(len(my_lista)):  # i = (0 - 8)
    valor = my_lista[i]  # valor = 9
    # 1 no esta en [2 _ 9]
    if valor not in my_lista[i + 1:]:  # 0 no esta en [1 - 9]
        lista_actual.append(valor)

print("La lista con elementos únicos: ", lista_actual)
print(my_lista)

# Version mas simplificada
my_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 9]

my_lista_sin_duplicados = []
for elemento in my_lista:
    if elemento not in my_lista_sin_duplicados:
        my_lista_sin_duplicados.append(elemento)

print(my_lista_sin_duplicados)


# Version Pro

my_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 9]

# Convertir la lista en un conjunto para eliminar duplicados
my_lista_sin_duplicados = list(set(my_lista))       # La funcion 'set()' convierte la lista en un conjunto
                                                    # Un conjunto no puede tener valores repetidos, es decir se almacenas valores uncios
                                                    # Luego la Funcion 'list()' convierte el conjunto a un lista.
print(my_lista_sin_duplicados)


# Version Pro - Mejorado

my_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 9]
elementos_unicos = set()
lista_actual = []

for elemento in my_lista:
    if elemento not in elementos_unicos:
        elementos_unicos.add(elemento)      # Es un Conjunto = {}
        lista_actual.append(elemento)       # Es una Lista   = []

print("La lista con elementos únicos: ", lista_actual)
print("El conjunto de elementos únicos: ", elementos_unicos)


# Version Super Pro

my_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 9]
lista_actual = [x for i, x in enumerate(my_lista) if x not in my_lista[:i]]

print("La lista con elementos únicos: ", lista_actual)
