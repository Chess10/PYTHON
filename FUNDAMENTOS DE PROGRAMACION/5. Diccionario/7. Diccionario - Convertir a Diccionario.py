
# Funcion dict(tupla/lista), permite convertir una lista o una tupla a un diccionario

# Los Valores de las Claves seran anidadas a la derecha y separadas entre parentesis o corchetes.

colors = (("verde", "#008000"), ("azul", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)


nombre = [["Yeric", "Luis"], ["Flores", "Lapa"]]

nombre_diccionario = dict(nombre)
print(nombre_diccionario)