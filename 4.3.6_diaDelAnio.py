def is_year_leap(year):
    if year%100 == 0:
        if year%400 == 0:
            return True
        else:
            return False
    elif year%4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    days_for_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month > 0 and month <= 12:
        if month == 2:
            if is_year_leap(year):
                return 29
            else:
                return 28
        else:
            return days_for_months[month - 1]
    else:
        return None

def day_of_year(year, month, day):
    sum = 0
    
    if month > 0 and month <= 12:
        if day > 0 and days_in_month(year, month) >= day:
            for i in range(1, month):
                sum += days_in_month(year, i)
            sum += day
            return sum
        else:
            return None
    else:
        return None


while True:
    try:
        yr = int(input("Ingrese un año: "))
        mo = int(input("Ingrese un mes: "))
        day = int(input("Ingrese un día: "))
        result = day_of_year(yr, mo, day)
        if result == None:
            print("Error. Uno de los datos ingresados no es válido.")
        else:
            print("Día del año: ", result)
        salir = input("\n¿Desea salir? Escriba \"si\"\n")
        if salir == "si":
            break

    except(ValueError):
        print("Error. Ingrese un número entero.")