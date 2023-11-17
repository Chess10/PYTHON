
value = None
if value is None:
    print("Lo siento, no contienes ningún valor")



# EJERCICIO 1

def sin_valor():
    print ("yeric")

valor = sin_valor()     # Se invoca a la funcion e imprime el cuerpo de la funcion pero no almacena un valor de retorno
print(valor)            # La variables valor es None porque almacena una funcion sin ningun retorno


def funcion_none(n):
    if(n % 2 == 0):     # Retorna True, si el numero es Par                 True
        return True     # No retorna ningun valor, si el numero en Impar    None

print(funcion_none(2))
print(funcion_none(1))

