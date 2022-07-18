def locations(city, country, population=0):
    if population:
        location =  city + ', ' + country + ' - ' + str(population)
    else:
        location =  city + ', ' + country 
    return location.title()

