class Restaurant():
    """Class that model a restaurant with name an cuisine type"""
    def __init__(self, restaurant_name, cuisine_type):
        """"Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the attributes of the restaurant"""
        print("Restaurant name is: " + self.restaurant_name)
        print("Cuisine type is: " + self.cuisine_type)

    def set_number_served(self):
        """Set the number of customers"""
        self.number_served = input("Set a number for customers server")

    def increment_number_served(self):
        """Increase the customers served counter by 1"""
        self.number_served += 1

class User():
    """Class that models an user"""
    def __init__(self, first_name, last_name, age, height):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
    
    def describe_user(self):
        print("Summary information\n")
        print(self.first_name + "" + self.last_name + "" + self.age + "" + self.height + "")

    def greet_user(self):
        print("Hello user: " + self.first_name)
    
restaurant = Restaurant("Crazy Chicken", "Fried Chicken")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.increment_number_served()
print(restaurant.number_served)

