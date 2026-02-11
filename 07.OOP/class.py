#A class is a blueprint or a template

#Object is a specific instance created from the class

class Employee:
    company = "HP"

    def get_salary(self):#self is important here because self is a way to reference the object of the class is being created
        return 34000

e = Employee()
print(e.get_salary())

e2 = Employee()
print(e2.get_salary())
print(e2.company)
print(e.company)