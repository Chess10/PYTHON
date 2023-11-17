# Esta excepción aparece cuando intentas aplicar un dato cuyo tipo no se puede aceptar en el contexto actual.
# Mira el ejemplo:

try:
    my_lista = [4]
    obenet_valor_my_lita = my_lista[0.5]    # Genera el Error

except TypeError:
    print("Para el recorrido de la lista, usamos datos Enteros")