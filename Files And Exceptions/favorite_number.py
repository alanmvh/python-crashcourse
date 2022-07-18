import json

# Reads the favorite number of an user then saves it into a txt file
try:
    filename = "Files And Exceptions/fav_number.txt"
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
except FileNotFoundError:
    favorite_number = input("Enter your favorite number")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        print("Your favorite number is " + favorite_number)
else:
    print("We remember your favorite number " + favorite_number)
