class User:
    def __init__(self, name, email, phoneNumber):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber

    def logout(self):
        self.name = None
        self.email = None
        self.phoneNumber = None
        print('Logged out successfully')