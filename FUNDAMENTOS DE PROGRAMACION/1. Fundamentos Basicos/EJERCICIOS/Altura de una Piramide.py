bloques = int(input("Ingrese el Numero de bloques: "))

altura = 0
capas = 1           # Altura se basa en las capas completas usadas por los bloques, es decir que los capas se incrementa en 1
                    # +     -> capas = 1
                    # **    -> capas + 1 = 2
                    # ***   -> capas + 1 = 3
base = 0

while altura < bloques:         # El altura no puede ser mayor a los bloques, por logica.
    bloques -= capas            # Las capas restan a los bloques, ya que las capas contienen bloques
    altura += 1                 # La altura son las capas completas
    capas += 1
    base += 1
else:
    if bloques != 0:
        base += 1

print("La Base de la piramide es "+ str(base))
print("La altura de la piramide es "+str(altura))