# ¡el except por defecto debe ser el último except! ¡Siempre!

try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))
except ValueError:
    print('No se que hacer con', value)
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')
except:                 # except por defecto
    print('Ha sucedido algo extraño, ¡lo siento!')