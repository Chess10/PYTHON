import time
from random import randrange

def display_board(board):
# La función acepta un parámetro el cual contiene el estado actual del board
# y lo imprime en la consola
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
def enter_move(board):
# La función acepta el estado actual del board, pide al usuario ingresar su posición en el board,
# chequea el input si es número y actualiza el board de acuerdo a lo ingresado por el usuario
    try:
        ingreso=input('Ingresa número entero entre 1 a 9: ')
        if ingreso=='q':
            return 'q'
        numero_ingresado=int(ingreso)
        if numero_ingresado>0 and numero_ingresado<10:
            diccionario={1:[0,0],2:[0,1],3:[0,2],
                 4:[1,0],5:[1,1],6:[1,2],
                 7:[2,0],8:[2,1],9:[2,2]}
            existe=False
            for row in board:
                if numero_ingresado in row:
                    existe=True
                    break
            if existe==True:
                i,j=diccionario[numero_ingresado]
                board[i][j]='O'
                return board
            else:
                print('Lugar no esta disponible para ingresar. Ingresa otro')
                return enter_move(board)
        else:
            print('Has ingresado un número no el rango de 1 a 9, cotas inclusive')
            return enter_move(board)

    except ValueError:
        print('Has ingresado un caracter no numérico')
        return enter_move(board)
def make_list_of_free_fields(board):
# La función recorre y busca en el board los espacios libres y construye una lista,
# la lista consiste de tuplas, mientras que cada tupla es un par de números de fila y columna
    lista=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]!='O' and board[i][j]!='X':
                lista.append((i,j))
    return lista
def victory_for(board, sign):
# La función analiza el board para determinar si el jugador que
# juega con 'X' o con 'O' ha ganado el juego
    ganador=None
    if sign=='X':
        ganador='Computador'
    if sign=='O':
        ganador='Tú(humano)'
    ganar=[[sign,sign,sign]]
    board_traspuesta=[[board[j][i] for j in range(3)] for i in range(3)]
    board_diagonal=[[ board[i][i] for i in range(3)],[board[i][2-i] for i in range(3)]]
    for i in board:
        if i in ganar:
            return f'El ganador es: {ganador}'
    for i in board_traspuesta:
        if i in ganar:
            return f'El ganador es: {ganador}'
    for i in board_diagonal:
        if i in ganar:
            return f'El ganador es: {ganador}'
    if len(make_list_of_free_fields(board))==0:
        return 'No hay más espacios disponibles. Juego Terminado no ha ganado nadie'
    else:
        return False
def draw_move(board):
# La función ejecuta el movimiento del computador y actualiza el board
    if board==[[1,2,3],[4,5,6],[7,8,9]]:
        return [[1,2,3],[4,'X',6],[7,8,9]]
    else:
        lista_campos_vacios=make_list_of_free_fields(board)
        tamaño=len(lista_campos_vacios)
        try:
            print("Jugando la Computadora, espere...")
            time.sleep(3)

            lugar = randrange(tamaño)
            posicion=lista_campos_vacios[lugar]
            i,j=posicion
            board[i][j]='X'
            return board
        except ValueError:
            return board

board=[[1,2,3],[4,5,6],[7,8,9]]
while True:
    if board==[[1,2,3],[4,5,6],[7,8,9]]:
        print('Ha comenzado el juego del Gato')
        print("El computador usa la marca 'X' y el usuario(tu) usas la marca 'O'")
        print('Ingresa q para salir en cualquier momento del juego')
    board=draw_move(board)
    display_board(board)
    time.sleep(0)
    result=victory_for(board,'X')
    if result:
        print(result)
        input()
        break

    board=enter_move(board)
    if board=='q':
        print('Has salido del programa')
        break
    result1=victory_for(board,'O')
    if result1:
        print(result1)
        print('El Tablero Final es el siguiente:')
        display_board(board)
        input()
        break
    display_board(board)