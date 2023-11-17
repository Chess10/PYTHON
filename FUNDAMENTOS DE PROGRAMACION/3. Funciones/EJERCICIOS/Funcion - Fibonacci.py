def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    la_suma = 0
    for i in range(3, n + 1):
        la_suma = elem_1 + elem_2       # Suma los elementos anteriores
        elem_1, elem_2 = elem_2, la_suma       # Se cambias los valores para el sigueinte numero
    return la_suma


for n in range(1, 10):  # probando
    print(n, "->", fibonacci(n))
