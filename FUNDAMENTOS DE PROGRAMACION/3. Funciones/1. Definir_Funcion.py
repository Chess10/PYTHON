# def my_function(parametro):   def, define la funcion
#   cuerpo de la función
#   return expresion

# my_function(argumentos)       invocamos a la funccion

# OJO:
    # parametros: son definidas en la definicion de la funcion
    # argumentos: son valores que se envian a los parametros en la invocacion de la funcion
    # parametros y argumentos tienen que ser iguales, tanto en cantidad, valor y condicion

# PROCESO DE COMO ACTUA LA INVOCACION
# -----------------------------------
# Cuando se invoca una función, Python recuerda el lugar donde esto ocurre y salta hacia dentro de la función invocada.
# El cuerpo de la función es entonces ejecutado.
# Al llegar al final de la función, Python regresa al lugar inmediato después de donde ocurrió la invocación.


# EJEMPLO 1
def mensaje():
    print("Es mi primera funcion")

print("Hola")
mensaje()                              # lo invocamos


# EJEMPLO 2
def mensaje2():
    mensaje = ("Ingrese un valor: ")    # Cuerpo de la funcion, variable que almacena una cadena
    return mensaje                      # Retorna como salido la variable mensaje

a = int(input(mensaje2()))              # invocamos a la funcion
b = int(input(mensaje2()))
c = int(input(mensaje2()))

print(a,b,c)


# EJEMPLO 3

def numero(x):                          # 1 solo parametro en la funcion
    return print(x)                     # retorna el parametro

numero(6)                               # invocamos a la funcion y le enviamos un argumento al parametro


# EJEMPLO 4

def mi_nombre(nombre, años):            # Mi funcion mi_nombre
    return "Mi nombre es: " + nombre + " y tengo: "+ str(años)  # Retornamos

Nombre = mi_nombre("Yeric", 23)         # Nombre, almacena el valor que devuelve de la funcion mi_nombre
print(Nombre)                           # Imprimimos Nombre