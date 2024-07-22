# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    home_town = {
        'city': 'Tamuning',
        'state': 'Guam',
        'population': 20000
    }

    home_town_message = (f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}.")

    return(home_town_message)

print('Exercise 4:', hometown_info())