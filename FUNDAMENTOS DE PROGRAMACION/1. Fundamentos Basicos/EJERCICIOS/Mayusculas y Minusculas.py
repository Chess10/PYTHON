# MAYUSCULA

# El Metodo upper()
    # convierte todos en mayuscula

    # Primera Forma
nombre = str(input("Ingrese su nombre completo: "))

print("Su nombre en Mayuscula es: {:}".format(nombre).upper())  # la funcion upper(), permite transformar una cadena a Mayuscula

    # Segunda Forma
nombre_mayuscula = nombre.upper()       # Convierte en Mayuscula y se almacena en 'nombre_mayuscula'
print("Su nombre en Mayuscula es: {:}".format(nombre_mayuscula))



# MINUSCULA

# El Metodo lower()
    # convierte todos en minuscula

    # Primera Forma
nombre2 = str(input("Ingrese su nombre completo: "))

print("Su nombre en Minuscula es: {:}".format(nombre2).lower())  # la funcion upper(), permite transformar una cadena a Minuscula

    # Segunda Forma
nombre_minuscula = nombre2.lower()  # Convierte en Mayuscula y se almacena en 'nombre_mayuscula'
print("Su nombre en Minuscula es: {:}".format(nombre_minuscula))


# COMBINACIONES ENTRE MAYUSCULA Y MINUSCULA

# El Metodo capitalize()
    # Convierte la primera letra en Mayuscula

    # Primera Forma
nombres = str(input("Ingrese tu nombre completo: "))
print("Su nombre es: {:}".format(nombres).capitalize())

    # Segunda Forma
nombre_mayus_minus = nombres.capitalize()
print("Su nombre es: {:}".format(nombre_mayus_minus))