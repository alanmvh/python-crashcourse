import json

# Load the username, if it has been sotred previously
# Otherwise, prompt for the username and store it
filename = "username.json"

def define_user():
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name: ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back")
    else:
        print("Welcome back" + username)
        username_verification = input("Is this your username in case not type 'q' and enter to quit")
        return username_verification == 'q'

while(define_user() != False):
    define_user()

