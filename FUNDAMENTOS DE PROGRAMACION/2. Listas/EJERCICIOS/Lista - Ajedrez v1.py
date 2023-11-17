# AJEDREZ CON LISTA

ESPACIO = ' '
PEON = 'PEON'
CABALLOS = 'CABALLOS'
TORRE = 'TORRE'
ALFIN = 'ALFIN'
REY = 'REY'
REINA = 'REINA'

tablero_Ajedrez = []

tablero_Ajedrez = [[ESPACIO for i in range(8)] for j in range(8)]

# Ingresamos las Torres
tablero_Ajedrez[0][0] = TORRE
tablero_Ajedrez[0][7] = TORRE
tablero_Ajedrez[7][0] = TORRE
tablero_Ajedrez[7][7] = TORRE

# Ingresamos los Alfin
tablero_Ajedrez[0][2] = ALFIN
tablero_Ajedrez[0][5] = ALFIN
tablero_Ajedrez[7][2] = ALFIN
tablero_Ajedrez[7][5] = ALFIN

# Ingresamos los Caballos
tablero_Ajedrez[0][1] = CABALLOS
tablero_Ajedrez[0][6] = CABALLOS
tablero_Ajedrez[7][1] = CABALLOS
tablero_Ajedrez[7][6] = CABALLOS

# Ingresamos los Reyes
tablero_Ajedrez[0][4] = REY
tablero_Ajedrez[7][4] = REY

# Ingresamos las Reinas
tablero_Ajedrez[0][3] = REINA
tablero_Ajedrez[7][3] = REINA

# Ingresamos los Peones
tablero_Ajedrez[1][0] = PEON
tablero_Ajedrez[1][1] = PEON
tablero_Ajedrez[1][2] = PEON
tablero_Ajedrez[1][3] = PEON
tablero_Ajedrez[1][4] = PEON
tablero_Ajedrez[1][5] = PEON
tablero_Ajedrez[1][6] = PEON
tablero_Ajedrez[1][7] = PEON

tablero_Ajedrez[6][0] = PEON
tablero_Ajedrez[6][1] = PEON
tablero_Ajedrez[6][2] = PEON
tablero_Ajedrez[6][3] = PEON
tablero_Ajedrez[6][4] = PEON
tablero_Ajedrez[6][5] = PEON
tablero_Ajedrez[6][6] = PEON
tablero_Ajedrez[6][7] = PEON

# JUGAR

print(tablero_Ajedrez)
