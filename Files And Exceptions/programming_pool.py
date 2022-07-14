file_path = "Files And Exceptions/reasons.txt"

with open(file_path, 'a') as file_object:
    while(True):
        reason = input("Why do you love programming?: \n")
        file_object.write(reason)