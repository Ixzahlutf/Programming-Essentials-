def liters_100km_to_miles_gallon(liters):
    liter = 3.785411784 # 1 galon = ?liter
    gallon = liters/liter
    meter = 1609.344     # 1 mile = ? meter
    miles = 100*1000/meter
    return miles/gallon
    
def miles_gallon_to_liters_100km(miles):
    liter = 3.785411784 # 1 galon = ?liter
    meter = 1609.344     # 1 mile = ? meter
    km100 = miles*meter*1000/100
    return liter/km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
