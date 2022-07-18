import json

username = input("Enter your name: ")

filename = "Files And Exceptions/user.json"
with open(filename) as f_obj:
    json.dump(username, f_obj)
    print("We will remember you when you come back " + username)
    