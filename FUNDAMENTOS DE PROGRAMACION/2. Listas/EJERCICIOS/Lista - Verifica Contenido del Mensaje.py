
respuesta = "  SIIIIUUUU   "
mensaje = respuesta.strip().upper()
lista = ["SI", "NO"]

for men in lista:               # men, recorre cada elemento de la Lista["SI", "NO"]
    if men in mensaje:          # men = ["SI", "NO"], recorre si esta en el contenido del mensaje ["SIIIIUUUU"]
        print("CORRECTO")       # men ["SI"], si esta en el contenido del mensaje con las 2 letras iniciales