# break - ejemplo

print("La instrucción 'break':")
for i in range(1, 6):
    if i == 3:
        break               # HACE QUE SE SALGA DEL BUCLE UNA VEZ FINALIZADO EL if.
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción 'continue':")
for i in range(1, 6):
    if i == 3:
        continue            # HACE QUE SE CONTINUE EL BUCLE UNA VEZ FINALIZADO LA CONDICION if, HASTA FINALIZAR CON EL for.
    print("Dentro del bucle.", i)
print("Fuera del bucle.")