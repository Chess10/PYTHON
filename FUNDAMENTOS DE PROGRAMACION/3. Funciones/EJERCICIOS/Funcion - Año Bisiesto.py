def es_año_biciesto(año):
    for i in año:
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            print(i, "Año Biciesto")

        else:
            print(i, "Año No Biciesto")


datos = [1900, 2000, 2016, 1987]
es_año_biciesto(datos)