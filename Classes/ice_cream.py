from restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize IceCreamStant attributes"""
        super().__init__(restaurant_name, cuisine_type)
        """Using special super function to call init method from Restaurant's parent class"""
        self.flavors = ['Spicy', 'sweet', 'Salty']
    
    def iceCream_flavors(self):
        """Shows all the available flavors"""
        print("We have the greatest flavors you can find it here: \n")
        for flavor in self.flavors:
            print("Flavor: " + flavor)
        

iceCream = IceCreamStand("Spicy Chicken", "Mexican food")
iceCream.iceCream_flavors()