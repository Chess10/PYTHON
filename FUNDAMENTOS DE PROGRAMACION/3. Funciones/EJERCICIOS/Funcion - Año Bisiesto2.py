# Función para determinar si un año es bisiesto
def es_anio_bisiesto(anio):
    # Un año es bisiesto si es divisible por 4 y no es divisible por 100, o si es divisible por 400.
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Función para validar la entrada del usuario
def validar_entrada(mensaje, opciones_validas):
    while True:
        # Solicita la entrada del usuario, elimina espacios en blanco y convierte a mayúsculas
        entrada = input(mensaje).strip().upper()
        # Comprueba si la entrada contiene alguna de las opciones válidas
        for opcion in opciones_validas:
            if opcion in entrada:
                return opcion
        print("Entrada no válida. Por favor, ingresa una de las opciones válidas.")

# Solicita al usuario un año en el rango de 1000 a 9999
while True:
    anio = int(input("Ingrese un año (1000-9999): "))
    if 1000 <= anio <= 9999:
        break
    else:
        print("\nAño no válido. Debe estar en el rango de 1000 a 9999.")

# Valida si el año es bisiesto y solicita al usuario si cree que es bisiesto o no
respuesta = validar_entrada(f"¿El año {anio} es bisiesto? (Si/No): ", ["SI", "NO"])

# Determina el resultado basado en la validación del año y la respuesta del usuario
if es_anio_bisiesto(anio):
    if respuesta == "SI":
        resultado = "CORRECTO"
    else:
        resultado = "FALLIDO"
else:
    if respuesta == "SI":
        resultado = "FALLIDO"
    else:
        resultado = "CORRECTO"

# Imprime el resultado basado en la validación del año
print(f"{resultado}, {anio} {'es' if es_anio_bisiesto(anio) else 'no es'} un año bisiesto.")

