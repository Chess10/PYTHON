# Crear tu propia Lista emulando Do While. Hallar la suma de todos los valores de tu lista

lista = []
total = 0

while True:
    valor = int(input("Ingrese valores para tu lista, presiona 0 para terminar: "))
    if valor != 0:
        lista.append(valor)
        total += lista
    else:
        break

for i in range(len(lista)):
    total += lista[i]

print("\n")
print("La Longitud  de tu Lista: ", len(lista))
print("Mi Lista: ", lista)
print("La suma de todos los valores de tu Lista: ", total)