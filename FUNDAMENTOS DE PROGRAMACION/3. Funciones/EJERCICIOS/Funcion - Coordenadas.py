def coordenadaZ(x, y):
    x = x + 10  #16
    y = y + 15  #22
    return print (x + y)    #38, 40, 42

# programa principal
x = 6
y = 7
for i in range(3):
    z = coordenadaZ(x, y) #invoca a la funcion coodenadasZ
    x = x + 1   #6 + 3 del range = 9
    y = y + 1   #7 + 3 del range = 10

print(x,".", y)
