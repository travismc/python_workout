# Write a function, get_rainfall, that tracks rainfall in a number of cities. Users of your program will enter the name of a city; if the city name is blank, then the function prints a report (which I’ll describe) before exiting.

# If the city name isn’t blank, then the program should also ask the user how much rain has fallen in that city (typically measured in millimeters). After the user enters the quantity of rain, the program again asks them for a city name, rainfall amount, and so on--until the user presses Enter instead of typing the name of a city.

# When the user enters a blank city name, the program exits--but first, it reports how much total rainfall there was in each city.

def get_rainfall():
    rainfall = {}  # initiates empty dict to hold city, rain amount pairs
    while True:
        city = input('What city? ')
        if not city:
            break

# TODO: change rain input block to .get() so that repeat city entries update value
        rain = input('How much rain? ')
        if not rainfall.get(city):
            rainfall.update({city: float(rain)})

    for k, v in rainfall.items():
        print(f'{k}: {v}')


get_rainfall()
