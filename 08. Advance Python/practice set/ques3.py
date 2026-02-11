class Employee:
    def __init__(self, salary):
        self._salary = salary
        
    @property
    def salary(self):
        return self._salary
    
e = Employee(3)
print(e.salary)
