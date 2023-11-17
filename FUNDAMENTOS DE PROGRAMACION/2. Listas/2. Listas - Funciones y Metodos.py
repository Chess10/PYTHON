# FUNCION
    # resultado = funcion(argumento)
    # Una función no pertenece a ningún dato: obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado.
    # La función toma un argumento, hace algo y devuelve un resultado.

numbers = [111, 7, 2, 1]
print(len(numbers))         # funcion len()
print(numbers)


# METODOS
    # resultado = dato.metodo(argumento)
    # Un método es un tipo específico de función: se comporta como una función y se parece a una función,
    # pero difiere en la forma en que actúa y en su estilo de invocación.
    # pero puede hacer algo más: puede cambiar el estado interno de los datos a partir de los cuales se ha invocado.

numbers.append(4)           # metodo append()
print(len(numbers))
print(numbers)

numbers.insert(0, 222)
print(len(numbers))
print(numbers)