
# El metodo update actualiza

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)     # Actualiza el diccionario d3, asignando un nuevo dato

print(d3)