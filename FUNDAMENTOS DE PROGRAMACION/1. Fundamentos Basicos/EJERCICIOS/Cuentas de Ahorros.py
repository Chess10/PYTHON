# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
# Redondear cada cantidad a dos decimales.

# Pedir al usuario que ingrese la cantidad de dinero inicial
monto_inicial = float(input("Ingrese la cantidad de dinero inicial en la cuenta de ahorros: "))

# Tasa de interés anual del 4%
tasa_interes = 0.04

# Calcular los ahorros después de 1 año
ahorros_1 = monto_inicial * (1 + tasa_interes)

# Calcular los ahorros después de 2 años
ahorros_2 = ahorros_1 * (1 + tasa_interes)

# Calcular los ahorros después de 3 años
ahorros_3 = ahorros_2 * (1 + tasa_interes)


# TIPOS DE REDONDEO DE UNA CIFRA
# Imprimir los ahorros después de cada año redondeados a dos decimale
print("Ahorros después de 1 año: {:.2f}".format(ahorros_1))     # Aqui solo emprime un argumento
print("Ahorros después de 2 años: ", round(ahorros_2,2))        # Aqui impre 2 argumentos
print("Ahorros después de 3 años: {:.2f}".format(ahorros_3))