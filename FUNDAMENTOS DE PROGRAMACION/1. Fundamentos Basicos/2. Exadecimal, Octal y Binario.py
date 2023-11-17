
    # Octal       =   0    1    2    3  -  4    5    6    7                                                 = 8 dígitos
    # Hexadecimal =   0    1    2    3  -  4    5    6    7  -  8    9    A    B   -  C    D     E     F    = 16 dígitos
    # Binario     =   1    1    1    1  -  1    1    1    1  -  1    1    1    1   -  1    1     1     1    = 16 dígitos
    # Decimal     =   1    2    4    8  -  16   32   64  128 - 256  512  1024 2048 - 4096 8192 16384 32768  = 16 dígitos


# NÚMERO OCTAL

    # El sistema octal usa 8 dígitos (0, 1, 2, 3, 4, 5, 6, 7) y cada dígito tiene el mismo valor que en el sistema de
    # numeración decimal.

    # EJEMPLO

    # Numero Octal (0o234) a decimal
        # Cantidad numeros (n-1)    2 1 0  = de Derecha a Izquierda
        # Numero Hexadecimal        2 3 4  = de Derecha a Izquierda

    # En Python se representa con un: 'o'

    # 0o234 = 4(8)^0 + 3(8)^1 + 2(8)^2
    # 0o234 = 4(1) + 3(8) + 2(64)
    # 0o234 = 4 + 24 + 128
    # 0o234 = 156 en decimal

print("\n\t OCTAL" )
# De Octal a Decimal
print("0o234 = ", 0o234)

# De Decimal a Octal
print ("156 = ", oct(156))

#__________________________________________________________________________________________________________________________________


# NÚMERO HEXADECIMAL

    # El sistema hexadecimal usa 16 dígitos (0, 1, 2, 3,..., 9, A, B, C, D, E, F) y cada dígito tiene el mismo valor que en el
    # sistema de numeración decimal.

    # EJEMPLO
    # NUmero hexadecimal (0x2345) a decimal
                # Cantidad numeros (n-1)    3 2 1 0  = de Derecha a Izquierda
                # Numero Hexadecimal        2 3 4 5  = de Derecha a Izquierda

    # En Python se representa con: 'X'
    # 0x2345 = 5(16)^0 + 4(16)^1 + 3(16)^2 + 2(16)^3
    # 0x2345 = 5(1) + 4(16) + 3(256) + 2(4096)
    # 0x2345 = 5 + 64 + 768 + 8192
    # 0x2345 = 9029 en decimal


print("\n\t HEXADEIMAL" )
# De Hexadecimal a Decimal
print("\n0x2345 = " , 0x2345)

# De Decimal a Hexadecimal
print("9029 = ",hex(9029))


#__________________________________________________________________________________________________________________________________


# NUMERO BINARIO

    # Es la representacion de 0 y 1 de un numero Decimal

    # 1 representa Encendido. Es decir, son pulsos electricos por el procesador.
    # 0 representa Apagado. Es decir, no produce pulsos electricos por el procesador.

    # Octal       =   0    1    2    3  -  4    5    6    7                                                 = 8
    # Hexadecimal =   0    1    2    3  -  4    5    6    7  -  8    9    A    B   -  C    D     E     F    = 16
    # Binario     =   1    1    1    1  -  1    1    1    1  -  1    1    1    1   -  1    1     1     1    = 16
    # Decimal     =   1    2    4    8  -  16   32   64  128 - 256  512  1024 2048 - 4096 8192 16384 32768  = 16


    # EJEMPLOS
    # De 255 a Binario es:
    # 255 = 11111111
    # 256 = 000000001
    # 15  = 11110000


print( "\n\tBINARIO")
# De Binario a Decimal
print("\n255 = ",bin(255))
print("15 = ", bin(15))

# De Decimal a Binario
print("11111111 = ",0b11111111)