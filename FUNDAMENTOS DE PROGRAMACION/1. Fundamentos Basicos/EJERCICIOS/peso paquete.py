# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa
# de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido
# y calcule el peso total del paquete que será enviado.

peso_payaso = 112
peso_muñeca = 75

num_payaso = int(input("Ingrese el numero de Payaso: "))
num_muñeca = int(input("Ingrese el numero de muñeca: "))

peso_total_payaso = peso_payaso * num_payaso
peso_total_muñeca = peso_muñeca * num_muñeca

peso_total = peso_total_payaso + peso_total_muñeca

print("\nNumero de Payasos vendidos es: ", num_payaso)
print("Numero de Muñecas vendidos es: ", num_muñeca)

print("Peso total del paquete es "+ str(peso_total) + "g")

