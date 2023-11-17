# EJEMPLO DE NUMERO GRANDES - MECANICO

# Se leen tres números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
num_grande = num1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if num2 > num_grande:
    num_grande = num2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if num3 > num_grande:
    num_grande = num3

# Imprime el resultado.
print("El número más grande es:", num_grande)



# EJEMPLO DE NUMERO GRANDES POR LA FUNCION max()

# con la funcion max(), nos permite encontrar el numero mas grande y luego almacenarlo en una variable
num_grande = max(num1, num2, num3)

# Imprime el resultado.
print("El número más grande es:", num_grande)