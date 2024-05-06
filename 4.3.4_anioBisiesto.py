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


print("Para terminar, escriba 'salir'")
while True:
    try:
        yr = input("Ingrese un año: ")
        if yr == "salir":
            break
        yr = int(yr)
        print(yr,"->",end=" ")
        result = is_year_leap(yr)
        if result:
            print("Es año bisiesto")
        else:
            print("No es año bisiesto")
    except(ValueError):
            print("Error. Ingrese un número entero.")