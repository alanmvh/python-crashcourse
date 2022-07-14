user_name = input("Write your name: \n")
guest_path = "Files And Exceptions/guest.txt"

with open(guest_path, 'w') as file_object:
    file_object.write(user_name)