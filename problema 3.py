# Este codigo ha sido generado por el modulo psexport 20180125-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	print("LA RAIZ CUADRADA")
	n = int()
	r = int()
	n = int(input())
	while True:# no hay 'repetir' en python
		if n<0:
			print("INGRESE OTRO NUMERO")
		if n>0: break
	print("LA RAIZ CUADRADA DE ",n," es ",sqrt(n))

