
school_class = {}       # Diccionario

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break

    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        # NO DEFINIMOS LA TUPLA
        school_class[name] += (score,)  # Se crea una Tupla con el valor unico obtenido y lo alojamos en el Diccionario
    else:                               # como su valor de la Clave
        school_class[name] = (score,)

# Funcion sorted(Diccionario, Tupla, Lista) - Ordena de forma Alfabetica
for name in sorted(school_class.keys()):    # Recorre el diccionario por medio de sus claves y retorna sus valores
    adding = 0
    counter = 0
    for score in school_class[name]:    # Recorre nota por Clave del diccionario
        adding += score         # Sumatoria de notas
        counter += 1            # Contador de notas
    print(name, ":", adding / counter)

print(f"\n Diccionario => {school_class}")