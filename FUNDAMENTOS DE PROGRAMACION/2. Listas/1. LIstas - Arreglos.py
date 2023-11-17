# QUE ES UNA LISTA

# Las listas en Python son un poderoso tipo de datos que te permiten crear colecciones de datos mutables.
# Es una propiedad de cualquier tipo de dato en Python que describe su disponibilidad para poder cambiar libremente
# durante la ejecución de un programa

# Una Lista es una secuencia de datos MUTABLES


# LA FUNCION len()
    # toma el nombre de la lista como un argumento y devuelve la cantidad de elementos almacenados en la lista

Numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", Numeros)           # Imprimiendo el contenido de la lista original.

Numeros[0] = 111
print("\nContenido de la lista con cambio:", Numeros)       # Imprimiendo contenido de la lista con 111.

Numeros[1] = Numeros[4]                                     # Copiando el valor del quinto elemento al segundo elemento.
print("\nContenido de la lista con intercambio:", Numeros)    # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(Numeros))              # Imprimiendo la longitud de la lista.

# =============================================================================================================================

# LA SENTENCIA del
    # Es una Instrucción de eliminar un valor dentro de la lista

del Numeros[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(Numeros))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", Numeros)  # Imprimiendo el contenido de la lista actual.

# =============================================================================================================================

# LA FUNCIÓN clear()
    # Es una Instrucción de eliminar todos los valores de la lista

lista = [8,32,1,23,45,6,7]

print("Longitud de la nueva lista:", len(lista))  # Imprimiendo nueva longitud de la lista.
print("Mi lista: ", lista)
print("\nLista Borrada:", lista.clear())     # Imprimiendo la lista vacía.

# =============================================================================================================================

# MÉTODO append() e insert( , )

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append(4)           # El Método "append(valor)" inserta un dato al final de la lista.

print(len(numbers))
print(numbers)

numbers.insert(0, 222)      # El Método "insert(posición,valor)" inserta una dato en la posición escogida
print(len(numbers))
print(numbers)

numbers.insert(1, 333)
print(len(numbers))
print(numbers)

# =============================================================================================================================

# EJMEPLO N°1
    # Paso 1: escribe una línea de código que solicite al usuario
    # reemplazar el número de en medio con un número entero ingresado por el usuario.
    # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
    # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.


dato = int(input("Ingrese un numero a remplazar: "))

hat_list[2] = dato

del hat_list[4]

print (hat_list)
print("La longitud de la lista es: ", len(hat_list))

# =============================================================================================================================

# EJMEPLO N°2
#   Crear tu propia Lista emulando Do While. Hallar la suma de todos los valores de tu lista

lista = []
total = 0

while True:
    valor = int(input("Ingrese valores para tu lista, presiona 0 para terminar: "))
    if valor != 0:
        lista.append(valor)
        total += lista
    else:
        break

for i in range(len(lista)):
    total += lista[i]

print("\n")
print("La Longitud  de tu Lista: ", len(lista))
print("Mi Lista: ", lista)
print("La suma de todos los valores de tu Lista: ", total)

# =============================================================================================================================

# EJMEPLO N°3
#     Crea 2 listas y cambia de valores entre ellos sin auxiliares

lista_1 = [1,3,5,7,9]
lista_2 = [2,4,6,8,10]

lista_1[1], lista_1[2], lista_1[3], lista_1[4], lista_2[0], lista_2[1], lista_2[2], lista_2[3] = \
    lista_2[0], lista_1[1], lista_2[1], lista_1[2], lista_2[2], lista_1[3], lista_2[3], lista_1[4]

lista_tot = lista_1 + lista_2

print(lista_1)
print(lista_2)
print(lista_tot)