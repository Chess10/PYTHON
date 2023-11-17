# EJEMPLO 1 - VARIABLE GLOBLA, DEFINIDA FUERA EN LA FUNCION
def mi_funcion():
    return f"El valor es: {var}"

var = 1
print (mi_funcion())


# EJEMPLO 2 - VARIABLE LOCAL, DEFINIDA EN LA FUNCION
def my_funcion():
    vari = 2                        # var1, es una variable diferente ya que cuenta con un valor asignado en la funcion
    return f"El valor es: {vari}"

vari = 1    # var1, es una variable global definida fuera da la funcion
print (my_funcion())
print (vari)


# EJEMPLO 3 - VARIABLES GLOBAL, DEFINIDA EN LA FUNCION
def funcion_global():
    global var2                     # var2, es la misma variable que esta definida fuera de la funcion y si o si es lleva como 'global'
    var2 = 2
    return f"El valor es: {var2}"

var2 = 1
print(funcion_global())
print(var2)