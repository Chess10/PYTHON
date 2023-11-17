def Es_triangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b


def Heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def Area_del_Triangulo(a, b, c):
    if not Es_triangulo(a, b, c):
        return None
    return Heron(a, b, c)


print(Area_del_Triangulo(1., 1., 2. ** .5))