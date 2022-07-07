import car

class ElectricCar(car.Car):
    """
    Initialize attributes of the parent class.
    Then initialize attributes specific to an electric car
    """


    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        """
        Print a statement describing the battery size
        """
        print("This car has a " + str(self.battery_size) + "-kWh battery")
    
    def fill_gast_tank():
        """
        Electric cars dont have gas tanks
        """
my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())