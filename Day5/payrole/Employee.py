from Day5.payrole.Person import Person

class Employee(Person):

    # private value (not accessible outside of class)
    __salary = 0.0

    def __init__(   self,
                    firstname, 
                    lastname, 
                    address, 
                    employeenumber):
        super().__init__(firstname, lastname, address)
        self.employeenumber = employeenumber
    
    def setsalary(self, value):
        if value <= 0:
            print("Error: Salary has no value")
        else:
            self.__salary = value

    def __str__(self):
        return super().__str__() + f"\nEmployee:{self.employeenumber} \nSalary:{self.__salary}"

    def getsalary(self):
        return self.__salary