# Espera esta excepción cuando estás manejando valores que pueden usarse de manera inapropiada en algún contexto.
# En general, esta excepción se genera cuando una función (como int() o float()) recibe un argumento de un tipo adecuado,
# pero su valor es inaceptable.

try:        # Hago algo
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))

# Me perdono con una de las excepciones de acuerdo con el error
except ValueError:      # Respuesta si la entrada no es un Entero
    print('No se que hacer con', value)