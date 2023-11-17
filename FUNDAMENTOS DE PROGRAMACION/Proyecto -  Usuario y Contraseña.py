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
def fin_sesion():
    return 'GRACIAS POR INGRESAR, VUELVA PRONTO..'

def sistema():
    return 'holaaaaaa'
def ingresar_contraseña_enmascarada():
    contra = []
    while True:                             # stream, controla la secuencia de entrada/salida que se utiliza para solicitar la contraseña
        caracter = getpass.getpass(prompt='', stream=None)  # Lee un carácter de la contraseña
        if not caracter:  # Si se presiona Enter, termina la entrada
            break
        contra.append(caracter)
        print('*', end='', flush=True)  # Muestra un asterisco en lugar del carácter
    return ''.join(contra)          # flush, permite controlar la salida si se debe vaciar o no
def login():
    users = input("User: " )
    contra = input("Password: " + ingresar_contraseña_enmascarada())

    if usuario == user and contrasena == contra:
        return 'Inicio de Sesion'
    else:
        if usuario != users:
            print("El Usuario es Incorrecto: ")
        elif contrasena != contra:
            print("La contraseña es Incorrecta: ")
        print("Ingresa de nuevo")
        login()
def inicio_sesion():
    while True:
        continuar = input("Deseas Iniciar Sesion (S/N): ").upper()
        continuar = list(continuar)
        continuar = continuar[0]
        continuar = ''.join(continuar)

        if continuar == 'S':
            # Llama a la función para borrar la pantalla
            clear_screen()
            login()
            print(login())
            sistema()
            return print(sistema())

        elif continuar == 'N':
            return print(fin_sesion())

        else:
            print("Vuelve a ingresar un valor correcto")
            inicio_sesion()


usuario = getpass.getuser()
user = os.getlogin()

print(f"Su Usuario es: {usuario}")
contrasena = getpass.getpass("Registre tu contraseña: ")
print(contrasena)

print("\n\t-- REGISTRADO --")
inicio_sesion()
print("ADIOS")



