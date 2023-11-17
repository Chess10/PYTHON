# EL metodo copy(), permite copiar el contenido del diccionario a otro

diccionario = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

copy_dictionary = diccionario.copy()        # Copiamos
diccionario.clear()                         # Eliminamos
print(copy_dictionary)
print(diccionario)