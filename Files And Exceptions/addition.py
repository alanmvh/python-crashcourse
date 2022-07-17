try:
    number_one = input("Type 'q' if you want to quit\nEnter number one: ")
    number_one = int(number_one)
    if number_one == "rq":
        exit()
    number_two = input("\nEnter number two:")
    number_two = int(number_two)
except ValueError:
    print("Value that you set is not a number!")
else:
    print("Both inputs are numbers... Great!!")

# Adition Calculator Exercise
while(True):
    try:
        number_one = input("Type 'q' if you want to quit\nEnter number one: ")
        number_one = int(number_one)
        if number_one == "rq":
            exit()
        number_two = input("\nEnter number two:")
        number_two = int(number_two)
    except ValueError:
        print("Value that you set is not a number try again!")
        pass
    else:
        print("Both inputs are numbers... Great!!")