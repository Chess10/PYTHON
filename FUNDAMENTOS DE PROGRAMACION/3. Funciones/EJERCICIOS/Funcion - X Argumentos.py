# X ARGUMENTOS - LA FUNCION NO DIEFINE CUANTOS ARGUMENTOS ESPERA

# EJEMPLO 1

def suma_varios(*args):  # *args = puede almacenar una lista de parámetros
    result = 0
    for i in args:
        result += i
    return print(result)


suma_varios(3, 5, 6, 7, 8, 9, 10)