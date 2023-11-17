
# EJEMPLO 1 - ENVIO DE UNA LISTA COMO ARGUMENTO
def lista_suma(lst):                # lst, es un parametro que recibe un argumento
    s = 0
    for elem in lst:
        s += elem                   # Suma todos los valores de la lista
    return s

print (lista_suma([2,3,4,5,7]))     # Pasamos una lista como argumento a nuestra funcion.


#---------------------------------------------------------------------------------------------------------------

# EJEMPLO 2 - ERROR DE ENVIO DE ARGUMENTO
def lista_suma2(lista):
    s=0
    for i in lista:
        s += i
        return s

print (lista_suma2(5))          # TypeError: 'int' object is not iterable
# Es porque el bucle for, trabaja con al menos 2 valores

