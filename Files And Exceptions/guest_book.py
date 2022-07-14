file_path = "Files And Exceptions/guest_book.txt"

with open(file_path, 'a') as file_object:
    while(True):
        guest_name = input("Write guest's name: \nIf you want to quit type 'q' and press enter\n")
        if guest_name == 'q':
            break
        file_object.write("Guest: " + guest_name + "\n")
