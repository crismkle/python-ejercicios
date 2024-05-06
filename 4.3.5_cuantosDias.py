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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
print("Ejemplos")
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    result = days_in_month(yr, mo)
    print("El mes", mo ,"en el año", yr, "tiene:", result, "días")

print("\nAhora te toca a vos. Para terminar, escribe \"salir\"")
while True:
    try:
        yr = input("Ingrese un año: ")
        if yr == "salir":
            break
        mo = input("Ingrese un mes: ")
        if mo == "salir":
            break
        yr = int(yr)        
        mo = int(mo)
        result = days_in_month(yr, mo)
        print("El mes", mo ,"en el año", yr, "tiene:", result, "días\n")
    except(ValueError):
        print("Error. Ingrese un número entero.")