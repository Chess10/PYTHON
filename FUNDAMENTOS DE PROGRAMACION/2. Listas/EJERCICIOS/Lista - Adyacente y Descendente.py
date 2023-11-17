# ORDENAMIENTO DE UNA LISTA DE MAYOR A MENOR - MECANICO
Mi_lista = [8, 10, 6, 2, 4]  # lista a ordenar
Intercambio = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while Intercambio:  # Se acitva de bucle cada vez que swapped es verdadero
    Intercambio = False  # no hay intercambios hasta ahora
    print(Intercambio)
    for i in range(len(Mi_lista) - 1):
        print(i)
        if Mi_lista[i] > Mi_lista[i + 1]:
            Intercambio = True  # ¡ocurrió el intercambio!
            print(Intercambio)
            Mi_lista[i], Mi_lista[i + 1] = Mi_lista[i + 1], Mi_lista[i]
            print(Mi_lista[i], Mi_lista[i + 1], "\n")
        print("\n")

print(Mi_lista)

# ORDENAMIENTO DE UNA LISTA CON LA FUNCION sort()

Mi_lista2 = [2,0,7,1,9,43,30,23,12,6]

Mi_lista2.sort()

print(Mi_lista2)