
# EJEMPLO 1 - Unir Listas

mi_lista = [1,2,3,4]
mi_lista_2 = [5,6,7,8]

lista = mi_lista + mi_lista_2
print (lista)

# EJEMPLO 2 - Multiplicar Listas

mi_lista_3 = [2,4,6]

lista_1 = mi_lista_3 * 2        # Multiplica la Lista no los valores que contien la lista
print(lista_1)


# EJEMPLO 3 - Esta en la LIsta

mi_lista_4 = [1,2,3,4,5]
print(4 in mi_lista_4)          # Verdadero = True, si esta en la lista


# EJEMPL0 4 - No esta en la Lista

mi_lista_5 = [1,2,3,4,5]        # Verdadero = True, 10 no esta en la Lista
print(10 not in mi_lista_5)