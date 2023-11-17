# LISTA EN ORDEN INVERSO - MECANICO

# EJEMPLO 1
mi_lista = [10, 1, 8, 3, 5]

mi_lista[0], mi_lista[4] = mi_lista[4], mi_lista[0]
mi_lista[1], mi_lista[3] = mi_lista[3], mi_lista[1]

print(mi_lista)

# EJEMPLO 2
# Puedes usar el bucle for para hacer lo mismo automáticamente, independientemente de la longitud de la lista,
# osea puedes tener una lista infinita de numero

mi_lista2 = [10, 1, 8, 3, 5]
length = len(mi_lista2)             # Funcion len() para obtener la longitud de mi_lista2

for i in range(length // 2):        # ´i´ toma los valores en el rango de (length//2) 0 - 2, que es una division entera entre 5/2 = 2
                                    # y como es un bucle los valores que tomaria ´i´ son (0 - 1)
    mi_lista2[i], mi_lista2[length - i - 1] = mi_lista2[length - i - 1], mi_lista2[i]
 #            0 ,                  4  =   4 ,               0  =>   5, , , , 10
 #            1 ,                  3  =   3 ,               1  =>   5, 3, 8, 1, 10

print(mi_lista2)


# EJEMPLO 3
# El usuario ingresa los valores que tendra nuestra lista y se revertira

mi_lista3 = []
mi_lista3_actual = []
while True:
    valor = int(input("Ingrese valores a tu lista y 0 para finalizar: "))

    if valor != 0:
        mi_lista3.append(valor)         # Insertamos a la lista valores
    else:
        break

mi_lista3_actual = mi_lista3
longitud = len(mi_lista3)               # Longitud de la lista
print("Mi lista 3 actual es: " + str(mi_lista3_actual))

for i in range(longitud // 2):
    mi_lista3[i], mi_lista3[longitud - i - 1] = mi_lista3[longitud - i - 1], mi_lista3[i]   # Invierte Lista


print("Mi Lista 3 Revertida es: " + str(mi_lista3))
print("La longitud de mi lista 3 es: "+ str(longitud))


# LISTA EN ORDEN INVERSO CON LA FUNCION reverse()

mi_lista4 = [5, 3, 1, 2, 4]
print(mi_lista4)

mi_lista4.reverse()
print(mi_lista4)  # salida: [4, 2, 1, 3, 5]