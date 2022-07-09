import time
file_path = "C:\\Users\\Nydhoggr\\Desktop\\Programming\\Python\\Files And Exceptions\\pi_digits.txt"
# with open(file_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# Opening the file again to store the lines in a list 
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line

# Searching my birthday in pi number
birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi be happy")
else:
    print("Your birthday does not appear in the first million digits of pi")

# print(pi_string[:52])

# print(len(pi_string))