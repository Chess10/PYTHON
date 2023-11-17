
# DIVISION DE 3 EXPRECION ARITMETICA

x = float(input("Ingresa el valor para x: "))
cont = 0
y = x + (1 / x)

while True:
    y = x + (1 / y)
    cont += 1

    if cont == 2:
        y = (1 / y)
        break

print("y =", y)