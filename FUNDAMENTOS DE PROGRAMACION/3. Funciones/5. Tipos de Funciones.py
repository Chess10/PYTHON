# FUNCIONES DEFINIDAS
print ("\n\t FUNCION DEFINIDA")
# EJEMPLO 1
def raiz_cubica(raiz):  # def = Define la creación de 3. Funciones
    result = raiz ** 1 / 3
    return print(result)

raiz_cubica(5)


# _____________________________________________________________________________________

# FUNCIONES RECURSIVAS
print ("\n\t FUNCION RECURSIVA")
# Son funciones que se llaman asi misma dentro de su cuerpo

# EJEMPLO 1
def funci_recursiva(num):
    if num > 0:
        print(num)
        funci_recursiva(num - 1)

funci_recursiva(3)


# EJEMPLO 2
# Implementación recursiva de la función factorial.
def factorial(n):
    if n == 1:    # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24


# _____________________________________________________________________________________

# FUNCIONES LAMBDA
print ("\n\t FUNCION LAMBDA")
# Son funciones más resumida realizadas en una sola línea de código

result = lambda a, b, c: (a ** b) + c  # La función Lambda ocupa menos espacio de memoria
print(result(1, 2, 4))  # a,b,c: = son los parámetros de la función Lambda
# : (a**b) + c = es la operación que se vá realizar dentro de la función
