
#  ARGUEMENTOS DE PALABRAS CLAVES

    # Son mecanismos de pasar de un argumento a otro.

    # Palabras Claves = end=" "
    # Palabras Claves = sep=" "

#__________________________________________________________________________________________________________________________________

# end=" " = esta palabra clave que atrae a los argumentos de una linea superior a su linea invocada.
            # Es decir 2 oraciones en diferentes lineas pueden ser mostradas en una sola linea.

print("\nPALABRA CLAVE =>", 'end=""')

    # Ejemplo 1

print ("\n\t1.", 'end=""' )
print ("\n\tHOLA, SOY PROGRAMADOR", end="")     # Dentro de la comillas del 'end' permite ingresar una cadena y juntan con el argumento
print (". Y TÚ?")                             # siguiente.

    # Ejemplo 2

print("\n\t2.", 'end=" "')
print("\n\tMI NOMBRE ES:", end=" ")
print("YERIC")

    # Ejemplo 3

print("\n\t3.", 'end="LUIS"')
print("\n\tHOLA, SOY YERIC", end=" LUIS")
print(" FLORES LAPA")


#__________________________________________________________________________________________________________________________________


# sep=" " = (SEPARADOR) esta es una palabra clave que reemplaza los espacios entre argumentos por un caracter definido dentro del "".

print("\nPALABRA CLAVE =>", 'sep=""')

    # EJEMPLO 1
print("\n\t1.", 'sep=""')
print("\n\t5","+","6","=","10", sep="")     # Dentro de las comillas del 'sep=""' puedes ingresar caracteres que reemplacen a los
                                            # espacion vacios brindados por las comas o como tambien eliminar los espacios sin
                                            # ingresar ninguna cada al 'sep=""'

    # EJEMPLO 2
print("\n\t2.", 'sep="+"')
print("\n\t5", "15", sep=" + ", end=" = ")
print("20")

