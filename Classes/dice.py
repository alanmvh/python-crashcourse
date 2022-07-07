from random import randint

class Dice():
    def __init__(self):
        self.sides = 6

    def roll_dice(self):
        for x in range(10):
            print("Attempt: " + str(x) + " - number: " + str(randint(1,self.sides)))
    
dice = Dice()
dice.roll_dice()