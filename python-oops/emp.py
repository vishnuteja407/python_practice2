class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Smith', 60000)

print(emp_1.email)
print(emp_2.email)

# emp_1.first = 'Will'

print(emp_1.fullname())

print(Employee.fullname(emp_1))