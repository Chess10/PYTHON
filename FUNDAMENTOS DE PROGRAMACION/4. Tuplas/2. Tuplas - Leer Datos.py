# Las posiciones de las 0. Tuplas son como las Listas empienzan desde 0 - (n-1)

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])          # Funciona como una Lista
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:       # Recorre por la Tupla
    print(elem)