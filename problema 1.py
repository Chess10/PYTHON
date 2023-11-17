# Este codigo ha sido generado por el modulo psexport 20180125-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print("media aritmetica")
	n = int()
	suma = int()
	cont = int()
	print("ingrese un numero (-1 para terminar): ")
	n = int(input())
	suma = 0
	suma = 1
	while n!=-1:
		suma = suma+n
		cont = cont+1
		n = int(input())
	print("La media aritmetica de los numeros es: ",suma/(cont-1))

