# Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club.
# Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento
# mediante el ingreso de un nombre vacío. Precondición: el formato del nombre de los socios será: nombre apellido.
# Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un apellido,
# el usuario sólo ingresará uno. Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa
# debe dejar al usuario en un bucle hasta que ingrese un DNI correcto. Por cada socio se debe imprimir su identificador
# único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI.
# Ejemplo:
# Nombre: Alba María Linares
# DNI: 25834910
# Alba7258

    # El metodo title(), convierte la primera letra en mayuscula de cada palbra
    # El metodo join(), convierte en cadena una lista o tupla
    # El metodo strip(), quita los espacios vacios de una cadena
def palabraXpalbra(palabra):
    palabra = list(palabra)

    primer_palabra = []
    segundo_palabra = []

    if not ' ' in palabra:
        primer_palabra = ''.join(palabra).strip()
        segundo_palabra = ''.join(segundo_palabra).strip()
        return primer_palabra, segundo_palabra

    else:
        letra_vacia = palabra.index(' ')
        for i in range(len(palabra)):
            if i in range(letra_vacia):
                primer_palabra.append(palabra[i])
            else:
                segundo_palabra.append(palabra[i])

        primer_palabra = ''.join(primer_palabra).strip()
        segundo_palabra = ''.join(segundo_palabra).strip()

        return primer_palabra, segundo_palabra

while True:
    try:
        nombre = str(input("Ingrese su Nombre, Precio 'Enter' para salir: ")).title()
        if nombre == '':
            print("Gracias por Ingresar. Vuelva Pronto")
            break
        apellido = input("Ingrese sus Primer Apellidos: ").title()

        while True:
            dni = str(input("Ingrese su DNI: "))
            if len(dni) in range(7, 9):
                dni = list(dni)
                break
            else:
                print("Ingrese un DNI correcto. El DNI tiene 7 u 8 digitos, vuelve a ingresar...")

        primer_nombre, segundo_nombre = palabraXpalbra(nombre)
        primer_apellido, segundo_apellido = palabraXpalbra(apellido)

        id = primer_nombre + str(len(primer_apellido)) + ''.join(dni[0:3])
        print(f"\n\t--DATOS--")
        print(f"Nombre: {primer_nombre} {(segundo_nombre)} {primer_apellido}")
        print(f"DNI: {''.join(dni)}")
        print(f"ID: {id}\n")

    except ValueError:
        print("No ingrese numero a su nombre")