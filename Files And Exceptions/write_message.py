filename = "Files And Exceptions/programming.txt"


with open(filename, 'a') as file_object:
    file_object.write("I love programming"*2)
    file_object.write("I love creating apps that can run in a browser.\n")
