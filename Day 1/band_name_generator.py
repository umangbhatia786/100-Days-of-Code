#Go to: https://replit.com/@appbrewery/band-name-generator-start?v=1

print('Welcome to the Band Name Generator.')

city = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")

band_name = "{0} {1}".format(city, pet_name)
print('Your band name could be {0}'.format(band_name))