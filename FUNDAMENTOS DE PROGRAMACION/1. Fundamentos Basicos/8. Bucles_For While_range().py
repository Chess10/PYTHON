# For   = Ejecuta un conjuntode Condiciones varias veces
# While = Se ejecuta siempre que la condicion True

for i in range(3):
    print(i, end=" ")  # Salidas: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Salidas: 6, 4, 2

# Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla.
# Usa el esqueleto de abajo:
import time

for i in range(0, 11):          # range(start, stop, slep) = genera una secuencia de números
    if (i % 2 != 0):                # start = inicio        /   stop = final
       print (i)                    # slep = salto de recorrido, por defecto es 1
       time.sleep(1)    # un tiempo de respuesta  

# Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla.
# Usa el esqueleto de abajo:

x = 0
while x < 11:
    if (x % 2 != 0):
        print (x)
    x += 1


# Crea un programa con un bucle for y una sentencia break.
# El programa debe iterar sobre los caracteres en una dirección de correo electrónico,
# salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.
# Usa el esqueleto de abajo:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")


# Crea un programa con un bucle for y una sentencia continue.
# El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x,
# e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:

print("\n")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")



