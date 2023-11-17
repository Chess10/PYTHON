# Esta aparece cuando intentas forzar a Python a realizar cualquier operación que provoque una división en la que el
# divisor es cero o no se puede distinguir de cero

try:        # Hago algo
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))

# Me perdono con una de las excepciones de acuerdo con el error
except ValueError:      # Respuesta si la entrada no es un Entero
    print('No se que hacer con', value)
except ZeroDivisionError:   # Respuesta para una division a 0
    print('La división entre cero no está permitida en nuestro Universo.')
