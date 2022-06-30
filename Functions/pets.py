def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My "+ animal_type + "'s name is " + pet_name.title())

def make_shirt(size="L", text_msg="I love python"):
    """Display information about the size and text that should be 
    printed on the shirt"""
    print("Shirt's size is: " + size.title() + "and the text i: " + text_msg.title())

def describe_city(city, country="Mexico"):
    """Display simple information of a city"""
    print(city + " is in " + country.title())

# describe_pet("hamster", "harry")

# This function call uses just 1 parameter to use default values
describe_pet(pet_name='willie') 

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# Positional arguments call
make_shirt("XXL", "I love python")
# Call with keyword arguments
make_shirt(size="XXL", text_msg="I love python")

describe_city("Durango")
describe_city("Reykjavik", "iceland")
describe_city("Los Angeles", "USA")


