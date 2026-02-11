class Employee:
    company = "Google"

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"the name of the employee is {self.name}. Salary is {self.salary}. the bond is for {self.bond} years")

e1 = Employee(3400, "john", 3, "tesla")
print(e1.company)
print(Employee.company)#always print the class atttrubute

#Object Introspection
print(dir(e1))