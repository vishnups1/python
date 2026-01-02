"""
Inheritance allows us to inherit attributes and methods from a parent class to a child class. We can create a base class (parent class) and then create derived classes (child classes) that inherit from the base class.

We can override or extend the functionality without affecting the base class (Parent).

- Method resolution order. The places python searches for attributes and methods
  - print(help(<CLASS_NAME>))
- isinstance()
- issubclass()

Every class in python inherits from "builtins.object" base class
"""

class Employee:

    # class attribute
    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):

        # object attributes
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def full_name(slef):
        pass

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@company.com"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):

    # class attribute
    raise_amt = 1.10

    # sometimes we have to initiate our sub classes with more information than our parent classes can handle

    def __init__(self, first_name, last_name, pay, prog_language):
        super().__init__(first_name, last_name, pay)
        self.progr_language = prog_language

class Manager(Employee):
    
    def __init__(self, first_name, last_name, pay, employees = None):
        super().__init__(first_name, last_name, pay)
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        if self.employees:
            for emp in self.employees:
                print(f"--> {emp.email}")

manager = Manager("Andrew", "Carbone", 5000)

emp1 = Employee("Vishnu", "Pradeep", 4000)
emp2 = Employee("Aman", "Krishna", 4500)

manager.add_employee(emp1)
manager.add_employee(emp2)

manager.print_employees()