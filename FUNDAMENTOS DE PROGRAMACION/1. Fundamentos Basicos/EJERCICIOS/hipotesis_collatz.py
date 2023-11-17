# Empezamos con un número entero positivo. Lo evaluamos, si el número es par entonces lo dividimos entre 2.
# Si es impar, entonces se multiplica por 3 y se le suma 1. Al resultado lo volvemos a evaluar y
# nuevamente aplicamos las operaciones correspondientes.

n = int(input("Ingrese un numero entero mayor a 0: "))
pasos = 0

while (n > 0 and n != 1):

    if (n % 2 == 0):
        n /= 2
    else:
        n = (3 * n) + 1

    pasos += 1
    print(n)

print("pasos " + str(pasos))