with open("C:\\Users\\Nydhoggr\\Desktop\\Programming\\Python\\Files And Exceptions\\learning_python.txt") as file_object:
    lines = file_object.readlines()

    for line in lines:
        print("\n" + line * 3)
