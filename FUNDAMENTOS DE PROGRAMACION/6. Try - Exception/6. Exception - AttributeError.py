# Esta excepción llega, entre otras ocasiones, cuando intentas activar un método que no existe en un elemento
# con el que se está tratando. Por ejemplo:

try:
    short_list = [1]
    short_list.append(2)
    short_list.depend(3)
except:
    print("No es un Metodo correcto")

print(short_list)