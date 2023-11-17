def days_in_month(year, month):
    # Validar si el año y el mes son válidos
    if year < 1 or month < 1 or month > 12:
        return None

    # Definir la cantidad de días en cada mes
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar si el año es bisiesto y ajustar febrero
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_per_month[1] = 29

    # Devolver el número de días del mes dado
    return days_per_month[month - 1]

# Definir los meses
nom_month = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
            "Octubre", "Noviembre", "Diciembre"]

# Prueba de la función con los valores de ejemplo
year = int(input("Ingrese Año: "))
months = int(input("Ingrese el Mes (1-12): "))
days = int(input("Ingrese el numero de Dia del Mes: "))

print("\t\n RESULTADO")
print(f"Año = {year} Mes = {months} Prueba ", end="-> ")
result = days_in_month(year, months)
month = result
if result == days:
    print("CORRECTO")
    print(F"En el año {year} el mes {nom_month[months-1]} tiene {month}")
else:
    print("Fallido")
    print(F"En el año {year} el mes {nom_month[months-1]} tiene {month}")
