# Este codigo ha sido generado por el modulo psexport 20180125-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print("contraseña")
	contrasena = str()
	cont = int()
	cont = 0
	aciertos = False
	while True:# no hay 'repetir' en python
		print("INGRESE LA CONTRASEÑA: ")
		contrasena = input()
		if (contrasena=="continental"):
			print("CLAVE CORRECTA, BIENVENIDO")
			cont = 1
			aciertos = True
		else:
			print("CLAVE INCORRECTA, INTENTA DE NUEVO")
			cont = cont+1
		if (cont==3 or aciertos==True): break

