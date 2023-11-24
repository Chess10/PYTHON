import getpass
import os
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable
# sin tener en cuenta mayúsculas y minúsculas.

def clear_screen():
    if os.name == 'nt':  # Verifica si el sistema es Windows
        os.system('cls')  # Utiliza 'cls' en Windows para borrar la pantalla
    else:
        os.system('clear')  # Utiliza 'clear' en sistemas tipo Unix para borrar la pantalla

def usuario_existe(user, lista_usuarios):
    UserExits = False
    if user in lista_usuarios.keys():
        UserExits = True
        return UserExits
    return UserExits
    
def registrar_cuenta(lista_usuarios):
    clear_screen()
    print ("\t== BIENVENIDO ==")
    print ("REGISTRE SU CUENTA")
    print("\n¿Desea crear un usuario o desea obtener el usuario del sistema?")
    print("Si, para crear ")
    print("No, para obtener usuario") 

    while True:
        obtener_user = input("Si  o No: ")
        if obtener_user.capitalize() == "No":
            crear_user = False
            break
        elif obtener_user.capitalize() == "Si":
            crear_user = True
            break
        else:
            print("Ingrese un valor correcto....")

    clear_screen()
    print("\nUSUARIO")

    if crear_user == False:
        username = getpass.getuser()
        user_exists = usuario_existe(username, lista_usuarios)
        if user_exists == True:
            print("\nEl usuario de este sistema ya existe")
            print("Cree un nombre de usuario.\n")
            crear_user = True
        else:
            print(f"\nSu nombre de usuario es: {username}")

    if crear_user == True:
        while True:
            username = str(input("Ingrese nombre de usuario: "))  
            user_exists = usuario_existe(username, lista_usuarios)
            if user_exists == True:
                print("El usuario ya existe, ingrese nuevamente")
                continue
            else:
                break

    while True:
        password = input("\nIngrese su password: ")   # Creamos y confirmamos
        password2 = input("Confirme su password: ")
        usuario = {}
        if password == password2:            
            usuario[username] = password
            lista_usuarios.update(usuario)
            archivo = open("Usuarios.txt", "a")
            archivo.write(str(usuario)+"\n")
            archivo.close()
            break
        else:
            print("Las contraseñas no coinciden, ingrese nuevamente....")
            continue 

    clear_screen()
    print(" ** SU CUENTA SE CREO CORRECTAMENTE **")

    while True:
        print("\n¿Desea salir?")
        salir = input("Si o No: ")
        if salir.capitalize() == "Si":    
            return lista_usuarios
        elif salir.capitalize() == "No":
            registrar_cuenta(lista_usuarios)
        else:
            print("Ingrese un valor correcto....")


list_users = {}
registrar_cuenta(list_users)

print(list_users)
input()