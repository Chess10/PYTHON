# EJEMPLO 1 - Unir  Tuplas

mi_tupla = (1,2,3,4)
mi_tupla_2 = (5,6,7,8)

tupla = mi_tupla + mi_tupla_2
print (tupla)

# EJEMPLO 2 - Multiplicar Tupla

mi_tupla_3 = (2,4,6)

tupla_1 = mi_tupla_3 * 2        # Multiplica la Tupla no los valores que contien la Tupla
print(tupla_1)


# EJEMPLO 3 - Esta en la Tupla

mi_tupla_4 = (1,2,3,4,5)
print(4 in mi_tupla_4)          # Verdadero = True, si esta en la Tupla


# EJEMPL0 4 - No esta en la Tupla

mi_tupla_5 = (1,2,3,4,5)        # Verdadero = True, 10 no esta en la Tupla
print(10 not in mi_tupla_5)