
try:        # Hacer algo sin permiso

    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))

except:     # Pedir perdon por lo cometido
    print('No se que hacer con', value)
