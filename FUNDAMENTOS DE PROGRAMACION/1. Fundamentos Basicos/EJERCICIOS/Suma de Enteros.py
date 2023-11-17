# Escribir un programa que lea un entero positivo, 'n',
# introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 'n'.
# La suma de los 'n' primeros enteros positivos puede ser calculada de la siguiente forma:

suma = 0

while True:
    n = int(input("Ingrese un numero entero positivo: "))
    if n > 0:
        break


for var in range(1, n+1):
    suma = var + suma

suma_2 = (n * (n+1))/2
print("La suma de numeros positivos es: ", suma, ", ", suma_2)


