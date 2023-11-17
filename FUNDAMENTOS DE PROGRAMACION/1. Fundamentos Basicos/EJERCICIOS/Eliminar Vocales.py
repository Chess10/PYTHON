# Importar el módulo 'time' para usar la función 'sleep'.
import time

Palabra_Usuario = str(input("Ingrese una palabra: "))
Palabra_Usuario = Palabra_Usuario.upper()           # convertira a mayúsculas.


vocales = ['A', 'E', 'I', 'U', 'O']                 # Arreglo de Vocales

# Iterar a través de cada letra en la palabra ingresada por el usuario.
for a in Palabra_Usuario:       # Es decir que, 'a' recorre por la primera letra de la variable 'Palabra_Usuario'
                                # hasta que llegue a la ultima letra, dentro del for lo hace por cada letra.
    if a in vocales:           # Comprobar si la letra actual está en la lista de vocales.
                                    # Dentro de la condicion if sabiendo que encontro una vocal,
        print(" ", end="")          # imprimir un espacio en blanco y continuar con la siguiente letra.

        continue

    # Pausa de 1 segundo antes de imprimir la letra actual.
    time.sleep(1)

    # Imprimir la letra actual sin salto de línea.
    print(a, end="")

print("\n")

# Iterar a través de cada letra en la palabra ingresada por el usuario nuevamente.
for i in Palabra_Usuario:

    print(i, end="")             # Imprimir la letra actual con un retraso de 2 segundos.
    time.sleep(2)




