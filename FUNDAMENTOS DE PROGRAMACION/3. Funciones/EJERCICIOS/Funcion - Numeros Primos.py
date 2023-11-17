def is_prime(num):  # 7
    diviso = 0

    for a in range(1, num + 1):
        if num % a == 0:
            diviso += 1
    if diviso > 2:
        return False
    else:
        return True

while True:
    dato = int(input("Ingrese el rango para evaluar los numeros primos:  "))
    if(dato > 0):
        break

for i in range(1, dato):
    if is_prime(i + 1):
        print(i + 1, end=" ")
