def liters_100km_to_miles_gallon(liters):
    miles = 100 / 1.609344
    gallon = liters / 3.785411784
    return miles / gallon
    

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    km = miles * 1.609344
    return 100 * liters / km
    
print("\nEjemplos de conversiones de litros por cada 100 km a millas por galón, y viceversa.\n")
print("3,9 litros por cada 100 km son:", round(liters_100km_to_miles_gallon(3.9), 2), "millas por galón.\n")
print("7,5 litros por cada 100 km son:", round(liters_100km_to_miles_gallon(7.5), 2), "millas por galón.\n")
print("10 litros por cada 100 km son:", round(liters_100km_to_miles_gallon(10.), 2), "millas por galón.\n")
print("60,3 millas por galón son:", round(miles_gallon_to_liters_100km(60.3), 2), "litros por cada 100 km.\n")
print("31,4 millas por galón son:", round(miles_gallon_to_liters_100km(31.4), 2), "litros por cada 100 km.\n")
print("23,5 millas por galón son:", round(miles_gallon_to_liters_100km(23.5), 2), "litros por cada 100 km.\n")