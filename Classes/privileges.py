class Privilege():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges that administrators have"""
        print("This user has the following permissions: ")
        for permission in self.privileges:
            print("Permissions: " + permission)    