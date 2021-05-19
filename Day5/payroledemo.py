from Day5.payrole.Employee import Employee
from Day5.payrole.Address import Address
from Day5.payrole.Person import Person

billsaddress = Address(1, "High Street", "Gourock", "PA19 FG5")
employeebill = Employee("Bill", "Bloggs", billsaddress, "ABC123")
employeebill.setsalary(999.99)

print(employeebill)
print("Salary:", employeebill.getsalary())