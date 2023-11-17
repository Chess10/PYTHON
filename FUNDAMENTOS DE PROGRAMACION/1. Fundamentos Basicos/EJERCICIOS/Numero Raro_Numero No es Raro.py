# Tarea
# Dado un número entero, realice las siguientes acciones condicionales:

# Si es impar, imprima Raro
# Si es par y está en el rango inclusivo de 2 a 5, imprima No es raro
# Si es par y está en el rango inclusivo de 6 a 20, imprima Raro
# Si es par y mayor que 20, imprima No es raro

# n tiene que tener una rango de 1 a 100

if __name__ == '__main__':

    while True:
        n = int(input("Ingresa un Numero: ").strip())   # Funcio Strip() = elimína los espacios en blanco al INICIO Y al FINAL
        if n in range(1, 101):
            break

    if n % 2 == 0:
        if n in range(2, 6):
            print("No es Raro")

        if n in range(6, 21):
            print("Raro")
        if n > 20:
            print("No es Raro")
    else:
        print("Raro")