
Precio_Barras_Pan = 3.49
cant_Barras_Pan_Defectuosas = 20

descuento = Precio_Barras_Pan * 0.6
pan_descuento = Precio_Barras_Pan - descuento
Precio_total = cant_Barras_Pan_Defectuosas * pan_descuento

print("Precio de la Barra de Pan: {:}".format(Precio_Barras_Pan))
print("Descuento del 60% por Pan que no es del dia, un total de: {:.2f}".format(pan_descuento))
print("El precio final es de: {:.2f}".format(Precio_total))


