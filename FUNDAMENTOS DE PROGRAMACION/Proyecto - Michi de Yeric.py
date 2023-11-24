import time
from random import randrange

def Vista_Tablero(board):

    print('+-------'*3+'+')
    print('|       '*3+'|')
    print(f'|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |')
    print('|       '*3+'|')
    print('+-------'*3+'+')
    print('|       '*3+'|')
    print(f'|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |')
    print('|       '*3+'|')
    print('+-------'*3+'+')
    print('|       '*3+'|')
    print(f'|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |')
    print('|       '*3+'|')
    print('+-------'*3+'+')
def Espacios_Vacios(board):

    espacios_disponibles = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                espacios_disponibles.append((i, j))
    return espacios_disponibles
def Posicion_Jugado(board):

    try:
        movi_jugador = int(input("Ingrese su Movimiento (1/9): "))
        if movi_jugador > 0 and movi_jugador < 10:
            dicc = {
                1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2)
                }
            i, j = dicc[movi_jugador]
            espacio = Espacios_Vacios(board)

            if dicc[movi_jugador] in espacio:
                board[i][j] = 'X'
                return board
            else:
                print("La posicion ya esta Ocupada. Ingrese de Nuevo..")
                Posicion_Jugado(board)
        else:
            print("Vuelve a ingresar un numero en el rango de: 1 al 9")
            Posicion_Jugado(board)

    except ValueError:
        print("Vuelve a Intentarlo. Ingrese un Valor Numerico...")
        Posicion_Jugado(board)
def Posicion_Computer(board):

    print("Esperando movimiento de la Computadora..."), time.sleep(2)

    if not any('O' in row for row in board):
        board[1][1] = 'O'
    else:
        lista_espacios_vacios = Espacios_Vacios(board)
        espacio = len(lista_espacios_vacios)

        lugar = randrange(espacio)
        mov_computer = lista_espacios_vacios[lugar]
        i, j = mov_computer

        board[i][j] = 'O'
    Vista_Tablero(board)
    return board
def rectificar(lista, valor):

    for elem in lista:
        if elem != valor:
            return False
    return True
def Ganador_Juego(board):
    a = 0
    while True:
        capturar_valores_fila = board[a:1 + a]
        fila = [elemento for i in capturar_valores_fila for elemento in i]

        capturar_valores_colum = []
        for i in range(3):
            lis_colum = []
            for j in range(3):
                lis_colum.append(tablero[j][i])
            capturar_valores_colum.append(lis_colum)
        capturar_valores_colum = capturar_valores_colum[a:1 + a]
        column = [elemento for i in capturar_valores_colum for elemento in i]

        diagonal = []
        for i in range(3):  diagonal.append(board[i][i])

        diagonal_inversa = []
        for i in range(3):  diagonal_inversa.append(board[i][-1 - i])

        if rectificar(fila, 'X') or rectificar(diagonal, 'X') or rectificar(diagonal_inversa, 'X') \
                or rectificar(column, 'X'):
            return True
        elif rectificar(fila, 'O') or rectificar(diagonal, 'O') or rectificar(diagonal_inversa, 'O') \
                or rectificar(column, 'O'):
            return True
        a += 1
        if a == 3: break

print("\t\n* EL JUEGO DEL GATO *")
tablero = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

while len(Espacios_Vacios(tablero)) != 0:

    Vista_Tablero(tablero)
    if len(Espacios_Vacios(tablero)) != 0:
        Posicion_Computer(tablero)
        if Ganador_Juego(tablero) == True:
            print("GANADOR COMPUTADOR")
            Vista_Tablero(tablero)
            break
    if len(Espacios_Vacios(tablero)) != 0:
        Posicion_Jugado(tablero)
        if Ganador_Juego(tablero) == True:
            print("TU GANASTE")
            Vista_Tablero(tablero)
            break
    else:
        print("No hay espacios Disponibles")
        print("No hay ganador")
        print("El tablero final es: ")
        Vista_Tablero(tablero)
        break

