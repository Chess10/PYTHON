# Un hotel enorme que consta de tres edificios, de 15 pisos cada uno. Hay 20 habitaciones en cada piso.

# False, las habitaciones estan disponibles
# True, las habitaciones estas ocupadas

hotel = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#              habitaciones             pisos               edificio
#   hotel [habitaciones][pisos][edificio]
#   hotel [[[True]]]
print(hotel)

disponible = 0  #   Si hay habitaciones disponibles

for room_number in range(20):
#   if not True:    es falso, se cumple la condicion: porque en el hotel todas las habitaciones son false
#   not True = False
#   not False = True
    if not hotel[2][14][room_number]:
        disponible += 1

print(len(hotel), disponible)