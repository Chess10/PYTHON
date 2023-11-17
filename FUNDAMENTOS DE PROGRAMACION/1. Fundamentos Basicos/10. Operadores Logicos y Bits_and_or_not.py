print("============================")
print("OPERADORES LOGICOS Y DE BITS")
print("============================\n")

v1 = int(input("Ingrese primer valor: "))
v2 = int(input("Ingrese segundo valor: "))

print("\nOPERADORES LOGICOS")
print("------------------\n")

# Operador Lógico 'Y' CONJUNCIÓN LOGICA, se cumple cuando todas las condiciones son verdaderas
print("Operador Logico 'and' - CONJUNCION ")
print(v1, " > 0 and ", v2, " > 10 \n", v1 > 0 and v2 > 10)
conjuncion = v1 > 0 and v2 > 10
if conjuncion == False:
    print ("Porque uno de las condiciones es falsa, lo que no se cumple con la CONJUNCION\n")
else:
    print("Ambas condiciones son Verdaderas, cumpliendo con la CONJUNCION\n")


# Operador Lógico 'O' DISYUNCIÓN LOGICA, se cumple cuando al menos 1 condicion verdadera
print("Operador Logico 'or' - DISYUNCION")
print(v1, " > 0 or ", v2, " > 10 \n", v1 > 0 or v2 > 10)
disyuncion = v1 > 0 or v2 > 10
if disyuncion == False:
    print("Ambas condiciones son Falsas, lo que no se cumple con la DISYUNCIÓN\n")
else:
    print ("Porque uno de las condiciones es Verdadera, lo que se cumple con la DISYUNCIÓN\n")


# Operador Lógico 'No' NEGACIÓN LOGICA, se cumple
print("Operador Logico 'not' - NEGACION")
print("not ", v1, " == ", v2, "\n", not v1 == v2)
negacion = not v1 == v2
if negacion == True:
    print("La condicion es Verdadera, No es verdad que ", v1, " sea igual a ", v2)
else:
    print("Porque la condicion si es igual, lo que no se cumple con la NEGACION")


print("\nOPERADORES BINARIOS")
print("-------------------\n")

print("Operador Bit '&' CONJUNCION")                    # Operador Bit 'Y' CONJUNCIÓN BINARIA
print(v1, " & ", v2, " = ", v1 & v2)                    # 0 & 0 = 0         0 & 1 = 0
print(bin(v1), " & ", bin(v2), " = ", bin(v1 & v2))     # 1 & 0 = 0         1 & 1 = 1  OJO: El 0 es prioridad

print("\nOperador Bit '|' DISYUNCION")                   # Operador Bit 'O' DISYUNCIÓN BINARIA
print(v1, " | ", v2, " = ", v1 | v2)                     # 0 & 0 = 0         0 & 1 = 1
print(bin(v1), " | ", bin(v2), " = ", bin(v1 | v2))      # 1 & 0 = 1         1 & 1 = 1  OJO: El 1 es prioridad

print("\nOperador Bit '~' NEGACION")                                            # Operador Bit '~' NEGACIÓN BINARIA
print("~", v1, " = ", ~v1, " and ", "~", v2, " = ", ~v2)                        # OJO: NO es la inversa de los bits del número,
print("~", bin(v1), " = ", bin(~v1), " and ", "~", bin(v2), " = ", bin(~v2))    # es la suma de un bit al resultado
                                                                                  # EJEMPLO: 5 = 0101 => ~5 = 0101 + 1
                                                                                  #                   => ~5 = 0110
                                                                                  #                   => ~5 = -6

print("\nOperador Bit '^' EXCLUSION")                   # Operador Bit '^' EXCLUSIÓN BINARIA
print(v1, " ^ ", v2, " = ", v1 ^ v2)                    # 0 & 0 = 0         0 & 1 = 1
print(bin(v1), " ^ ", bin(v2), " = ", bin(v1 ^ v2))     # 1 & 0 = 1         1 & 1 = 0  OJO: si ambos bits son iguales prioriza el 0,
                                                                                #       y si son diferentes prioriza el 1.


print("\nDESPLAZAMIENTO A LA DERECHA")
print("---------------------------\n")
numero = 15                                                     # 15 = 1111
dezplazamiento = 3                                              # >> 3 : CANTIDAD DE BITS QUE SE DESPLAZARAN HACIA LA DERECHA
resultado = numero >> dezplazamiento                            # 1111 >> 3: SE DESPLAZA 3 BITS HACIA LA DERECHA = 0001 = 1
print("numero >> ",dezplazamiento," = ", resultado)
print(bin(numero), ">> ",dezplazamiento," = ", bin(resultado))  # CALCULO: 15 / 2^(3) donde 3 es la cantidad de bits de desplazamiento


print("\nDESPLAZAMIENTO A LA IZQUIERDA")
print("---------------------------\n")
numero = 20                                                     # 20 = 10100
dezplazamiento2 = 4
dezplazamiento = numero << dezplazamiento2                      # << 3 : CANTIDAD DE BITS QUE SE DESPLAZARAN HACIA LA IZQUIERDA
print("numero << ",dezplazamiento2," = ", resultado)            # 10100 << 3: SE DESPLAZA 3 BITS HACIA LA DERECHA = 10100000 = 160
print(bin(numero), "<< ",dezplazamient2," = ", bin(resultado))  # CALCULO: 20 x 2^(3), donde 3 es la cantidad de bits de desplazamiento
