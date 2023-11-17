# La asignación: list_2 = list_1 copia el nombre del arreglo no su contenido. En efecto, los dos nombres (list_1 y list_2)
# identifican la misma ubicación en la memoria de la computadora. Modificar uno de ellos afecta al otro, y viceversa.

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2, list_1)   # Es decir que almacena la ubicacion de memoria de list_1 para list_2
                        # list_2 = 2


# Si deseas copiar el contenido de la Lista y no la ubicacion donde esta almacenado, tendrias que hacer [start:end]
# por defecto copia todos los valores, pero si deseas copiar algunos valores, te brinda un rango inicial y finale - 1

# Rebanadas Poderosas

# Una rebanada es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista, o partes de una lista.
# En realidad, copia el contenido de la lista, no el nombre de la lista

# Copiando la lista entera.
list_1 = [1]
list_2 = list_1[:]          # [:] copia todos los contenido de la Lista
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]        # [start:end - 1] = es decir toma los valores en el rango, es decir 1 a 3-1 y
print(new_list)                # 6 en la posicion 2, ya que la posicion final es 3 pero asigna al valor menor
