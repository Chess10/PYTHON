# Son operacion que se hacen dentro de una lista, verificando sus condiciones para ser evaludas y darle el dato a la lista

# Se evalua de Derecha a Izquierda
# Primero: Se evalua las condiciones, siempre y cuando hay un 'if' o 'else'
# Segundo: Se evalua los bucles, siempre y cuando hay un 'for' o 'while'
# Tercero: Se evalua el Dato final de la lista, ya sea una operacion aritmetica o un dato simpe

# row = [ x + 1 for x in range(8)]
        # x + 1  = son los datos que se utilizarán para completar la lista
        # for x in range(8)   = La cláusula que especifica cuántas veces se producen los datos dentro de la lista

        # x => 0 - 8
        # Luego: x + 1 => 1 - 8

row = [ x + 1 for x in range(8)]
print(row)



# EJEMPLO 2
squares = [x ** 2 for x in range(10)]       # x = 0 - (10-1)
twos = [2 ** i for i in range(8)]           # i = 0 - (8-1)
odds = [x for x in squares if x % 2 != 0 ]  # x = al rango de valores de squares, toma sus valores anteriores, con su condicion especifica
print(squares)
print(twos)
print(odds)