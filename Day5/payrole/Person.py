class Person:

    # Class instances initialisation
    def __init__(self, firstname, lastname, address):
        self.firsname = firstname
        self.lastname = lastname
        self.address = address

    # Example method used in class
    def get_fullname(self):
        return self.firsname + " " + self.lastname

    # Creates a friendly string printout of class
    def __str__(self):
        return f"Full name: {self.firsname}{self.address}"
        