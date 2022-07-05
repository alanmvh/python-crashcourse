import car

class ElectricCar(car.Car):
    """Represents aspects of a car specific to electric vehicles"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())