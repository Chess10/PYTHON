# Encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos.
# Las horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe ser mostrado en la consola.
# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

hora = int(input("Hora de inicio (horas): "))
minu = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

minu += dura

while True:
    if minu > 59:
        hora += 1
        minu -= 60
        if hora > 24:
            hora = 0
            hora += 1
        continue
    break

print (hora,":",minu)