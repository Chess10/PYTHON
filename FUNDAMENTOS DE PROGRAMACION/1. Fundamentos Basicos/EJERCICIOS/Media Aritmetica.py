print("\nCALCULO DE LA MEDIA ARITMETICA")

lis_num = []

print ("Ingrese los valores, (ingrese un numero negativo para cerrar)")
while True:    
	try: 
		num = float(input("-> "))
		if num >= 0:
			lis_num.append(num)				
		else:
			break
	except ValueError:
		print ("Error, ingrese un numero")
		continue

n_valores = len(lis_num)
suma_valores = sum(lis_num)

print (f"Media Aritmetica es: ")
print (f"Valores ingresado: {lis_num} = {suma_valores}")
print (f"Cantidad de Valores ingresados = {n_valores}")
print (f"El calculo es: {suma_valores} / {n_valores} = {suma_valores/n_valores}" )
