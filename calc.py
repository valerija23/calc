
# konvertē datu mērvienības
def megabit_to_megabyte(megabit):
   result = megabit*8
   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers = 100):
   result = (litres/kilometers)*100
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = (celsius)*9/5+32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result = 0
    for i in range(tail+1):
       result += i
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    return str(grams) + "g"