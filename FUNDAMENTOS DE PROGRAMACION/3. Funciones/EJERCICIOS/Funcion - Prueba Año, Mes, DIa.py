def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
        return None

    # Definir la cantidad de días en cada mes
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar si el año es bisiesto y ajustar febrero
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_per_month[1] = 29

    days = days_per_month[month - 1]
    if days == day:
        return "Es correcto el mes y el dia"
    else:
        return "Los dias del mes no son correctos para el año"


print(day_of_year(2000, 2, 35))
