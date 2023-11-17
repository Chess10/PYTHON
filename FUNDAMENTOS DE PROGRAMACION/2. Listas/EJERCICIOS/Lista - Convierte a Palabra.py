# CONVERCION DE LISTA A UNIR EN UNA PALABRA

# EJEMPLO 1

Lista = ["H", "o","l","a"]
palabra = ''.join(Lista)        # funcion join(), convierte una lista en palabra, esta esta anidada con ''.
                                # que significa que si contendra un espacio
print(palabra + f"\n{Lista}")

# EJEMPLO 2

Lista2 = ["Hola", "Yeric"]
Oracion = '\n'.join(Lista2)      # ''.join(Lista2), contendra un espacio

print(Oracion + f"\n{Lista2}")

# EJEMPLO 3

Lista3 = ["H", "o","l","a"]
palabra2 = sep="*".join(Lista3[1:])
print(palabra2 + f"\n{Lista3}")