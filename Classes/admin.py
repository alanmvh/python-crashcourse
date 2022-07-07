class User():
    def __init__(self, first_name, last_name, nickname):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
    
    def describe_user(self):
        """Prints a summary of the user's information"""
        print("User's name is: " + self.first_name + ' ' + self.last_name + " known as: " + self.alias)

class Administrator(User):
    def __init__(self, first_name, last_name, nickname):
        super().__init__(first_name, last_name, nickname)
        """Initializes Admin attributes and calls init from super class"""
        self.privileges = ["Can add post", "Can delete post", "Can ban user"]

    def show_privileges(self):
        """Display the privileges that administrators have"""
        print("This user has the following permissions: ")
        for permission in self.privileges:
            print("Permissions: " + permission)

user = Administrator("Alan", "Villarreal", "Alan")
user.show_privileges()