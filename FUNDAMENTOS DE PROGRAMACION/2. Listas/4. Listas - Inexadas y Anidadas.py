
# Las listas se pueden indexar y actualizar

mi_lista = [1, None, True, "Soy una cadena", 256, 0]
print(mi_lista[3])  # salida: Soy una cadena
print(mi_lista[-1])  # salida: 0

mi_lista[1] = '?'
print(mi_lista)  # salida: [1, '?', True, 'Soy una cadena', 256, 0]

mi_lista.insert(0, "primero")
mi_lista.append("último")
print(mi_lista)  # outputs: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'último']


# Las listas pueden estar anidadas, por ejemplo:

my_list = [1, 'a', ["lista", 64, [0, 1], False]]