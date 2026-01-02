# https://www.youtube.com/watch?v=jCzT9XFZ5bw
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.email = f"{first_name}.{last_name}@company.com"

    # In order to continue accessing the email as an attribute you can add '@property' decorator
    # We are defining the 'email' inside our class as a method but we are accessing it like an attribute
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        self.first_name, self.last_name = name.split(" ")

    # below block will get executed when 'del employee.full_name' is invoked
    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None

employee = Employee("John", "Smith")

print(employee.first_name)
print(employee.last_name)
print(employee.email)

employee.first_name = "Jim"

print(employee.first_name)
print(employee.last_name)
print(employee.email)

employee.full_name = "Vishnu Pradeep"

print(employee.first_name)
print(employee.last_name)
print(employee.email)

def new_func(employee):
    del employee.full_name

new_func(employee)

print(employee.first_name)
print(employee.last_name)
print(employee.email)
