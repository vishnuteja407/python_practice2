class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Smith', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.__dict__)
# print(Employee.__dict__)
# Employee.raise_amt = 1.05

emp_1.raise_amt = 1.05

# print(emp_1.__dict__)
# print(Employee.__dict__)  # Employee namespace

print(emp_1.raise_amt)
print(emp_2.raise_amt)
print(Employee.raise_amt)

print(Employee.num_of_emps)