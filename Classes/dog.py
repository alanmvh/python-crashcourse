class Dog():
    """A simple attemp to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + "is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + "rolled over")

my_dog = Dog('willie', 6)
print('My dogs name is ' + my_dog.name.title())
my_dog.roll_over()
your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")